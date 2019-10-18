from MCipher import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


f = open("clientPriKey.pem","r")
prikey = RSA.importKey(f.read())
f.close()
f = open("clientPubKey.pem","r")
pubkey = RSA.importKey(f.read())
f.close()

print(prikey)
print(pubkey)

test = "Hello"

# print(pubkey.can_encrypt())
# encrypt = pubkey.encrypt(test.encode(),32)
# print(encrypt)

encryptor_for_server = PKCS1_OAEP.new(pubkey)
encrypted = encryptor_for_server.encrypt(test.encode())

print(encrypted)
decryptor_for_client = PKCS1_OAEP.new(prikey)
decrypted = decryptor_for_client.decrypt(encrypted).decode()
print(decrypted)

# encrypt = pubkey.PKCS1_OAEP(test,32)
# print(encrypt)
#
# decrypt = prikey.decrypt(encrypt)
# print(decrypt)