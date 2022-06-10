import wave

def getLSB(Frame):
    return int(bin(Frame).lstrip('0b').rjust(8,'0')[7])

song = wave.open("song_embedded.wav", mode='rb')
# Convert audio to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

for i in range(0,song.getnframes()):
    if getLSB(frame_bytes[i])==(frame_bytes[i]&1):
        print(True)
    else:
        print(getLSB(frame_bytes[i]),type(getLSB(frame_bytes[i])))
        print(frame_bytes[i]&1,type(frame_bytes[i]&1))
        print(False)