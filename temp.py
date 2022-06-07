import imghdr
from logging import exception
from tkinter import EXCEPTION
from PIL import Image

def check_file_imgae():
    image_name=input('enter the file name:')
    img=Image.open(image_name)
    if img.format.lower() in ['png','jpeg']:
        print(True)
    else:
        raise Exception('file type wrong')

check_file_imgae();


# import imghdr
# import cv2
# import numpy as np
# import types
# from PIL import Image
# # import os



# def change_type_file():
#     image_name = input('enter the file name: ')
#     image =cv2.imread(image_name)
#     print(imghdr.what(image_name))
#     img=Image.open(image_name)
#     print(img.format)
#     if img.format =='PNG':
#         print(True)
#     else:
#         print(False)
        

# change_type_file()