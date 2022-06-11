from stegano import lsb
secret=lsb.hide(input('enter image name with ex: '),input('enter string: '))
secret.save('./out123.png')
print(lsb.reveal('./out123.png'))


