import numpy as np
import random

class classic_code:

    def __init__(self,path):
        self.data=self.read_data(path).replace('\n','')
        self.data=self.data.lower()
        self.TransRect=[x for x in range(len(self.data))]
        random.shuffle(self.TransRect)#生成随机置换矩阵

    def read_data(self,path):
        with open(path) as f:
            data=f.read()
        return data

    def vigenere_encrypt(self,key):
        dl=len(self.data)
        kl=len(key)
        m=dl//kl
        n=dl%kl
        out=""
        key=key*m+key[:n]
        for i in range(dl):
            out+=chr((ord(self.data[i])+ord(key[i])-2*ord('a'))%26+ord('a'))
        self.data=out

    def vigenere_decrypt(self,key):
        dl = len(self.data)
        kl = len(key)
        m = dl // kl
        n = dl % kl
        out = ""
        key = key * m + key[:n]
        for i in range(dl):
            out += chr((ord(self.data[i]) - ord(key[i])) % 26 + ord('a'))
        self.data = out

    def gcd(self,a, b):
        while a != 0:
            a, b = b % a, a
        return b

    def findModReverse(self,a, m):
        if self.gcd(a, m) != 1:
            return None
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m
        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % m

    def affine_encrypt(self,a,b):
        out=""
        dl=len(self.data)
        for i in range(dl):
            out+=chr((a*(ord(self.data[i])-ord('a'))+b)%26+ord('a'))
        self.data=out

    def affine_decrypt(self,a,b):
        a=self.findModReverse(a,26)
        out = ""
        dl = len(self.data)
        print(self.data)
        for i in range(dl):
            out += chr((a * (ord(self.data[i]) - ord('a')-b)) % 26 + ord('a'))
        self.data=out

    def rotate_encrypt(self):
        out=""
        for i in self.TransRect:
            out+=self.data[i]
        self.data=out

    def rotate_decrypt(self):
        out=""
        for i in range(len(self.data)):
            for j,k in enumerate(self.TransRect):
                if(i==k):
                    out+=self.data[j]
        self.data=out

    def hill_encrypt(self,key):
        dl=len(self.data)
        kl=key.shape[1]
        if dl%kl!=0:
            for i in range(kl-(dl%kl)):
                self.data+='a'
        dl=len(self.data)
        m=dl//kl
        out=""
        for i in range(m):
            temp=self.data[kl*i:kl*(i+1)]
            l=[]
            for j in range(kl):
                l.append(ord(temp[j])-ord('a'))
            l=(np.dot(np.array(l),key))%26
            for k in l:
                out+=chr(k+ord('a'))
        self.data=out

    def hill_decrypt(self,key):
        key=np.linalg.inv(key)*np.linalg.det(key)
        key=key.astype(int)
        a=self.findModReverse(int(np.linalg.det(key)),26)
        kl=len(key)
        dl = len(self.data)
        m = dl // kl
        out = ""
        for i in range(m):
            temp = self.data[kl * i:kl * (i + 1)]
            l = []
            for j in range(kl):
                l.append(ord(temp[j]) - ord('a'))
            l = (a*(np.dot(np.array(l), key))) % 26
            for k in l:
                out += chr(k + ord('a'))
        self.data = out


if __name__ == '__main__':
    c=classic_code('/home/wlj/PycharmProjects/InfoSafe/date.txt')
    #c.vigenere_encrypt('buct')
    #c.vigenere_decrypt('buct')
    #c.affine_encrypt(1,2)
    #c.affine_decrypt(1,2)
    #c.rotate_encrypt()
    #c.rotate_decrypt()
    key=np.array([[3,6],[2,7]])
    c.hill_encrypt(key)
    c.hill_decrypt(key)