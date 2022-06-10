# We will use wave package available in native Python installation to read and write .wav audio file
import wave



# # # # ========================== function test ==================
def getfisrt0(frame_bytes):
    res=0
    for i in range(0,len(frame_bytes)):
        if frame_bytes[i]==0:
            res+=1
        else:
            break
    return res
def sum0(frame_bytes):
    res=0
    for i in range(0,len(frame_bytes)):
        if frame_bytes[i]==0:
            res+=1
    return res
def sumnot0(frame_bytes):
    res=0
    for i in range(0,len(frame_bytes)):
        if frame_bytes[i]!=0:
            res+=1
    return res
# # # # ========================== function test end ==============

ENDSIGNAL=10 *'#'

# read wave audio file
filename=input('enter the file audio .wav: ')
song = wave.open(filename, mode='rb')
# Read frames and convert to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))



# test =======================================
print('first 0: ',getfisrt0(frame_bytes))
print('sum 0: ',sum0(frame_bytes))
print('not 0: ',sumnot0(frame_bytes))
print('length:',len(frame_bytes))
# end test ====================================




# The "secret" text message
# # # string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
fl=open('text.txt','r')

# string='Leo is a supermancoding!'

string=fl.read()
# print('leuleu: ',string)
# Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.

# string=string+ENDSIGNAL
string =string +'###'
# string = string + int((len(frame_bytes)-(len(string)*8*8))/(8*1)) *'#'


# Convert text to bit array
liststrbit=''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])
bits=list(map(int,liststrbit))

# Replace LSB of each byte of the audio data by one bit from the text bit array
for i in range(0,len(bits)):
    frame_bytes[i]= (frame_bytes[i] & 254) | bits[i]
# Get the modified bytes
frame_modified = bytes(frame_bytes)

steganoSong=wave.open(filename+'embedded.wav', 'wb')
steganoSong.setparams(song.getparams())
steganoSong.writeframes(frame_modified)
steganoSong.close()
song.close()