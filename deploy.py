from collections.abc import Iterable
from itertools import chain
from pathlib import Path
from typing import TypeAlias
from zipfile import ZipFile

from compile import compile_cpy, compile_ts

ExtPair: TypeAlias = dict[str, list[str]]


# Return a list of files in the given folder with the given extensions.
def get_file(folder: Path, pair: ExtPair) -> Iterable[Path]:
    return (
        file
        for path in folder.iterdir()
        if path.is_dir() and path.name in pair
        for ext in pair[path.name]
        for file in path.rglob(ext)
        if file.is_file()
    )


# Select extensions for top level folders.
def cwd_file() -> ExtPair:
    return {
        "media": ["*.placeholder"],
        "temp": ["*.placeholder"],
    }


# Select extensions for webapp folder.
def app_file() -> ExtPair:
    return {
        "handler": ["*.json", "*.txt"],
        "static": ["*.css", "*.js", "*.ico"],
        "templates": ["*.html", "*.jinja"],
    }


def main() -> None:
    deploy = "deploy.zip"
    build = Path("build")
    webapp = Path("webapp")

    if not webapp.is_dir():
        raise FileExistsError(f"{webapp} does not exist.")

    file_cwd = get_file(Path(), cwd_file())
    file_web = get_file(webapp, app_file())
    file_top = ["environment.yml", "webapp.py", ".env.dev", ".env"]

    # If build dir not found, build .so first.
    if not build.is_dir():
        compile_cpy(webapp.name)
    libs = (so for lib in build.glob("lib.*") for so in lib.rglob("*.so"))

    # FileNotFoundError would be thrown if npm is not installed.
    compile_ts(webapp / "static")

    with ZipFile(deploy, "w", 0) as container:
        # Copying .so files
        for path in libs:
            container.write(path, Path(*path.parts[2:]))

        # Copying files from selected files
        for file in chain(file_cwd, file_web, file_top):
            container.write(file)


if __name__ == "__main__":
    main()
