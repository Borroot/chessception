from audio import extract
import pytest

# Use the following words to test the regex.
#   a = apple  b = bean c = carrot d = date
#   e = endive f = fig  g = grape  h = honey

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

def test_extract_duplicates_short():
    cases = [
        ['c3 a1 towards b2'   , 'a1 b2'],
        ['a1 towards b2 c3'   , 'a1 b2'],
        ['c3 a1 towards b2 c3', 'a1 b2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_duplicates_long():
    cases = [
        ['carrot 3 apple 1 towards bean 2'         , 'a1 b2'],
        ['apple 1 towards bean 2 carrot 3'         , 'a1 b2'],
        ['carrot 3 apple 1 towards bean 2 carrot 3', 'a1 b2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_duplicates_combined():
    cases = [
        ['c3 apple 1 towards bean 2'           , 'a1 b2'],
        ['carrot 3 a1 towards bean 2'          , 'a1 b2'],
        ['carrot 3 apple 1 towards b2'         , 'a1 b2'],
        ['c3 a1 towards bean 2'                , 'a1 b2'],
        ['c3 apple 1 towards b2'               , 'a1 b2'],
        ['carrot 3 a1 towards b2'              , 'a1 b2'],

        ['a1 towards bean 2 carrot 3'          , 'a1 b2'],
        ['apple 1 towards b2 carrot 3'         , 'a1 b2'],
        ['apple 1 towards bean 2 c3'           , 'a1 b2'],
        ['a1 towards b2 carrot 3'              , 'a1 b2'],
        ['a1 towards bean 2 c3'                , 'a1 b2'],
        ['apple 1 towards b2 c3'               , 'a1 b2'],

        ['c3 apple 1 towards bean 2 carrot 3'  , 'a1 b2'],
        ['carrot 3 a1 towards bean 2 carrot 3' , 'a1 b2'],
        ['carrot 3 apple 1 towards b2 carrot 3', 'a1 b2'],
        ['carrot 3 apple 1 towards bean 2 c3'  , 'a1 b2'],
        ['c3 a1 towards bean 2 carrot 3'       , 'a1 b2'],
        ['c3 apple 1 towards b2 carrot 3'      , 'a1 b2'],
        ['c3 apple 1 towards bean 2 c3'        , 'a1 b2'],

        ['carrot 3 a1 towards b2 carrot 3'     , 'a1 b2'],
        ['carrot 3 a1 towards bean 2 c3'       , 'a1 b2'],
        ['carrot 3 apple 1 towards b2 c3'      , 'a1 b2'],

        ['carrot 3 a1 towards b2 c3'           , 'a1 b2'],
        ['c3 apple 1 towards b2 c3'            , 'a1 b2'],
        ['c3 a1 towards bean 2 c3'             , 'a1 b2'],
        ['c3 a1 towards b2 carrot 3'           , 'a1 b2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_synonyms():
    cases = [
        ['apple one towards bean 2'  , 'a1 b2'],
        ['apple won towards bean 2'  , 'a1 b2'],

        ['apple two towards bean 2'  , 'a2 b2'],
        ['apple too towards bean 2'  , 'a2 b2'],
        ['apple to towards bean 2'   , 'a2 b2'],

        ['apple three towards bean 2', 'a3 b2'],
        ['apple tree towards bean 2' , 'a3 b2'],

        ['apple four towards bean 2' , 'a4 b2'],
        ['apple fore towards bean 2' , 'a4 b2'],
        ['apple for towards bean 2'  , 'a4 b2'],

        ['apple five towards bean 2' , 'a5 b2'],
        ['apple hive towards bean 2' , 'a5 b2'],

        ['apple six towards bean 2'  , 'a6 b2'],
        ['apple sics towards bean 2' , 'a6 b2'],

        ['apple seven towards bean 2', 'a7 b2'],

        ['apple eight towards bean 2', 'a8 b2'],
        ['apple ait towards bean 2'  , 'a8 b2'],
        ['apple ate towards bean 2'  , 'a8 b2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_combined():
    cases = [
        ['apple 1 towards b2'      , 'a1 b2'],
        ['a1 towards bean 2'       , 'a1 b2'],

        ['apple one towards bean 2', 'a1 b2'],
        ['apple 1 towards bean two', 'a1 b2']]

    for case in cases:
        assert extract(case[0]) == case[1]

def test_extract_error_number_short():
    cases = [
        'a1 to b0',
        'a0 to b1',

        'a1 to b9',
        'a9 to b1',

        'a1 to b99',
        'a99 to b1']

    for case in cases:
        with pytest.raises(ValueError):
            extract(case)

def test_extract_error_number_long():
    cases = [
        'apple 1 to bean 0',
        'apple 0 to bean 1',

        'apple 1 to bean 9',
        'apple 9 to bean 1',

        'apple 1 to bean 99',
        'apple 99 to bean 1',

        'apple -1 to bean 1',
        'apple 1 to bean -1']

    for case in cases:
        with pytest.raises(ValueError):
            extract(case)

def test_extract_error_letter_short():
    cases = [
        'i1 to a2',
        'a1 to i2',

        'z1 to a2',
        'a1 to z2']

    for case in cases:
        with pytest.raises(ValueError):
            extract(case)

def test_extract_error_letter_long():
    cases = [
        'i1 to a2',
        'a1 to i2',

        'z1 to a2',
        'a1 to z2']

    for case in cases:
        with pytest.raises(ValueError):
            extract(case)

def test_extract_error_missing():
    cases = [
        'a1 to',
        'to a2',

        'apple 1 to',
        'to apple 1']

    for case in cases:
        with pytest.raises(ValueError):
            extract(case)
