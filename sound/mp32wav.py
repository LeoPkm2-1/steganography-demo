from os import path
from pydub import AudioSegment

def convert(srcMp3,dstWav='au.wav'):
    sound = AudioSegment.from_mp3(srcMp3)
    sound.export(dstWav,format='wav');

def main():
    srcfile=input("enter the MP3 file song: ")
    convert(srcfile)
main()