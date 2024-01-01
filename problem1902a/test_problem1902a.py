import io
import pytest

from problem1902a import main

def test_multiple_testcases(capsys):
    stdin_stream = io.StringIO("3\n2\n00\n2\n11\n2\n10\n")

    main(stdin_stream)
    # Retrieve stdout content
    out, _ = capsys.readouterr()

    assert out == "YES\nNO\nYES\n"


@pytest.mark.parametrize("test_input,expected", [
    ("00000", "YES"),
    ("11111", "NO"),
    ("010101", "YES"),
    ("01111", "YES"),
    ("11101", "YES"),
])
def test_one_case(capsys, test_input, expected):
    stdin_stream = io.StringIO("1\n%d\n%s\n" % (len(test_input), test_input))

    main(stdin_stream)
    out, _ = capsys.readouterr()

    assert out == expected + "\n"
