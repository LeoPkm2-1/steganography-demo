import wave

# reading wave audio file
filename=input('enter the song .wav name file')
song = wave.open(filename,mode='rb')
print(song.getnframes())