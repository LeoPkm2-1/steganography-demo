
# Use wave package (native to Python) for reading the received audio file
import wave
song = wave.open("song_embedded.wav", mode='rb')
# Convert audio to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))
t1=list(song.readframes(10))
t2=song.readframes(1)
t3=bytearray(list(song.readframes(10)))
# print(frame_bytes[10002],frame_bytes[10002]&1,type(frame_bytes[10002]))
# print(frame_bytes[10000],frame_bytes[10000]&1,type(frame_bytes[10000]))
# print(frame_bytes[100000],frame_bytes[100000]&1,type(frame_bytes[100000]))
# print(frame_bytes[100002],frame_bytes[100002]&1,type(frame_bytes[100002]))

a1=bin(frame_bytes[10002]).lstrip('0b').rjust(8,'0')
a2=bin(frame_bytes[10000]).lstrip('0b').rjust(8,'0')
a3=bin(frame_bytes[100000]).lstrip('0b').rjust(8,'0')
a4=bin(frame_bytes[100002]).lstrip('0b').rjust(8,'0')

print(frame_bytes[10002],type(frame_bytes[10002]&1) ,'\t ',a1,type(a1),'\t ',a1[7],type(a1[7]),'\t ',int(a1[7]),type(int(a1[7])))
print(frame_bytes[10000],type(frame_bytes[10000]&1) ,'\t ',a2,type(a2),'\t ',a2[7],type(a2[7]),'\t ',int(a2[7]),type(int(a2[7])))
print(frame_bytes[100000],type(frame_bytes[100000]&1) ,'\t ',a3,type(a3),'\t ',a3[7],type(a3[7]),'\t ',int(a3[7]),type(int(a3[7])))
print(frame_bytes[100002],type(frame_bytes[100002]&1) ,'\t ',a4,type(a4),'\t ',a4[7],type(a4[7]),'\t ',int(a4[7]),type(int(a4[7])))
# print(t3)
# print(type(list(t2)))
# print(frame_bytes)
# print(t1)

# # Extract the LSB of each byte
# extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
# # Convert byte array back to string
# string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
# # Cut off at the filler characters
# decoded = string.split("###")[0]

# # Print the extracted text
# print("Sucessfully decoded: "+decoded)
# song.close()