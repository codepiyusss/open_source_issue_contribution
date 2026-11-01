import shlex

def run_shell() -> None:
    """Read and execute commands until user exits"""
    from fixit.cli import main

    while True:
        try:
            line = input("fixit> ")
        except(EOFError, KeyboardInterrupt):
            print()
            break

        if not line.strip():
            continue

        try:
            args = shlex.split(line)
        except ValueError as error:
            print(f"Error: {error}")

        if args[0] in ('exit', 'quit'):
            break

        if args[0] == "shell":
            print("Error: already in active shell")

        try:
            main(args)
        except SystemExit:
            # argparse may exit on invalid input or --help
            # this is to keep the shell running.
            continue