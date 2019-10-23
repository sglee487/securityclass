import hashlib

data = input('->')

hashdata = hashlib.sha256(data.encode()).hexdigest()

Mblock = '{0:04x}'.format(len(data)) + data + '{0:04x}'.format(len(hashdata)) + hashdata

print(Mblock)

data_size = int(Mblock[:4],16)
realData = Mblock[4 : data_size+4]

print(hashdata)
print(Mblock)
print(data_size)
print(realData)

