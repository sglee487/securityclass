from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

message = 'abcdefghijklmnop is user1 message'.encode()

#read priKey and init RSA
pri_file = open('user1_Private.pem','r')
key = RSA.importKey(pri_file.read())

#sign to message
hasher = SHA256.new(message)
signer = PKCS1_v1_5.new(key)
signature = signer.sign(hasher)
print(signature)


#read pubKey and init RSA
pub_file = open('user1_Public.pem','rb')
key = RSA.importKey(pub_file.read())

#verify the sign
verifier = PKCS1_v1_5.new(key)
if verifier.verify(hasher, signature):
    print('it is user1 message')
else:
    print('no!')