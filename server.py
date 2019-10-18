from MCipher import *

import socket

def server_program():
    host = '127.0.0.1'
    port = 5462

    # symmetric key
    # key = 'thisisbadkeyokeythisisbadkeyokey'
    # iv = 'ivisinitialvetor'

    # private/public key
    key = "clientPubKey.pem"

    # symmetric key
    # cipher_encrypt = setAES(key,iv)
    # cipher_decrypt = setAES(key, iv)

    # private/public key
    pub_client_key = readPEM(key)

    server_socket = socket.socket()
    server_socket.bind((host,port))

    # symmetric key
    # server_socket.listen(2)
    # conn, address = server_socket.accept()
    # conn.send(key.encode())
    # print(conn.recv(1024).decode())
    # conn.send(iv.encode())
    # print(conn.recv(1024).decode())

    # private/pubilc key
    server_socket.listen(2)
    conn, address = server_socket.accept()
    conn.send(key.encode())
    print(conn.recv(1024).decode())
    # conn.send(iv.encode())
    # print(conn.recv(1024).decode())

    print("Connection from: " + str(address))

    while True:
        # symmetric key
        # rdata = conn.recv(1024)
        # if not rdata:
        #     break
        # print(rdata)
        # data = AES_Decrypt(cipher_decrypt,rdata)
        # print("Recieved from user2 : " + str(data))

        rdata = input(' -> ')

        # symmetric key
        # data = AES_Encrypt(cipher_encrypt,rdata)

        data = AES_Encrypt(pub_client_key, rdata)
        print(data)
        conn.send(data)
        if (rdata == "bye"):
            break

    conn.close()

if __name__ == '__main__':
    server_program()