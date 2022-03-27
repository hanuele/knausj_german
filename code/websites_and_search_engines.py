from .user_settings import get_list_from_csv
from talon import Module, Context
from urllib.parse import quote_plus

mod = Module()
ctx = Context()
ctx.matches = r"""
language: de_DE
"""

website_defaults = {
    "amazon": "https://www.amazon.de/",
    "dropbox": "https://dropbox.com/",
    "google": "https://www.google.de/",
    "google calendar": "https://calendar.google.com",
    "google maps": "https://maps.google.de/",
    "google scholar": "https://scholar.google.com/",
    "gmail": "https://mail.google.com/",
    "github": "https://github.com/",
    "gist": "https://gist.github.com/",
    "wikipedia": "https://de.wikipedia.org/",
    "youtube": "https://www.youtube.com/",
}

_search_engine_defaults = {
    "amazon": "https://www.amazon.de/s/?field-keywords=%s",
    "google": "https://www.google.de/search?q=%s",
    "map": "https://maps.google.com/maps?q=%s",
    "scholar": "https://scholar.google.com/scholar?q=%s",
    "wiki": "https://de.wikipedia.org/w/index.php?search=%s",
}

ctx = Context()
ctx.lists["self.website"] = get_list_from_csv(
    "websites.csv",
    headers=("URL", "Spoken name"),
    default=website_defaults,
)
ctx.lists["self.search_engine"] = get_list_from_csv(
    "search_engines.csv",
    headers=("URL Template", "Name"),
    default=_search_engine_defaults,
)
