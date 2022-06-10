import wave
ENDSIGNAL='###'
def getLSB(Frame):
    return int(bin(Frame).lstrip('0b').rjust(8,'0')[7])

def getListLSB(AllFrame):
    listLSB=[]
    for i in range(len(AllFrame)):
        lsb=getLSB(AllFrame[i])
        listLSB.append(lsb)
    return listLSB

def getTextFromLSBlist(LSBlst):
    hidenstring=''
    for i in range(0,len(LSBlst),8):
        bytegroup=LSBlst[i:i+8]
        bytestr="".join(str(b) for b in bytegroup)
        asciicode=int(bytestr,2)
        char=chr(asciicode)
        hidenstring=hidenstring+char
        if hidenstring[-10:].__eq__(ENDSIGNAL):
            return hidenstring[:-10]
    return ''
        
def decodeAudio():
    
    song = wave.open("song_embedded.wav", mode='rb')
    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    # list of lsb in all frame
    LSBlist=getListLSB(frame_bytes)
    stringhiden=getTextFromLSBlist(LSBlist)
    print("Sucessfully decoded: ",stringhiden)

decodeAudio()




















































































































































































    # for i in range(0,song.getnframes()):
    #     if getLSB(frame_bytes[i])==(frame_bytes[i]&1):
    #         print(True)
    #     else:
    #         print(getLSB(frame_bytes[i]),type(getLSB(frame_bytes[i])))
    #         print(frame_bytes[i]&1,type(frame_bytes[i]&1))
    #         print(False)