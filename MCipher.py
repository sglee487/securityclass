from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import hashlib

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
    encrypted = pubKey.encrypt(data.encode())
    return encrypted

#복호화
def RSADecrypt(priKey, data):
    decrypted = priKey.decrypt(data).decode()
    return decrypted

#해시
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

#해시블록 생성
def makeHashBlock(data):
    hashdata = hashlib.sha256(data.encode()).hexdigest()
    hashBlock = '{0:04x}'.format(len(data)) + data + '{0:04x}'.format(len(hashdata)) + hashdata
    return hashBlock

#해시블록 분리
def separateHashBlock(hashBlock):
    data_size = int(hashBlock[:4], 16)
    data = hashBlock[4: data_size + 4]
    hashData_size = int(hashBlock[data_size+4:data_size+8],16)
    hashData = hashBlock[data_size+8:data_size+8+hashData_size]
    return data,hashData

#무결성 검사
def integrityCheck(data, hashData):
    return (hashlib.sha256(data.encode()).hexdigest()) == hashData