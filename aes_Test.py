
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
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))

    if mode[0] == 'd':
        e_byte = eval(message)
        translated = str(cipher.decrypt(e_byte).decode('utf-8'))
        translated = unpad(translated)
        print(translated)
    else:
        e_byte = cipher.encrypt((pad(message)).encode("utf-8"))
        print(e_byte)
        translated = str(e_byte)
        print(translated)

    outputFile.write(translated)
    outputFile.close()
    inputFile.close()
    print("En(De)cryption complete")


mode = getMode()
fileName = getFileName()
crypto(mode, fileName)