from MCipher import *

import socket

def client_program():
    host = '127.0.0.1'
    port = 5462

    keyRecive = False
    client_socket = socket.socket()
    client_socket.connect((host,port))


    if(keyRecive == False):
        key = client_socket.recv(1024).decode()
        print('key : ' + key)
        client_socket.send('key exchange Success'.encode())
        iv = client_socket.recv(1024).decode()
        print('iv : ' + iv)
        client_socket.send('iv exchange Success'.encode())
        keyRecive = True
        cipher_encrypt = setAES(key, iv)
        cipher_decrypt = setAES(key, iv)

    if(keyRecive):
        message = input(" -> ")
        while message.lower().strip() != 'bye':
            message = AES_Encrypt(cipher_encrypt,message)
            print(message)
            client_socket.send(message)
            data = client_socket.recv(1024)
            print(data)
            data = AES_Decrypt(cipher_decrypt,data)
            print('Received from user1 : ' + data)

            message = input(" -> ")
    client_socket.close()

if __name__== '__main__':
    client_program()
