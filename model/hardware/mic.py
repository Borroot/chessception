import speech_recognition as sr
import re
import sys

def record(recognizer):
    # mic = sr.Microphone(sample_rate=44100, chunk_size=4096)
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
        print("Google Speech Recognition could not understand the audio.", file=sys.stderr)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e), file=sys.stderr)

def atoi(alpha):
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
                return index + 1

    raise ValueError('No move can be extracted from the transcript.')

def add_pos(move, group1, group2):
    move.append(group1.lower())
    if re.match(r'\d', group2):
        move.append(group2)
    else:
        move.append(atoi(group2.lstrip()))

def extract(transcript):
    # Seperators and positions.
    sep = r'too?(wards)?'
    pos = r'\b([a-h])[a-z]* ?([1-8]| [a-z]+)\b'

    regex = r'.*' + pos + r' ' + sep + r' ' + pos + r'.*'
    match = re.match(regex, transcript, re.I)

    if match:
        move = [] # e.g. ['a', 1, 'b', 2]
        add_pos(move, match.group(1), match.group(2))
        add_pos(move, match.group(4), match.group(5))

        move = '{}{}{}{}'.format(move[0], move[1], move[2], move[3])
        return move
    else:
        raise ValueError('No move can be extracted from the transcript.')

def main():
    recognizer = sr.Recognizer()
    audio      = record(recognizer)
    # save(audio)
    transcript = transcribe(recognizer, audio)
    move       = extract(transcript) # TODO handle error
    # validate(move)

if __name__ == "__main__":
    main()
