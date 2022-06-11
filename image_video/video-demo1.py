import cv2
import numpy as np
import types
from PIL import Image
import imghdr
# from stegano import lsb
from os.path import isfile,join

import time                                                                 #install time ,opencv,numpy modules
# import cv2
# import numpy as np
import math
import os
import shutil
from subprocess import call,STDOUT

#  function to convert any type of data into binary
def messageToBinary(message):
    if type(message)==str:
        return ''.join([format(ord(charI),'08b') for charI in message])
    elif type(message) == bytes or type(message)==np.ndarray:
        return [ format(i,"08b") for i in message ]
    elif type(message) == int or type(message) == np.uint8:
        return format(message,'08b')
    else:
        return TypeError('the input message is not valid!')
   
    
#  function to hide secret message into the image by altering the LSB
def hideData(image,secret_message):
    
    # get height and width of image
    h,w,_ = image.shape
    # maximum value to be encoded
    n_bytes = h*w*3//8
    print('the maximun bytes to be encoded: ', n_bytes)
    
    # check weather the size of secret string is suitable
    if len(secret_message)> n_bytes:
        raise ValueError('error string is to big to be hiden!')
    
    secret_message+='#####' # insert delimiter to string
    
    data_index=0
    
    # convert input data to binary format
    binary_secret_msg=messageToBinary(secret_message)
    
    data_len=len(binary_secret_msg) #find then length of data that needs to be hidden
    for values in image:
        for pixel in values:
            # convert RGB values into  binary format 
            r,g,b = messageToBinary(pixel)
            # modify LSB only if there is still data to store
            if data_index < data_len:
                # hide data into LSB of red value in pixel
                pixel[0] = int(r[:-1] + binary_secret_msg[data_index],2)
                data_index+=1
            if data_index < data_len:
                # hide data into LSB of green value in pixel
                pixel[1] = int( g[:-1] +binary_secret_msg[data_index],2)
                data_index+=1
            if data_index < data_len: 
                # hide data into LSB of blue value in pixel
                pixel[2] = int(b[:-1]+binary_secret_msg[data_index],2)
                data_index+=1
            
            if data_index>=data_len:
                break
    
    return image

# # function to decode the hidden message from the stego image
# def showData(image):
#     binary_data=''
#     for values in image:
#         for pixel in values:
#             # convert red, green, blue value of pixel into binary format
#             r,g,b = messageToBinary(pixel) 
            
#             # extracting data process
#             binary_data+=r[-1] # getting least significant bit of red value in pixel
#             binary_data+=g[-1] # getting least significant bit of green value in pixel
#             binary_data+=b[-1] # getting least significant bit of blue value in pixel
        
#     # slipt binary_string into  group of 8-bits
#     all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
#     # convert byte-group to characters
#     decoded_data=''
#     for byte in all_bytes:
#         decoded_data += chr(int(byte,2))
#         if decoded_data[-5:] == '#####' : # check if we reached delimiter which is '#####'
#             break
        
#     # print(decoded_data)
#     return decoded_data[:-5] # remove the delimiter to show the original hidden message

# function to decode the hidden message from the stego image
def showData(image):
    binary_data=''
    for values in image:
        for pixel in values:
            # convert red, green, blue value of pixel into binary format
            r,g,b = messageToBinary(pixel) 
            
            # extracting data process
            binary_data+=r[-1] # getting least significant bit of red value in pixel
            binary_data+=g[-1] # getting least significant bit of green value in pixel
            binary_data+=b[-1] # getting least significant bit of blue value in pixel
        
    # slipt binary_string into  group of 8-bits
    all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    # convert byte-group to characters
    decoded_data=''
    for byte in all_bytes:
        decoded_data += chr(int(byte,2))
        if decoded_data[-5:] == '#####' : # check if we reached delimiter which is '#####'
            # print(decoded_data)
            return decoded_data[:-5] # remove the delimiter to show the original hidden message            
            break
    
    return False
        


