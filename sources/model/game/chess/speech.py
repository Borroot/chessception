import model.hardware.speech
import re


class Speech(model.hardware.speech.Speech):

    @staticmethod
    def _atoi(alpha):
        similar = [
            ['one', 'i', 'won'],
            ['two', 'ii', 'too', 'to'],
            ['three', 'iii', 'tree'],
            ['four', 'iv', 'for', 'fore'],
            ['five', 'v', 'hive'],
            ['six', 'vi', 'sics'],
            ['seven', 'vii'],
            ['eight', 'viii', 'ait', 'ate']]

        for index, synonyms in enumerate(similar):
            for synonym in synonyms:
                if alpha == synonym:
                    return str(index + 1)

        raise ValueError('No move can be extracted from the transcript.')

    @staticmethod
    def _pos(group1, group2):
        move = group1.lower()
        group2 = group2.lower().lstrip()
        if re.match(r'\d', group2):
            return move + group2
        else:
            return move + Speech._atoi(group2)

    @staticmethod
    def extract(transcript):
        sep = r' (to|too|towards) '
        pos = r'\b([a-h])[a-z]*( ?[1-8]| [a-z]+)\b'

        regex_gutter = r'.*' + pos + sep + pos + r'.*'
        regex_exact = pos + r'( )' + pos

        match_gutter = re.match(regex_gutter, transcript, re.I)
        match_exact = re.match(regex_exact, transcript, re.I)
        match = match_gutter if match_gutter else match_exact

        if match:
            move = Speech._pos(match.group(1), match.group(2))
            move = move + Speech._pos(match.group(4), match.group(5))
            return move
        else:
            raise ValueError('No move can be extracted from the transcript.')
