# We will use wave package available in native Python installation to read and write .wav audio file
import wave
# read wave audio file
song = wave.open("au.wav", mode='rb')
# Read frames and convert to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# The "secret" text message
string='Peter Parker is the Spiderman!'
# Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
# Convert text to bit array
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

for i , bit in enumerate(bits):
    print('index: ',i,type(i))
    print('bit: ',bit,type(bit))