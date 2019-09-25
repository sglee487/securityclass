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
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def encrypt(mode, fileName, key):
    outputFileName = 'encrypt.txt'
    if mode[0] == 'd':
        key = -key
        outputFileName = 'decrypt.txt'
    translated = ''
    outputFile = ''

    inputFile = ''
    message = M

    for symbol in message:
        translated += shift(symbol, key)

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
