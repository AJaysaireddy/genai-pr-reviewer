from review_engine import run_all_reviews


def main():
    before_code = """
def add(a, b):
    return a + b
"""

    after_code = """
def add(a, b):
    return a - b
"""

    results = run_all_reviews(before_code, after_code)

    for section, output in results.items():
        print(f"\n{section}:")
        print(output)


if __name__ == "__main__":
    main()
