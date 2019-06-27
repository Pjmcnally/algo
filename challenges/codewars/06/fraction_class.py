class Fraction:
    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
        self.reduce()

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __add__(self, other):
        new_top = (self.top * other.bottom) + (other.top * self.bottom)
        new_bottom = self.bottom * other.bottom
        return Fraction(new_top, new_bottom)

    def __str__(self):
        return "{}/{}".format(self.top, self.bottom)

    def reduce(self):
        num = gcd(self.top, self.bottom)
        self.top = self.top // num
        self.bottom = self.bottom // num


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


# Tests below this line
# ==============================================================================
import codewarstest as test  # noqa: E402, pylint: disable=C0413
test.assert_equals(Fraction(1, 8), Fraction(1, 8))
test.assert_equals(Fraction(1, 8) + Fraction(4, 5), Fraction(37, 40))
test.assert_equals(
    Fraction(911, 920) + Fraction(980, 906), Fraction(863483, 416760))
test.assert_equals(
    Fraction(610, 941) + Fraction(253, 985), Fraction(838923, 926885))
test.assert_equals(
    Fraction(956, 798) + Fraction(662, 189), Fraction(16880, 3591))
test.assert_equals(
    Fraction(694, 485) + Fraction(853, 861), Fraction(1011239, 417585))
test.assert_equals(
    Fraction(982, 111) + Fraction(219, 561), Fraction(191737, 20757))
test.assert_equals(
    Fraction(344, 873) + Fraction(658, 486), Fraction(41201, 23571))
test.assert_equals(
    Fraction(662, 361) + Fraction(322, 382), Fraction(184563, 68951))
test.assert_equals(
    Fraction(740, 813) + Fraction(184, 348), Fraction(33926, 23577))
test.assert_equals(
    Fraction(579, 441) + Fraction(543, 807), Fraction(78524, 39543))
test.assert_equals(
    Fraction(212, 979) + Fraction(46, 580), Fraction(83997, 283910))
