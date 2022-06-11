from os import path
from pydub import AudioSegment

def isMp3(audioFileName):
    return audioFileName.lower().endswith('.mp3')

def isWav(audioFileName):
    return audioFileName.lower().endswith('.wav')


def convertMp3toWav(srcMp3,dstWav='au.wav'):
    sound = AudioSegment.from_mp3(srcMp3)
    sound.export(dstWav,format='wav');