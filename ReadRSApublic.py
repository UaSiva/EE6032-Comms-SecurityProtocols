'''
Created on 3 Mar 2018

@author: Kevin
'''
from Crypto.PublicKey import RSA

secret_code = "Unguessable"
encoded_key = open("rsa_key.bin", "rb").read()
key = RSA.import_key(encoded_key, passphrase=secret_code)

print(key.publickey().exportKey())