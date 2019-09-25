# print(chr((ord('a') ^ ord('b'))))
# print(chr((ord('a') ^ ord('b'))))

# print(chr(ord('a')))
# c = chr((ord('a') ^ ord('b')))
# print(c)
# d = chr((ord(c) ^ ord('b')))
# print(d)
#
# for a,b in zip('hello','world2'):
#     print(a)
#     print(b)

fileName = 'encrypt.txt'

inputFile = open(fileName, 'r')
message = inputFile.read()

print(message)

keyValue = ''
key = 'key'
for i in range(len(message) // 3):
    keyValue += key

result_array = []
for k, m in zip(keyValue, message):
    result_array.append(chr((ord(k) ^ ord(m))))
    print(result_array)
result_string = ''.join(result_array)
print(result_string)
result_toarray = list(result_string)
print(result_toarray)