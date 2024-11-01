import uuid
from collections.abc import Generator
from datetime import datetime
from hashlib import sha512
from typing import IO, NotRequired, TypedDict

from azure.ai.documentintelligence import DocumentIntelligenceClient as Client
from azure.ai.documentintelligence.models import Document, DocumentField
from azure.core.credentials import AzureKeyCredential
from flask import Config
from werkzeug.datastructures import FileStorage as FS


class Details(TypedDict):
    fileLength: NotRequired[int | None]
    invoiceId: NotRequired[str | None]
    invoiceDate: NotRequired[str | None]
    dueDate: NotRequired[str | None]

    customerId: NotRequired[str | None]
    customerName: NotRequired[str | None]
    invoiceTotal: NotRequired[str | None]
    amountDue: NotRequired[str | None]


class Extractor(Details):
    timestamp: float
    fileIndex: str
    filename: str
    filehash: str


def get_filehash(file: IO[bytes]) -> tuple[str, int]:
    return sha512(file.read()).hexdigest(), file.seek(0)


def azure_load(config: Config) -> Client:
    return Client(config.get("AZURE_ENDPOINT") or "", AzureKeyCredential(config.get("AZURE_API_KEY") or ""))


def azure_analyze(client: Client, file: FS, model: str, local: str = "en-US") -> tuple[list[Document], str] | None:
    filehash = get_filehash(file.stream)
    poller = client.begin_analyze_document(model, file.stream, locale=local, content_type="application/octet-stream")

    if parsed := poller.result().documents:
        return parsed, filehash[0]


def conf_check[T](value: T | None, confidence: float | None, threshold: float = 0.75) -> T | None:
    if (confidence or 0) > threshold:
        return value


def value_str(field: dict[str, DocumentField], val: str) -> str | None:
    if (key := field.get(val)) and (value := conf_check(key.value_string, key.confidence)):
        return value


def value_date(field: dict[str, DocumentField], val: str) -> str | None:
    if (key := field.get(val)) and (value := conf_check(key.value_date, key.confidence)):
        return str(value)


def value_curr(field: dict[str, DocumentField], val: str) -> str | None:
    if (key := field.get(val)) and (value := conf_check(key.value_currency, key.confidence)):
        return f"{value.currency_code}{value.amount}"


def name_index(file: str, idx: int) -> str:
    return f"{file}_{idx}" if idx > 0 else file


def doc_details(doc: Document) -> Details | None:
    if (fields := doc.fields) and (bounders := doc.bounding_regions):
        return {
            "fileLength": len(bounders),
            "invoiceId": value_str(fields, "InvoiceId"),
            "invoiceDate": value_date(fields, "InvoiceDate"),
            "dueDate": value_date(fields, "DueDate"),
            "customerId": value_str(fields, "CustomerId"),
            "customerName": value_str(fields, "CustomerName"),
            "invoiceTotal": value_curr(fields, "InvoiceTotal"),
            "amountDue": value_curr(fields, "AmountDue"),
        }


def doc_extract(file: str, idx: int, filehash: str, doc: Document) -> Extractor:
    return {
        "timestamp": datetime.now().timestamp(),
        "fileIndex": str(uuid.uuid4()),
        "filename": name_index(file, idx),
        "filehash": filehash,
        **(doc_details(doc) or Details()),
    }


def files2pipe(files: list[FS], client: Client) -> Generator[Extractor]:
    for file in files:
        if (name := file.filename) and (analyzes := azure_analyze(client, file, "prebuilt-invoice")):
            for idx, analyze in enumerate(analyzes[0]):
                yield doc_extract(name, idx, analyzes[1], analyze)
