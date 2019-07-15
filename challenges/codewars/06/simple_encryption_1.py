def decrypt(encrypted_text, n):
    while n > 0:
        split_1 = encrypted_text[len(encrypted_text) // 2 :]
        split_2 = encrypted_text[: len(encrypted_text) // 2]

        res = ""
        i, j = 0, 0
        while i < len(split_1) and j < len(split_2):
            res = f"{res}{split_1[i]}{split_2[j]}"
            i += 1
            j += 1

        res += split_1[i:]
        res += split_2[j:]

        n -= 1
        encrypted_text = res

    return encrypted_text


def encrypt(text, n):
    while n > 0:
        split_1 = "".join(x for i, x in enumerate(text) if i % 2 == 1)
        split_2 = "".join(x for i, x in enumerate(text) if i % 2 == 0)
        text = f"{split_1}{split_2}"
        n -= 1

    return text


# Tests below this line
# ==============================================================================
import os, sys  # noqa: E401, E402

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import codewarstest as Test  # noqa: E402, pylint: disable=E0401

Test.describe("Basic Tests")
Test.it("Test Encrypt")
Test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
Test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
Test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
Test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
Test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
Test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
Test.assert_equals(
    encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig"
)
Test.assert_equals(encrypt("", 0), "")
Test.assert_equals(encrypt(None, 0), None)

Test.it("Test Decrypt")
Test.assert_equals(decrypt("This is a test!", 0), "This is a test!")
Test.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
Test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
Test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
Test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
Test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
Test.assert_equals(
    decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!"
)
Test.assert_equals(decrypt("", 0), "")
Test.assert_equals(decrypt(None, 0), None)
