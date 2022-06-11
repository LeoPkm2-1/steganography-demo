from stegano import lsb
from os.path import isfile,join

import time                                                                 #install time ,opencv,numpy modules
import cv2
import numpy as np
import math
import os
import shutil
from subprocess import call,STDOUT

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
        secret_enc=lsb.hide(f_name,split_string_list[i])
        secret_enc.save(f_name)
        print("[INFO] frame {} holds {}".format(f_name,split_string_list[i]))
def decode_string(video_name):
    # frame_extraction('outV'+video_name)
    frame_extraction(video_name)
    secret=[]
    root="./tmp/"
    for i in range(len(os.listdir(root))):
        f_name="{}{}.png".format(root,i)
        secret_dec=lsb.reveal(f_name)
        if secret_dec == None:
            print("break: ",f_name)
            break
        secret.append(secret_dec)
        
    print(''.join([i for i in secret]))
    clean_tmp()
    
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
    call(["ffmpeg",'-framerate','30' ,"-i", "tmp/%d.png" , "-vcodec", "png", "tmp/outV.mp4", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    # call(["ffmpeg",'-framerate','30' ,"-i", "tmp/%d.png" , "-vcodec", "png", "outV.gif", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    
    call(["ffmpeg", "-i", "tmp/outV.mp4", "-i", "tmp/audio.mp3", "-codec", "copy", "outV.mp4", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    
       
    
    # print("-----------------888-----------------")
    # call(["ffmpeg", "-i", "outV.mp4", "-b", "10000k", "outV-x264.mp4", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    # call(['ffmpeg', "-c:v", "libx264",'-i', 'outV-x264.mp4',"-c:v", "png",'outRaw.mp4','-y'],stdout=open(os.devnull, "w"), stderr=STDOUT)
    clean_tmp()
if __name__ == "__main__":
    while True:
        print("1.Hide a message in video 2.Reveal the secret from video")
        print("any other value to exit")
        choice = input()
        if choice == '1':
            main()
        elif choice == '2':
            video_name=input("enter the name of video with extension")
            # call(['ffmpeg','-i',video_name,'-vcodec','png','outV-'+video_name],stdout=open(os.devnull, "w"), stderr=STDOUT)
            decode_string(video_name)
        else:
            break