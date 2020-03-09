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
    # [A-Z][1-8]        [a-zA-Z]+ \w
    regex = r'.*\b([a-zA-Z])\w* ([1-8]) to(wards)? ([a-zA-Z])\w* ([1-8])'
    match = re.match(regex, transcript)

    if match:
        move = '{}{} {}{}'.format(match.group(1), match.group(2), match.group(4), match.group(5))
        move = move.lower()
        return move
    else:
        raise ValueError('No move could be extracted from the transcript.')

def main():
    recognizer = sr.Recognizer()
    audio      = record(recognizer)
    # save(audio)
    transcript = transcribe(recognizer, audio)
    move       = extract(transcript)
