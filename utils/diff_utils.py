import difflib


def get_code_diff(before_code: str, after_code: str) -> str:
    before_lines = before_code.splitlines()
    after_lines = after_code.splitlines()

    diff = difflib.unified_diff(
        before_lines,
        after_lines,
        lineterm="",
        fromfile="before.py",
        tofile="after.py"
    )

    return "\n".join(diff)
