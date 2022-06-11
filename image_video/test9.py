
from stegano import lsb
secret=lsb.hide('./b.png','hello world')
secret.save('./encoded_image.png')
lsb.reveal('./encoded_image.png')