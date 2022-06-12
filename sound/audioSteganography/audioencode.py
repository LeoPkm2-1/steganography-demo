import mp3towav
import wave
import os

NUMOFSIGNAL=10
ENDSIGNAL=NUMOFSIGNAL *'#'


def encodeAudio(audioFileName,hidenString='',audioSteganoFileName='song_embedded.wav'):
    # check stegano output file
    if len(audioSteganoFileName)<1:
        audioSteganoFileName='song_embedded.wav'
    # change mp3 to wav
    if mp3towav.isMp3(audioFileName):
        file_path = audioFileName
        file_name = os.path.basename(file_path)
        file_name=os.path.splitext(file_name)[0]
        mp3towav.convertMp3toWav(audioFileName,file_name+'.wav')
        # reload file name
        audioFileName=file_name+'.wav'
        
    # read wave audio file
    song = wave.open(audioFileName, mode='rb')
    # Read frames and convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    # adding delimiter of signal to the string and decode must to remove it
    hidenString =hidenString + ENDSIGNAL
    # Convert text to bit array    
    liststrbit=''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in hidenString])
    bits=list(map(int,liststrbit))
    # Replace LSB of each byte of the audio data
    for i in range(0,len(bits)):
        frame_bytes[i] = (frame_bytes[i] & 254) | bits[i]
    # Get the modified bytes
    frame_modified = bytes(frame_bytes)
    steganoSong=wave.open(audioSteganoFileName, 'wb')
    steganoSong.setparams(song.getparams())
    steganoSong.writeframes(frame_modified)
    steganoSong.close()
    song.close()