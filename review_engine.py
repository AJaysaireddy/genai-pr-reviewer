import pkgutil
import reviews


def load_review_modules():
    modules = []
    for module_info in pkgutil.iter_modules(reviews.__path__):
        module = __import__(f"reviews.{module_info.name}", fromlist=["run"])
        modules.append(module)

    return sorted(modules, key=lambda m: m.PRIORITY)


def run_all_reviews(before_code, after_code):
    results = []

    for module in load_review_modules():
        section, output = module.run(before_code, after_code)
        results.append((section, output))

    return results
