"""Create test wrapper for CodeWars tests.

Import Code (Add this code the the problem file):
# Tests below this line
# ==============================================================================
import os, sys  # noqa: E401, E402

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import codewarstest  # noqa: E402, pylint: disable=E0401
"""


def assert_equals(val, result, default_message=""):
    """Implement assert_equals func."""
    message = ["FAILED", "Passed"]
    comp = ["!=", "="]
    success = val == result

    if default_message:
        print(f"Test {message[success]}: {default_message}")
    else:
        print(f"Test {message[success]}: {val} {comp[success]} {result}")


def describe(message):
    """Implement describe func."""
    print(message)
