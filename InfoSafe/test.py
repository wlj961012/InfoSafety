from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(0).encode('utf-8')
unpad = lambda s : s[0:-ord(s[-1])]

class PrpCrypt(object):

    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
        self.data=self.read_date().replace('\n','')

    def read_date(self,path="/home/wlj/PycharmProjects/InfoSafe/date.txt"):
        with open(path) as f:
            data=f.read()
        return data

    def encrypt(self):
        self.data = self.data.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        self.data=pad(self.data)
        self.ciphertext = cryptor.encrypt(self.data)
        return b2a_hex(self.ciphertext)

    def decrypt(self,e):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(e))
        return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
    pc = PrpCrypt('keyskeyskeyskeys')
    e = pc.encrypt()
    d = pc.decrypt(e)
    print("加密:", e)
    print("解密:", d)