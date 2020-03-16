import speech_recognition as sr
import re
import sys

class Speech():
    """
    This class provides a way of inputing moves by speech.
    """

    def move(self):
        recognizer = sr.Recognizer()
        audio      = self._record(recognizer)
        # _save(audio)
        transcript = self._transcribe(recognizer, audio)
        move       = self._extract(transcript) # TODO handle error
        return move

    def _record(self, recognizer):
        mic = sr.Microphone(sample_rate=44100, chunk_size=4096)
        with mic as source:
            return recognizer.listen(source)

    def _save(self, audio):
        with open('audio.wav', 'wb') as file:
            wav = audio.get_wav_data()
            file.write(wav)

    def _transcribe(self, recognizer, audio):
        try:
            # dic = recognizer.recognize_google(audio, language='en-GB', show_all=True)
            return recognizer.recognize_google(audio, language='en-GB')
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.", file=sys.stderr)
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e), file=sys.stderr)

    def _atoi(self, alpha):
        similar = [
            ['one', 'won'],
            ['two', 'too', 'to'],
            ['three', 'tree'],
            ['four', 'for', 'fore'],
            ['five', 'hive'],
            ['six', 'sics'],
            ['seven'],
            ['eight', 'ait', 'ate']]

        for index, synonyms in enumerate(similar):
            for synonym in synonyms:
                if alpha == synonym:
                    return str(index + 1)

        raise ValueError('No move can be extracted from the transcript.')

    def _pos(self, group1, group2):
        move = group1.lower()
        if re.match(r'\d', group2):
            return move + group2
        else:
            return move + self._atoi(group2.lstrip())

    def _extract(self, transcript):
        sep = r'too?(wards)?'
        pos = r'\b([a-h])[a-z]* ?([1-8]| [a-z]+)\b'

        regex = r'.*' + pos + r' ' + sep + r' ' + pos + r'.*'
        match = re.match(regex, transcript, re.I)

        if match:
            move =        self._pos(match.group(1), match.group(2))
            move = move + self._pos(match.group(4), match.group(5))
            return move
        else:
            raise ValueError('No move can be extracted from the transcript.')
