from webapp.page.api import bp as api
from webapp.page.loader import bp as loader
from webapp.page.root import bp as root

__all__: list[str] = ["api", "root", "loader"]
