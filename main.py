import sys
from pathlib import Path

def translator(syntax):
    syntax = syntax.replace("strout", "print")
    syntax = syntax.replace("func", "def")
    syntax = syntax.replace("run", "exec")
    syntax = syntax.replace("@", "class")
    syntax = syntax.replace("|", "or")
    syntax = syntax.replace("&", "and")
    syntax = syntax.replace("÷", "not")
    syntax = syntax.replace("strin", "input")
    return syntax



def main() -> int:
    if len(sys.argv) < 2:
        print("SCL Interpreter 1.0")
        print("Use: scl file")
        return 1

    file_path = Path(sys.argv[1])

    if file_path.suffix.lower() != ".scl":
        print("InvalidFileError")
        return 1

    if not file_path.is_file():
        print(f"FileNotFoundError: {file_path}")
        return 1

    try:
        source = file_path.read_text(encoding="utf-8")
    except OSError as error:
        print(f"ReadingError: {error}")
        return 1

    python_code = translator(source)

    try:
        exec(compile(python_code, str(file_path), "exec"), {"__name__": "__main__"})
    except Exception as error:
        print(f"RuntimeError: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())