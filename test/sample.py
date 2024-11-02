import json
from pathlib import Path

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from dotenv import dotenv_values, find_dotenv


def load_azure() -> tuple[str, AzureKeyCredential]:
    envvar = dotenv_values(find_dotenv())
    return envvar.get("AZURE_ENDPOINT") or "", AzureKeyCredential(envvar.get("AZURE_API_KEY") or "")


def analyze_invoice(filename: str) -> None:
    document_intelligence_client = DocumentIntelligenceClient(*load_azure())

    path_to_sample_document = Path(filename)
    with path_to_sample_document.open("rb") as file:
        poller = document_intelligence_client.begin_analyze_document(
            "prebuilt-invoice", analyze_request=file, locale="en-US", content_type="application/octet-stream"
        )

    invoices = poller.result()

    # [START analyze_invoices]
    if invoices.documents:
        for idx, invoice in enumerate(invoices.documents):
            # jsonify invoice and save as a json file
            path = Path(f"{filename}_{idx + 1}.json")
            print(f"Invoice {idx + 1} analyzed and saved as invoice_{idx + 1}.json")

            with path.open("w") as file:
                json.dump(invoice.as_dict(), file)

            print(f"--------Analyzing invoice #{idx + 1}--------")
            if field := invoice.fields:
                print(field)


if __name__ == "__main__":
    analyze_invoice("./invoice_2.pdf")
