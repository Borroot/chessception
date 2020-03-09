import speech_recognition as sr
import re

def record(recognizer):
    mic = sr.Microphone(sample_rate=44100, chunk_size=4096)
    with mic as source:
        print("Say something!")
        audio = recognizer.listen(source)

def save(audio):
    with open('audio.wav', 'wb') as file:
        wav = audio.get_wav_data()
        file.write(wav)

def transcribe(recognizer, audio):
    try:
        # dic = recognizer.recognize_google(audio, language='en-GB', show_all=True)
        return recognizer.recognize_google(audio, language='en-GB')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def extract(transcript):
    # Seperators and positions.
    sep = r'too?(wards)?'
    pos = r'\b([a-h])[a-z]* ?([1-8])\b'

    regex = r'.*' + pos + r' ' + sep + r' ' + pos + r'.*'
    match = re.match(regex, transcript, re.I)

    if match:
        move = '{}{} {}{}'.format(match.group(1), match.group(2), match.group(4), match.group(5))
        return move.lower()
    else:
        raise ValueError('No move could be extracted from the transcript.')

def main():
    recognizer = sr.Recognizer()
    audio      = record(recognizer)
    # save(audio)
    transcript = transcribe(recognizer, audio)
    move       = extract(transcript)
