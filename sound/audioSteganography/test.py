import audioencode
import audiodecode

while True:
    choice = input('1. encode audio.\n2. decode audio\nAny key else to exit\nEnter your choice: ')
    if choice.__eq__('1'):
        # input data
        inputfilename=input('enter the audio file to carry text: ')
        hidenText=input('enter the hiden text: ')
        outputSteganoName=input("enter the steganography audio file name: ")
        # encode process
        audioencode.encodeAudio(inputfilename,hidenText,outputSteganoName)
    elif choice.__eq__('2'):
        # input data
        inputSteganoFileName = input("enter the steganography audio file name to decode: ")
        print('text hiden is:-'+audiodecode.decodeAudio(inputSteganoFileName)+'-')
    else:
        break
        
    
