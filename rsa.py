from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import time


keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()

#print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
#print(pubKeyPEM.decode('ascii'))

#print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
#print(privKeyPEM.decode('ascii'))

filename = "rsafile.txt"
readmsg = open(filename, "rb")
msg = readmsg.read()
readmsg.close()
start = time.time() 

# msg = b'Network Information Security'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))
# print(type(encrypted))
end = time.time()
print(end - start)

filename = "rsaencrypt1.txt"
readmsg = open(filename, "wb")
msg = readmsg.write(encrypted)
readmsg.close()

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)

filename = "rsadecrypt1.txt"
readmsg = open(filename, "wb")
msg = readmsg.write(decrypted)
readmsg.close()
