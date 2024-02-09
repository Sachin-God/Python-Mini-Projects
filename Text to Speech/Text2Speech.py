from gtts import gTTS
import os

f = open('hello.txt')
x = f.read()

# language = 'en'

audio = gTTS(text=x, lang='en',slow=False)
audio.save('hello.wav')
os.system('hello.wav')

f.close()