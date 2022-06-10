# We will use wave package available in native Python installation to read and write .wav audio file
import wave

ENDSIGNAL=10 *'#'

# read wave audio file
filename=input('enter the file audio .wav: ')
song = wave.open(filename, mode='rb')
# Read frames and convert to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))
# The "secret" text message
# # # string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
string='Leo is a supermancoding!'
# Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
string=string+ENDSIGNAL
# Convert text to bit array
liststrbit=''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])
bits=list(map(int,liststrbit))

# Replace LSB of each byte of the audio data by one bit from the text bit array
for i in range(0,len(bits)):
    frame_bytes[i]= (frame_bytes[i] & 254) | bits[i]
# Get the modified bytes
frame_modified = bytes(frame_bytes)

steganoSong=wave.open('song_embedded.wav', 'wb')
steganoSong.setparams(song.getparams())
steganoSong.writeframes(frame_modified)
steganoSong.close()
song.close()