# We will use wave package available in native Python installation to read and write .wav audio file

import wave
#read wave audio file
song = wave.open('au.wav',mode='rb')
#read frames and convert to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# print(frame_bytes)
# for i in len(frame_bytes):
#     print(frame_bytes[i])
# for i in range(len(frame_bytes)):
#     print(i)
# for i in range(100,len(frame_bytes)//300):
#     print(frame_bytes[i])
temp= bin(frame_bytes[10000]).lstrip('0b').rjust(8,'0')
print(temp)
temp=temp[:7]+'0'+temp[8:]
# print(temp)
# # print(int(''.join(bin(temp))))
# print(frame_bytes[10000])
# print(type(frame_bytes[10000]))
print(temp,type(temp))
print(int(temp,2),type(int(temp,2)))
print(frame_bytes[10000],type(frame_bytes[10000]))
frame_bytes[10000]=30
print(frame_bytes[10000])
# print(temp)
# print(type(temp))
# temp[7]='0'
# print(temp)
# # the hiden string
# string = 'Leo is superman ahihi!'
# # Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
# string = string + int((len(frame_bytes)-(len(string)*8*8))/8)* '#'
# # Convert text to bit array
# bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

                        