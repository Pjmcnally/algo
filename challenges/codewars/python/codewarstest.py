"""Create test wrapper for CodeWars tests."""


def assert_equals(val, result, default_message=''):
    """Implement assert_equals func."""
    message = ["FAILED", "Passed"]
    comp = ["!=", "="]
    success = (val == result)

    if default_message:
        print(f"Test {message[success]}: {default_message}")
    else:
        print(f"Test {message[success]}: {val} {comp[success]} {result}")


def describe(message):
    """Implement describe func"""
    print(message)
