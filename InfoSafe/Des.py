'''
from pyDes import *
import base64

data = "Please encrypt my data"
print(type(data))
key='BuctBuct'
k = des(key, ECB, "BuctBuct", pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)
d=base64.b64encode(d)
print(d)
d=base64.b64decode(d)
print(k.decrypt(d))
'''
from pyDes import *
import base64

class Des:

    def __init__(self):

        self.k=des('BuctBuct',ECB,'BuctBuct', pad=None, padmode=PAD_PKCS5)

    #从文件中读取我的数据
    def read_date(self,path="/home/wlj/PycharmProjects/InfoSafe/date.txt"):

        with open(path) as f:
            data=f.read()
        #print(data)
        return data


    def CBC_encode_data(self,key='BuctBcut',iv='BuctBuctBuctBuct'):
        data=self.read_date()
        key = 'BuctBuct'
        d = self.k.encrypt(data)
        data=str.encode(data)
        assert self.k.decrypt(d, padmode=PAD_PKCS5) == data
        d=base64.b64encode(d)
        self.write_data(d)
        return d

    def CBC_decode_data(self,data):
        data=base64.b64decode(data)
        d=self.k.decrypt(data)
        return d

    def ECB_encode_date(self,key="BuctBuct",iv="BuctBuct"):
        data=self.read_date()
        k=des(key,ECB,iv,pad=None,padmode=PAD_PKCS5)
        d=k.encrypt(data)
        assert k.decrypt(d,padmode=PAD_PKCS5) == data
        return base64.encode(d)

    def write_data(self,data,path="/home/wlj/PycharmProjects/InfoSafe/code.txt"):
        data = bytes.decode(data)
        with open(path,'a') as f:
            f.write(data)


if __name__ == '__main__':
    des=Des()
    cn=des.CBC_encode_data()
    print(cn)
    cd=des.CBC_decode_data(cn)
    print(cd)




