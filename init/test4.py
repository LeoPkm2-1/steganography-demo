import secrets
from stegano import lsb


file_name=input('enter name: ')
strhide=input('enter text: ')
secret=lsb.hide(file_name,strhide)
encode_file=input('enter the name of steganographed image')
secret.save(encode_file);
print(lsb.reveal(encode_file))