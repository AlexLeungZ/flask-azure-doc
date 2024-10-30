from argparse import ArgumentDefaultsHelpFormatter as ADHF
from argparse import ArgumentParser, Namespace
from socket import AF_INET, SOCK_DGRAM, socket

from flask import Flask
from waitress import serve

from webapp import create_app


class Args(Namespace):
    flask: bool
    debug: bool
    test: bool
    host: str | None
    port: int | None


def get_args() -> Args:
    flask = ["-f", "--flask"]
    debug = ["-d", "--debug"]
    test = ["-t", "--test"]
    host = ["-s", "--host"]
    port = ["-p", "--port"]

    parser = ArgumentParser(formatter_class=ADHF, description="Webapp runner with waitress")
    group = parser.add_mutually_exclusive_group()

    group.add_argument(*flask, dest="flask", action="store_true", help="run under flask")
    group.add_argument(*debug, dest="debug", action="store_true", help="debug under flask")
    group.add_argument(*test, dest="test", action="store_true", help="create app only")
    parser.add_argument(*host, dest="host", type=str, help="server host")
    parser.add_argument(*port, dest="port", type=int, help="server port")

    return parser.parse_args(namespace=Args())


# Get Current IP
def get_ip() -> str:
    with socket(AF_INET, SOCK_DGRAM) as sck:
        sck.connect(("192.168.0.0", 0))
        return sck.getsockname()[0]


def main() -> Flask | None:
    args = get_args()
    host = args.host or get_ip()
    port = args.port or 5000

    if args.test:
        return create_app()

    elif args.flask or args.debug:
        app = create_app(debug=args.debug)
        app.run(host=host, port=port, threaded=True)

    else:
        app = create_app(prod=True)
        serve(app, host=host, port=port)


if __name__ == "__main__":
    main()
