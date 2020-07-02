import speech_recognition as sr
import sys


class Speech:
    """
    This class provides a way of inputing moves by speech.
    """

    def move(self):
        recognizer = sr.Recognizer()
        audio = self._record(recognizer)
        # _save(audio)
        transcript = self._transcribe(recognizer, audio)
        print(transcript)
        return self.extract(transcript)

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
            return "None"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e), file=sys.stderr)
            return "No connection"

    @staticmethod
    def extract(transcript):
        raise NotImplementedError("Please implement this method.")
