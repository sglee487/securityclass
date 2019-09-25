
from Crypto.Cipher import AES
import base64

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

def getMode():
    while True:
        print('Enter either "encrypt" or "e" or "decrypt" or "d".')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('The value you entered its invalid')

def getFileName():
    print('Enter our file name:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key')
        key = input()
        return key

def crypto(mode, fileName):
    KeyValue = ''
    iv = 'asefasdfefsdsdfe'
    key = 'thisisbadkeyokey'

    outputFileName = 'encrypt.txt'
    if mode[0] == 'd':
        outputFileName = 'decrypt.txt'

    translated = ''
    outputFile = open(outputFileName, 'w')

    inputFile = open(fileName, 'r')
    message = inputFile.read()
    # print(message)
    # print(message.encode("utf-8"))
    # print(pad(message))
    # print(unpad(pad(message)))
    # print(pad(message).encode("utf-8"))
    # # print(pad(message.encode("utf-8")))
    # print(unpad(message))
    # print(type(message))
    # print(type(unpad(message)))
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))

    if mode[0] == 'd':
        # print(cipher.decrypt(b'NB\xc5fh#\xd9\xeaxD\xb6u\x87\x89@\x1d\xbb\xe0\x1e\xda\xe8]|\xaez\xaeD\xf3$\xf6Z\x15'))
        # print(cipher.decrypt((b'NB\xc5fh#\xd9\xeaxD\xb6u\x87\x89@\x1d\xbb\xe0\x1e\xda\xe8]|\xaez\xaeD\xf3$\xf6Z\x15')).decode("utf-8"))
        # print(message)
        bytestring = message.encode('latin-1')
        # print(bytestring)
        # print(bytestring.decode('utf-8'))
        # bytestring = unpad(bytestring)
        translated = str(cipher.decrypt(bytestring).decode('utf-8'))
        translated = unpad(translated)
        print(translated)
        # print(translated)
        # translated = unpad(translated)
    else:
        # translated = cipher.encrypt(pad(message).encode("utf-8")))
        e_byte = cipher.encrypt(pad(message).encode("utf-8"))
        # print(e_byte)
        # print(e_byte.decode('latin-1'))
        print(e_byte)
        translated = e_byte.decode('latin-1')
        print(translated)
        # translated = str(e_byte)
        # print(e_byte.decode('latin-1').encode('latin-1'))
        # print(translated.decode('latin-1').encode('latin-1'))
        # str_to_byte = bytes(translated,"")
        # print(str_to_byte)
    # cipher.encrypt(pad(message))


    outputFile.write(translated)
    outputFile.close()
    inputFile.close()
    print("En(De)cryption complete")

# print(b'NB\xc5fh#\xd9\xeaxD\xb6u\x87\x89@\x1d\xbb\xe0\x1e\xda\xe8]|\xaez\xaeD\xf3$\xf6Z\x15'.decode('utf-8'))

mode = getMode()
fileName = getFileName()
crypto(mode, fileName)