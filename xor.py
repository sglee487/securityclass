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
    print('Enter our file name:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key')
        key = input()
        return key

def encrypt(mode, fileName, key):
    keyValue = ''

    outputFileName = 'encrypt.txt'
    if mode[0] == 'd':
        outputFileName = 'decrypt.txt'

    translated = ''
    outputFile = open(outputFileName, 'w')

    inputFile = open(fileName, 'r')
    message = inputFile.read()

    len(message)
    for i in range(len(message)//3):
        keyValue += key

    print(keyValue)
    translated = str_xor(keyValue, message)
    print(translated)
    outputFile.write(translated)
    outputFile.close()
    inputFile.close()
    print("En(De)cryption complete")


def str_xor(keyValue, message):
    # print (keyValue ^ message)
    result_array = []
    for k,m in zip(keyValue,message):
        result_array.append(chr((ord(k) ^ ord(m))))
        print(result_array)
    result_string = ''.join(result_array)
    print(result_string)
    result_toarray = list(result_string)
    print(result_toarray)
    result_array2 = []
    for k,m in zip(keyValue,result_string):
        result_array2.append(chr((ord(k) ^ ord(m))))
        print(result_array2)
    return result_string

mode = getMode()
key = getKey()
fileName = getFileName()
encrypt(mode, fileName, key)
