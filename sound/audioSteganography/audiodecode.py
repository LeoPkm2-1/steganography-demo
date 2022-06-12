import wave
import audioencode
# ENDSIGNAL : delimiter is the same with delimiter in audioencode
ENDSIGNAL = audioencode.ENDSIGNAL

# get lsb of one audio frame
def getLSB(Frame):
    return int(bin(Frame).lstrip('0b').rjust(8,'0')[7])

# list of LSB of all lsb in allframe
def getListLSB(AllFrame):
    listLSB=[]
    for i in range(len(AllFrame)):
        lsb=getLSB(AllFrame[i])
        listLSB.append(lsb)
    return listLSB

# get string from lsb bit list
def getTextFromLSBlist(LSBlst):
    hidenstring=''
    for i in range(0,len(LSBlst),8):
        bytegroup=LSBlst[i:i+8]
        bytestr="".join(str(b) for b in bytegroup)
        asciicode=int(bytestr,2)
        char=chr(asciicode)
        hidenstring=hidenstring+char
        if hidenstring[ (-1*len(ENDSIGNAL)):].__eq__(ENDSIGNAL):
            return hidenstring[:(-1*len(ENDSIGNAL))]
    return ''
# decode function
def decodeAudio(steganoFileName):
    song = wave.open(steganoFileName, mode='rb')
    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    # list of lsb in all frame
    LSBlist=getListLSB(frame_bytes)
    stringhiden=getTextFromLSBlist(LSBlist)
    return stringhiden