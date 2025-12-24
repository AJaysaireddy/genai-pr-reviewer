PRIORITY = 2
REVIEW_ID = "EDGE"


def run(before_code, after_code):
    issues = []

    if "if" not in after_code:
        issues.append(("[MEDIUM]", "No input validation or guard conditions detected."))

    if not issues:
        issues.append(("[LOW]", "No obvious edge cases detected."))

    return "EDGE CASE REVIEW", format_output(issues)


def format_output(issues):
    return "\n- " + "\n- ".join(f"{level} {text}" for level, text in issues)
