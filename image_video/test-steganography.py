import cv2
import numpy as np
import types
# import cv2_imshow

#  function to convert any type of data into binary
def messageToBinary(message):
    if type(message)==str:
        return ''.join([format(ord(charI),'08b') for charI in message])
    elif type(message) == bytes or type(message)==np.ndarray:
        return [ format(i,"08b") for i in message ]
    elif type(message) == int or type(message) == np.uint8:
        return format(message,'08b')
    else:
        return TypeError('the input value is not supported!')
    
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
            break
        
    # print(decoded_data)
    return decoded_data[:-5] # remove the delimiter to show the original hidden message


        
#   Function that takes the input image name and secret message as input, calls hideData() to encode the message
def encode_text():
    image_name = input('enter the image name (with extension): ')
    image =cv2.imread(image_name) # read the input image using OpenCV-python.
    
    # details information of image
    print('the shape of the image is: ',image.shape) # check the shape of image 
    print('the original image is shown below: ')
    resized_image=cv2.resize(image,(500,500)) # resize image as per requirement
    # cv2_imshow(resized_image) # display image
    # cv2.waitKey()
    data = input('enter the string to be hiden: ....')
    if (len(data) == 0 ):
        raise ValueError('data is empty')

    filename = input('enter the name of new encoded image(with extension): ...')
    encoded_image = hideData(image,data) # call the hidedata function to hide the secret message into input image
    cv2.imwrite(filename,encoded_image)

# the function takes the steganography image name as input and call the showData() function to return text  which is hiden inside image input
def decode_text():
    # read the image the containts the hidden image
    image_name = input('enter the name of the steganographed image that you want to decode (with extension): ... ')
    image = cv2.imread(image_name) # read the image using cv2.imread()
    
    print("the steganographed image is as shown below: ")
    resized_image = cv2.resize(image,(500,500)) # resize the original image as per your requirement
    # cv2_imshow(resized_image) # display the steganographed image
    # cv2.waitKey()
    text = showData(image)
    return text

# this is the main() function
def Steganography():
    a = input('image steganography \n1. encode the data \n2.decode the data \n your input is: ....')
    userinput = int(a)
    if(userinput ==1):
        print('\nencoding.....')
        encode_text()
    elif(userinput ==2):
        print('\ndecoding....')
        print('\ndecoded message is '+ decode_text())
    else:
        raise Exception('enter the right input!')

Steganography()

    
    
    
    
    