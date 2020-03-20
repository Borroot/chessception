import speech_recognition as sr
import re
import sys


def _record(recognizer):
    mic = sr.Microphone(sample_rate=44100, chunk_size=4096)
    with mic as source:
        return recognizer.listen(source)


def _save(audio):
    with open('audio.wav', 'wb') as file:
        wav = audio.get_wav_data()
        file.write(wav)


def _transcribe(recognizer, audio):
    try:
        # dic = recognizer.recognize_google(audio, language='en-GB', show_all=True)
        return recognizer.recognize_google(audio, language='en-GB')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.", file=sys.stderr)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e), file=sys.stderr)


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


def _pos(group1, group2):
    move = group1.lower()
    group2 = group2.lower().lstrip()
    if re.match(r'\d', group2):
        return move + group2
    else:
        return move + _atoi(group2)


def _extract(transcript):
    sep = r' (to|too|towards) '
    pos = r'\b([a-h])[a-z]*( ?[1-8]| [a-z]+)\b'

    regex_gutter = r'.*' + pos + sep + pos + r'.*'
    regex_exact = pos + r'( )' + pos

    match_gutter = re.match(regex_gutter, transcript, re.I)
    match_exact = re.match(regex_exact, transcript, re.I)
    match = match_gutter if match_gutter else match_exact

    if match:
        move = _pos(match.group(1), match.group(2))
        move = move + _pos(match.group(4), match.group(5))
        return move
    else:
        raise ValueError('No move can be extracted from the transcript.')


class Speech:
    """
    This class provides a way of inputting moves by speech.
    """

    def __init__(self):
        self._recognizer = sr.Recognizer()

    def move(self):
        audio = _record(self._recognizer)
        # _save(audio)
        transcript = _transcribe(self._recognizer, audio)
        return _extract(transcript)
