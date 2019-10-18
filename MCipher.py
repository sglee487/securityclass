from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

def setAES(key, iv):
    #TODO SET AES
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    return cipher

def AES_Encrypt(cipher, data):
    #TODO DATA ENCRYPT
    message = cipher.encrypt((pad(data)).encode())
    return message

def AES_Decrypt(cipher, data):
    #TODO DATA DECRYPT
    message = str(cipher.decrypt(data).decode('utf-8'))
    message = unpad(message)
    return message

#키 읽기
def readPEM(filename):
    f = open(filename, "r")
    key = RSA.importKey(f.read())
    f.close()
    pkcs1_oaep = PKCS1_OAEP.new(key)
    return pkcs1_oaep

#암호화
def RSAEncrypt(pubKey, data):
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(data.encode())
    return encrypted

#복호화
def RSADecrypt(priKey, data):
    decryptor = PKCS1_OAEP.new(priKey)
    decrypted = decryptor.decrypt(data).decode()
    return decrypted