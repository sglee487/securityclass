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

def encrypt(mode, fileName):
    # keyValue = ''

    outputFileName = 'encrypt.txt'
    if mode[0] == 'd':
        outputFileName = 'decrypt.txt'

    translated = ''
    outputFile = open(outputFileName, 'w')

    inputFile = open(fileName, 'r')
    message = inputFile.read()

    for first_letter_key_number in range(97,123):
        first_letter_key = chr(first_letter_key_number)
        for second_letter_key_number in range(97,123):
            second_letter_key = chr(second_letter_key_number)
            for third_letter_key_number in range(97, 123):
                third_letter_key = chr(third_letter_key_number)

                key = first_letter_key+second_letter_key+third_letter_key
                print('key : ' + key)
                keyValue=''
                for i in range(len(message)//3):
                    keyValue += key

                print(keyValue)
                translated = str_xor(keyValue, message)
                print(translated)
                outputFile.write(translated)
                outputFile.write('\n')
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
    return result_string

mode = getMode()

fileName = getFileName()
encrypt(mode, fileName)
