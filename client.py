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

        # symmetric key
        # iv = client_socket.recv(1024).decode()
        # print('iv : ' + iv)
        # client_socket.send('iv exchange Success'.encode())

        keyRecive = True

        # symmetirc key
        # cipher_encrypt = setAES(key, iv)
        # cipher_decrypt = setAES(key, iv)

        # private/public key
        # key = "clientPriKey.pem"
        # pub_client_key = readPEM(key)

        # sign verify
        serverSignPubKey = readPEM("serverSignPubKey.pem")
        clientSignPriKey = readPEM("clientSignPriKey.pem")
        clientSignPriKey_for_sign = readPEM_for_signverify("clientSignPriKey.pem")
        serverSignPubKey_for_sign = readPEM_for_signverify("serverSignPubKey.pem")

    if(keyRecive):

        # symmetric key
        # message = input(" -> ")
        # while message.lower().strip() != 'bye':
        #     message = AES_Encrypt(cipher_encrypt,message)
        #     print(message)
        #     client_socket.send(message)
        #     data = client_socket.recv(1024)
        #     print(data)
        #     data = client_socket.recv(1024)
        #     data = AES_Decrypt(pub_client_key,data)
        #     print('Received from user1 : ' + data)
        #
        #     message = input(" -> ")

        while True:
            rdata = client_socket.recv(1024)
            # print(rdata)

            # private/public key
            # data = RSADecrypt(pub_client_key, rdata)
            # print('Received from user1 : ' + data)

            # sha256
            # hashBlock = RSADecrypt(pub_client_key,rdata)
            # data, hashData = separateHashBlock(hashBlock)
            # print("integrityCheck : " + str(integrityCheck(data,hashData)))
            # print(data)

            # sign verify
            data = RSADecrypt(clientSignPriKey, rdata)
            print('Received from user1 : ' + data)
            # print(data)

            signmessage = client_socket.recv(1024)
            # print(signmessage)

            verify(serverSignPubKey_for_sign,data.encode(),signmessage)

            if (data == "bye"):
                break

            rdata = input( '-> ')
            data = RSAEncrypt(serverSignPubKey, rdata)
            client_socket.send(data)

            hasher = SHA256.new(rdata.encode())
            signature = sign(clientSignPriKey_for_sign,hasher)
            client_socket.send(signature)

            if (rdata == "bye"):
                break

    client_socket.close()

if __name__== '__main__':
    client_program()
