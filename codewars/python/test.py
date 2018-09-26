import unittest

test = unittest.TestCase()


def assert_equals(val, result, message_fail=''):
    test.assertEqual(val, result, message_fail)
    print(f"{val} = {result}: Test Passed")
