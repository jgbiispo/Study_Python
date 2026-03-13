def is_balanced(expression: str) -> bool:
    stack = []

    for char in expression:
        match char:
            case "(":
                stack.append(char)
            case ")":
                if not stack:
                    return False
                stack.pop()

    return len(stack) == 0


def run_tests():
    test_cases = [
        ("(())", True),
        ("((()))", True),
        ("(()())", True),
        ("()", True),
        ("", True),
        ("(()", False),
        ("())", False),
        (")((", False),
        (")()", False),
        ("(((", False),
        ("((((", False),
    ]

    for expression, expected in test_cases:
        result = is_balanced(expression)
        status = "PASS:" if result == expected else "ERROR:"
        print(f"{status} is_balanced('{expression}') = {result} (esperado: {expected})")
