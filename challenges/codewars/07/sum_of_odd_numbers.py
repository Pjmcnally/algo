def row_sum_odd_numbers(n):
    start, end = get_odd_triangle_row(n)
    return calculate_seq_sum(start, end, 2)


def get_odd_triangle_row(row):
    row -= 1  # 0 index rows
    row_start = 2 * calculate_seq_sum(1, row) + 1
    row_end = row_start + (2 * row)
    return row_start, row_end


def calculate_seq_sum(start, end, step=1):
    num_count = ((end - start) // step) + 1
    seq_sum = num_count * (start + end) // 2
    return seq_sum


# Tests below this line
# ==============================================================================
import os, sys  # noqa: E401, E402

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import codewarstest as Test  # noqa: E402, pylint: disable=E0401

Test.assert_equals(row_sum_odd_numbers(1), 1)
Test.assert_equals(row_sum_odd_numbers(2), 8)
Test.assert_equals(row_sum_odd_numbers(13), 2197)
Test.assert_equals(row_sum_odd_numbers(19), 6859)
Test.assert_equals(row_sum_odd_numbers(41), 68921)
