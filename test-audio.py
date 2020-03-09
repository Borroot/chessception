import speech_recognition as sr
import re

rec = sr.Recognizer()
mic = sr.Microphone(device_index=2, sample_rate=44100, chunk_size=4096)

# Record the spoken words.
with mic as source:
    print("Say something!")
    audio = rec.listen(source)

# Save the recording in a file.
# with open('audio.wav', 'wb') as file:
    # wav = audio.get_wav_data()
    # file.write(wav)

# Query the google api for speech recognition.
try:
    dic = rec.recognize_google(audio, language='en-GB', show_all=True)
    # dic = {'alternative': [{'transcript': 'hello world apple 4 towards baby 7 right', 'confidence': 0.95467669}, {'transcript': 'hello world this is a new text'}, {'transcript': 'helloworld this is a new test'}, {'transcript': 'helloworld this is a new text'}], 'final': True}

    # [A-Z][1-8]
    # [a-zA-Z]+ \w
    print(dic)
    transcript = dic['alternative'][0]['transcript']
    print(transcript)

    regex = r'.*\b([a-zA-Z])\w* ([1-8]) to(wards)? ([a-zA-Z])\w* ([1-8])'
    match = re.match(regex, transcript)
    if match:
        print('{}{} {}{}'.format(match.group(1), match.group(2), match.group(4), match.group(5)))
    else:
        print('No match.')

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
