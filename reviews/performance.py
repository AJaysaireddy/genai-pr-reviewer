PRIORITY = 3
REVIEW_ID = "PERFORMANCE"


def run(before_code, after_code):
    issues = []

    if "for" in after_code:
        issues.append(("[MEDIUM]", "Loop detected; check performance for large inputs."))

    if not issues:
        issues.append(("[LOW]", "No obvious performance concerns detected."))

    return "PERFORMANCE REVIEW", format_output(issues)


def format_output(issues):
    return "\n- " + "\n- ".join(f"{level} {text}" for level, text in issues)
