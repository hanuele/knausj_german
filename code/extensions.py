from .user_settings import get_list_from_csv
from talon import Module, Context, actions, app

mod = Module()
mod.list("file_extension", desc="A file extension, such as .py")

_file_extensions_defaults = {
    "punkt pü": ".py",
    "punkt talon": ".talon",
    "punkt mark down": ".md",
    "punkt shell": ".sh",
    "punkt vim": ".vim",
    "punkt zeh": ".c",
    "punkt sie scharp": ".cs",
    "punkt com": ".com",
    "punkt net": ".net",
    "punkt org": ".org",
    "punkt us": ".us",
    "punkt U S": ".us",
    "punkt exe": ".exe",
    "punkt bin": ".bin",
    "punkt bend": ".bin",
    "punkt jason": ".json",
    "punkt dscheison": ".json",
    "punkt J S": ".js",
    "punkt java script": ".js",
    "punkt TS": ".ts",
    "punkt type script": ".ts",
    "punkt csv": ".csv",
    "punkt text": ".txt",
}

file_extensions = get_list_from_csv(
    "file_extensions.csv",
    headers=("File extension", "Name"),
    default=_file_extensions_defaults,
)

ctx = Context()
ctx.lists["self.file_extension"] = file_extensions