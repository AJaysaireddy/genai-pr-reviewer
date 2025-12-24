PRIORITY = 4
REVIEW_ID = "READABILITY"


def run(before_code, after_code):
    issues = []

    if "a, b" in after_code:
        issues.append(("[LOW]", "Parameter names 'a' and 'b' are not descriptive."))

    if len(after_code.strip().splitlines()) <= 3:
        issues.append(("[LOW]", "Function is very short; consider adding a docstring."))

    if not issues:
        issues.append(("[LOW]", "Code readability looks good."))

    return "READABILITY REVIEW", format_output(issues)


def format_output(issues):
    return "\n- " + "\n- ".join(f"{level} {text}" for level, text in issues)
