MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Enter either "encrypt" or "e" or "decrypt" or "d".')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('The value you entered its invalid')

def getFileName():
    # print('Enter our file name:')
    print('Enter our string:')
    return input()

def getKey():
    print('Enter the key')
    key = input().lower()
    return key

def encrypt(mode, fileName, key):
    outputFileName = 'encrypt.txt'
    if mode[0] == 'd':
        # key = -key
        outputFileName = 'decrypt.txt'
    translated = ''
    outputFile = ''

    inputFile = ''
    message = M

    count = 0
    for symbol in message:
        keyvalue = ord(key[count])-97
        if mode[0] == 'd':
            keyvalue = -keyvalue
        translated += shift(symbol, keyvalue)
        count = count + 1
        if (count == key.__len__()):
            count = 0

    # outputFile.write(translated)
    # outputFile.close()
    # inputFile.close()
    print(translated)
    print("En(De)cryption complete")


def shift(symbol, key):
    if ord(symbol) >= ord('a') and ord(symbol) <= ord('z'):
        if ord(symbol) + key > ord('z'):
            return chr(ord(symbol) + key - 26)
        elif ord(symbol) + key < ord('a'):
            return chr(ord(symbol) + key + 26)
        else:
            return chr(ord(symbol) + key)
    elif ord(symbol) >= ord('A') and ord(symbol) <= ord('Z'):
        if ord(symbol) + key > ord('Z'):
            return chr(ord(symbol) + key - 26)
        elif ord(symbol) + key < ord('A'):
            return chr(ord(symbol) + key + 26)
        else:
            return chr(ord(symbol) + key)

mode = getMode()
key = getKey()
M = getFileName()
encrypt(mode, M, key)
