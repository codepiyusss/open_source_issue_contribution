"""Command line entry point: `fixit <command>`."""
import argparse
import sys
import uuid

from fixit import __version__, convert, jsonfmt, password, textutils, wordcount

CONVERSIONS = {
    "c2f": convert.celsius_to_fahrenheit,
    "f2c": convert.fahrenheit_to_celsius,
    "km2mi": convert.km_to_miles,
    "mi2km": convert.miles_to_km,
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="fixit", description="A tiny toolbox to practice open source.")
    parser.add_argument("--version", action="version", version=f"fixit {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    wc = sub.add_parser("wc", help="count words, lines and characters")
    wc.add_argument("text")

    cv = sub.add_parser("convert", help="convert units")
    cv.add_argument("value", type=float)
    cv.add_argument("kind", choices=sorted(CONVERSIONS))

    pw = sub.add_parser("password", help="generate a password")
    pw.add_argument("--length", type=int, default=12)
    pw.add_argument("--symbols", action="store_true")

    uid = sub.add_parser("uuid", help="generate UUIDs")
    uid.add_argument("--count", type=int, default=1)

    js = sub.add_parser("json", help="pretty-print JSON")
    js.add_argument("raw")

    pal = sub.add_parser("palindrome", help="check if text is a palindrome")
    pal.add_argument("text")

    rw = sub.add_parser("reverse", help="reverse the words in a sentence")
    rw.add_argument("text")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "wc":
        print(f"words={wordcount.count_words(args.text)} "
              f"lines={wordcount.count_lines(args.text)} "
              f"chars={wordcount.count_chars(args.text)}")
    elif args.command == "convert":
        print(CONVERSIONS[args.kind](args.value))
    elif args.command == "password":
        print(password.generate(args.length, use_symbols=args.symbols))
    elif args.command == "uuid":
        for _ in range(args.count):
            print(uuid.uuid4())
    elif args.command == "json":
        print(jsonfmt.format_json(args.raw))
    elif args.command == "palindrome":
        print(textutils.is_palindrome(args.text))
    elif args.command == "reverse":
        print(textutils.reverse_words(args.text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
