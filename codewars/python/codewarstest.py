"""Adapt unittest to CodeWars style tests."""
import unittest


def assert_equals(val, result, message_fail=''):
    """Adapate CodeWars assert_equals func to unittests."""
    test = unittest.TestCase()

    test.assertEqual(val, result, message_fail)
    print(f"{val} = {result}: Test Passed")
