#base 64

import base64
from binascii import unhexlify


hex = unhexlify('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')
flag = base64.b64encode(hex) #This is to encode the strings to base 64
print(flag)
