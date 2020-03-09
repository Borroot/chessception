from audio import extract
import pytest

# Use the following words to test the regex.
#   a = apple
#   b = bean
#   c = carrot
#   d = date
#   e = endive
#   f = fig
#   g = grape
#   h = honey

def test_extract_letter_first():
    cases = [
        ['apple 1 to apple 2' , 'a1 a2'],
        ['bean 1 to apple 2'  , 'b1 a2'],
        ['carrot 1 to apple 2', 'c1 a2'],
        ['date 1 to apple 2'  , 'd1 a2'],
        ['endive 1 to apple 2', 'e1 a2'],
        ['fig 1 to apple 2'   , 'f1 a2'],
        ['grape 1 to apple 2' , 'g1 a2'],
        ['honey 1 to apple 2' , 'h1 a2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_letter_second():
    cases = [
        ['apple 1 to apple 2' , 'a1 a2'],
        ['apple 1 to bean 2'  , 'a1 b2'],
        ['apple 1 to carrot 2', 'a1 c2'],
        ['apple 1 to date 2'  , 'a1 d2'],
        ['apple 1 to endive 2', 'a1 e2'],
        ['apple 1 to fig 2'   , 'a1 f2'],
        ['apple 1 to grape 2' , 'a1 g2'],
        ['apple 1 to honey 2' , 'a1 h2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_number_first():
    cases = [
        ['apple 1 to bean 1', 'a1 b1'],
        ['apple 2 to bean 1', 'a2 b1'],
        ['apple 3 to bean 1', 'a3 b1'],
        ['apple 4 to bean 1', 'a4 b1'],
        ['apple 5 to bean 1', 'a5 b1'],
        ['apple 6 to bean 1', 'a6 b1'],
        ['apple 7 to bean 1', 'a7 b1'],
        ['apple 8 to bean 1', 'a8 b1']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_number_second():
    cases = [
        ['apple 1 to bean 1', 'a1 b1'],
        ['apple 1 to bean 2', 'a1 b2'],
        ['apple 1 to bean 3', 'a1 b3'],
        ['apple 1 to bean 4', 'a1 b4'],
        ['apple 1 to bean 5', 'a1 b5'],
        ['apple 1 to bean 6', 'a1 b6'],
        ['apple 1 to bean 7', 'a1 b7'],
        ['apple 1 to bean 8', 'a1 b8']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_seperator():
    cases = [
        ['apple 1 to bean 2'     , 'a1 b2'],
        ['apple 1 too bean 2'    , 'a1 b2'],
        ['apple 1 towards bean 2', 'a1 b2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_size_short():
    cases = [
        ['lorem a1 towards b2'                  , 'a1 b2'],
        ['a1 towards b2 lorem'                  , 'a1 b2'],
        ['lorem a1 towards b2 lorem'            , 'a1 b2'],

        ['lorem ipsum a1 towards b2'            , 'a1 b2'],
        ['a1 towards b2 lorem ipsum'            , 'a1 b2'],
        ['lorem ipsum a1 towards b2 lorem ipsum', 'a1 b2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_size_long():
    cases = [
        ['lorem apple 1 towards bean 2'                  , 'a1 b2'],
        ['apple 1 towards bean 2 lorem'                  , 'a1 b2'],
        ['lorem apple 1 towards bean 2 lorem'            , 'a1 b2'],

        ['lorem ipsum apple 1 towards bean 2'            , 'a1 b2'],
        ['apple 1 towards bean 2 lorem ipsum'            , 'a1 b2'],
        ['lorem ipsum apple 1 towards bean 2 lorem ipsum', 'a1 b2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_upper_lower_short():
    cases = [
        ['a1 towards b2', 'a1 b2'],
        ['A1 towards b2', 'a1 b2'],
        ['a1 towards B2', 'a1 b2'],
        ['A1 towards B2', 'a1 b2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_upper_lower_long():
    cases = [
        ['apple 1 towards bean 2', 'a1 b2'],
        ['Apple 1 towards bean 2', 'a1 b2'],
        ['apple 1 towards Bean 2', 'a1 b2'],
        ['Apple 1 towards Bean 2', 'a1 b2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_upper_lower_seperator():
    cases = [
        ['apple 1 towards bean 2', 'a1 b2'],
        ['apple 1 Towards bean 2', 'a1 b2'],
        ['apple 1 toWaRDs bean 2', 'a1 b2'],
        ['apple 1 TOWARDS bean 2', 'a1 b2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_error():
    cases = [
        ['5 towards bishop 3'],
        ]

    with pytest.raises(ValueError):
        for case in cases:
            extract(case[0])
