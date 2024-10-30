import logging
from pathlib import Path
from subprocess import PIPE, Popen

from Cython.Build import cythonize
from setuptools import Distribution, find_packages, setup


# fmt: off
def compile_cpy(target: str) -> Distribution:
    packages = find_packages(exclude=["test", "test.*"]) # Mostly indicated with __init__.py
    module = [f"{package.replace('.', '/')}/*.py" for package in packages]

    return setup(
        # Package name
        name=target,

        # Build share object
        script_args=["build_ext"],
        options={"build_ext": {"parallel": 8}},

        # Package locating
        include_package_data=True,
        packages=packages,
        verbose = False,

        # Cython extensions
        ext_modules=cythonize(
            module,
            nthreads=8,
            build_dir="cython",
            compiler_directives={
                "overflowcheck": True,
                "language_level": "3",
                "emit_code_comments": False,
            },
        ),
    )


# fmt: on
def compile_ts(static: str | Path) -> None:
    def _rmtree(path: Path) -> None:
        for child in path.glob("*"):
            child.unlink() if child.is_file() else _rmtree(child)
        path.rmdir()

    log = logging.getLogger("wp")
    log.setLevel(logging.INFO)

    npm_i = ["npm", "install", "--omit=dev"]
    npm_wp = ["npm", "run", "webpack"]

    if not isinstance(static, Path):
        static = Path(static)
    node = Path("node_modules")

    # npm install if node_modules not found
    if not node.is_dir():
        process = Popen(npm_i, stdout=PIPE, stderr=PIPE)  # noqa: S603
        stdout, _ = process.communicate()
        log.info(stdout.decode())

    # remove all webpack files
    for path in static.glob("*"):
        if path.is_dir() and path.name in {"js", "css"}:
            _rmtree(path)

    # npm run tsc (defined in package.json)
    process = Popen(npm_wp, stdout=PIPE, stderr=PIPE)  # noqa: S603
    stdout, _ = process.communicate()
    log.info(stdout.decode())


if __name__ == "__main__":
    compile_cpy("webapp")
    compile_ts("webapp/static")
