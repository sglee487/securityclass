from Crypto.Cipher import AES

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