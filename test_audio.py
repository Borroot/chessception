from audio import extract
import pytest

def test_extract_fail():
    cases = [
        ['5 towards bishop 3'],
        ]

    with pytest.raises(ValueError):
        for case in cases:
            extract(case[0])


def test_extract_good():
    cases = [
        ['apple 5 towards doll 3'                       , 'a5 d3'],
        ['hello apple 5 towards doll 3'                 , 'a5 d3'],
        ['hello apple 5 towards doll 3 hey'             , 'a5 d3'],
        ]

    for case in cases:
        assert extract(case[0]) == case[1]
