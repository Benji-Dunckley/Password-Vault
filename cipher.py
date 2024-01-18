from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encryption(plaintext, key):
    plaintext = bytes(plaintext, 'UTF-8')
    cipher_e = AES.new(key, AES.MODE_EAX)
    return cipher_e.encrypt(plaintext), cipher_e.nonce

def decryption(ciphertext, nonce, key):
    cipher_d = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher_d.decrypt(ciphertext).decode('utf-8')