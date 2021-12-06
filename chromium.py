from os import listdir, path
from pathlib import Path
from sys import modules
from typing import Union


def get_executable_path() -> Path | None:
    parent_folder = (
        Path(modules["playwright"].__file__).parent / "driver" / "package" / ".local-browsers"
    )

    if not path.exists(parent_folder):
        return None

    child_folders = [
        name
        for name in listdir(parent_folder)
        if path.isdir(parent_folder / name) and name.strip().lower().startswith("chromium")
    ]

    if len(child_folders) != 1:
        return None

    chromium_folder = child_folders[0]

    return parent_folder / chromium_folder / "chrome-win" / "chrome.exe"
