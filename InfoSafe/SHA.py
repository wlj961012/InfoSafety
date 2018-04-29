import hashlib

def read_data(path='/home/wlj/PycharmProjects/InfoSafe/date.txt'):
    with open(path) as f:
        data=f.read()
    return data.replace('\n','')

def write_data(data,path="/home/wlj/PycharmProjects/InfoSafe/code.txt"):
    with open(path, 'a') as f:
        f.write(data)

data=read_data()
dig1=hashlib.sha1(data.encode('UTF-8')).hexdigest()
write_data(dig1)
dig2=hashlib.sha256(data.encode('UTF-8')).hexdigest()
write_data(dig2)
dig3=hashlib.sha3_512(data.encode('UTF-8')).hexdigest()
write_data(dig3)