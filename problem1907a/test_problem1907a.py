import io
import pytest

from problem1907a import main


def test_multiple_testcases(capsys):
    stdin_stream = io.StringIO("3\na1\nb2\nc3\n")

    main(stdin_stream)
    # Retrieve stdout content
    out, _ = capsys.readouterr()

    squares = out.rstrip('\n').split('\n')

    # There should be 7+7 output squares in a single case response
    assert len(squares) == 3 * 14

    for got, expected in (
            (squares[:14], 'a2 a3 a4 a5 a6 a7 a8 b1 c1 d1 e1 f1 g1 h1'),
            (squares[14:28], 'b1 b3 b4 b5 b6 b7 b8 a2 c2 d2 e2 f2 g2 h2'),
            (squares[28:], 'c1 c2 c4 c5 c6 c7 c8 a3 b3 d3 e3 f3 g3 h3')
        ):
        assert sorted(got) == sorted(expected.split())


@pytest.mark.parametrize("test_input,expected", [
    ("d5", "d1 d2 b5 g5 h5 d3 e5 f5 d8 a5 d6 d7 c5 d4"),
    ("g7", "g1 g2 g3 g4 g5 g6 g8 a7 b7 c7 d7 e7 f7 h7"),
    ("h6", "h1 h2 h3 h4 h5 h7 h8 a6 b6 c6 d6 e6 f6 g6"),
])
def test_one_case(capsys, test_input, expected):
    stdin_stream = io.StringIO("1\n%s\n" % test_input)

    main(stdin_stream)
    out, _ = capsys.readouterr()

    squares = out.rstrip('\n').split('\n')

    # There should be 7+7 output squares in a single case response
    assert len(squares) == 14
    assert sorted(squares) == sorted(expected.split())
