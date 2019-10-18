from Crypto.PublicKey import RSA

# 공개키쌍 생성
#     -> 개인키를 먼저 생성한 후 개인키에서 공개키 추출

prikey = RSA.generate(1024)
pubkey = prikey.publickey()

priFile = open("./clientPriKey.pem","wb+")
priFile.write(prikey.exportKey('PEM'))
priFile.close()

pubFile = open("./clientPubKey.pem","wb+")
pubFile.write(pubkey.exportKey('PEM'))
pubFile.close()