def encode_text(f_name,message,stegano_image_name='steganoOut'):
    # f_name = input('enter the image name (with extension): ')
    image =cv2.imread(f_name) # read the input image using OpenCV-python.
    
    # data = input('enter the string to be hiden: ....')
    data = message
    if (len(data) == 0 ):
        data = '#####'
    
    # filename = input('enter the name of new encoded image(WITHOUT extension): ...')
    filename = stegano_image_name
    filename+='.png'
    encoded_image=hideData(image,data)
    cv2.imwrite(filename,encoded_image)
    
def decode_text(image_name):
    # image_name = input('enter the name of the steganographed image type PNG that you want to decode (with extension): ... ')
    img=Image.open(image_name)
    if  img.format =='PNG':
        pass
    else:
        raise Exception('enter the right image type!');
    
    image = cv2.imread(image_name) # read the image using cv2.imread()
    text = showData(image)
    return text
    
# # this is the main() function
# def Steganography():
#     choice = input('image steganography \n1. encode the data \n2.decode the data \n your input is: ....')
#     userinput = int(choice)
#     if(userinput ==1):
#         print('\nencoding.....\n')
#         f_name=input('file name\n')
#         message=input("message to hiden")
#         encode_text(f_name,message)
#     elif(userinput ==2):
#         print('\ndecoding....')
#         img_name=input('enter steganography image')
#         print('\ndecoded message is:'+ decode_text(img_name)+'$')
#     else:
#         raise Exception('enter the right input!')

# Steganography()

def split_string(s_str,count=10):
    per_c=math.ceil(len(s_str)/count)
    c_cout=0
    out_str=''
    split_list=[]
    for s in s_str:
        out_str+=s
        c_cout+=1
        if c_cout == per_c:
            split_list.append(out_str)
            out_str=''
            c_cout=0
    if c_cout!=0:
        split_list.append(out_str)
    return split_list

def frame_extraction(video):
    if not os.path.exists("./tmp"):
        os.makedirs("tmp")
    temp_folder="./tmp"
    print("[INFO] tmp directory is created")

    vidcap = cv2.VideoCapture(video)
    count = 0

    while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        count += 1
        

def encode_string(input_string,root="./tmp/"):
    split_string_list=split_string(input_string)
    for i in range(0,len(split_string_list)):
        f_name="{}{}.png".format(root,i)
        # secret_enc=lsb.hide(f_name,split_string_list[i])
        secret_enc=encode_text(f_name,split_string_list[i],f_name)
        # secret_enc.save(f_name)
        print("[INFO] frame {} holds {}".format(f_name,split_string_list[i]))
        
        
def decode_string(video):
    frame_extraction(video)
    secret=[]
    root="./tmp/"
    for i in range(len(os.listdir(root))):
        f_name="{}{}.png".format(root,i)
        secret_dec=decode_text(f_name)
        print(secret_dec,type(secret_dec))
        if secret_dec == False:
            break
        secret.append(secret_dec)
        
    # clean_tmp()
    return ''.join([i for i in secret])
    
def clean_tmp(path="./tmp"):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("[INFO] tmp files are cleaned up")


def main():
    input_string = input("Enter the input string :")
    f_name=input("enter the name of video")
    frame_extraction(f_name)
    call(["ffmpeg", "-i",f_name, "-q:a", "0", "-map", "a", "tmp/audio.mp3", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    
    encode_string(input_string)
    call(["ffmpeg", "-i", "tmp/%d.png" , "-vcodec", "png", "tmp/video-leo.mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    
    call(["ffmpeg", "-i", "tmp/video-leo.mov", "-i", "tmp/audio.mp3", "-codec", "copy", "video-leo.mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    clean_tmp()
if __name__ == "__main__":
    while True:
        print("1.Hide a message in video 2.Reveal the secret from video")
        print("any other value to exit")
        choice = input()
        if choice == '1':
            main()
        elif choice == '2':
            print(decode_string(input("enter the name of video with extension")))
        else:
            break