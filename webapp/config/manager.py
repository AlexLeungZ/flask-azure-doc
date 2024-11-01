from dataclasses import dataclass, field
from multiprocessing.managers import BaseManager

from azure.ai.documentintelligence import DocumentIntelligenceClient


@dataclass
class _global:
    # Object can be reassigned here
    client: DocumentIntelligenceClient = field(init=False)


# Attributes as Global Variable
# Attributes are non-reassignable, but sub attributes can be reassigned
class FlaskManager(BaseManager):
    gvar: _global = _global()
