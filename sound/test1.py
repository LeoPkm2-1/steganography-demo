import wave

# read wave audio file
# au_name=input('enter the file in .wav format: ')
song = wave.open("au.wav")
numberOfframe=song.getnframes()
audio_frames=song.readframes(numberOfframe)
frameslist=list(audio_frames)
frame_bytes=bytearray(100000)
# print(len(frame_bytes))
string='a'
print(len(string))
print(int((len(frame_bytes)-(len(string)*8*8))/8))
# print(frame_bytes)
# print('\n')
# print(frame_bytes[1])
# for b in frame_bytes:
#     print(b)

# import wave

# # reading wave audio file
# filename=input('enter the song .wav name file')
# song = wave.open(filename,mode='rb')
# print(song.getnframes())
# print(song.readframes(2))