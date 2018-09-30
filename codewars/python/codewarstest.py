"""Adapt unittest to CodeWars style tests."""


def assert_equals(val, result, default_message=''):
    """Adapate CodeWars assert_equals func to unittests."""
    message = ["FAILED", "Passed"]
    comp = ["!=", "="]
    success = (val == result)

    if default_message:
        print(f"Test {message[success]}: {default_message}")
    else:
        print(f"Test {message[success]}: {val} {comp[success]} {result}")
