import hashlib

def read_data(path='/home/wlj/PycharmProjects/InfoSafe/date.txt'):
    with open(path) as f:
        data=f.read()
    return data.replace('\n','')

def write_data(data,path="/home/wlj/PycharmProjects/InfoSafe/code.txt"):
    with open(path, 'a') as f:
        f.write(data)

data=read_data()
dig=hashlib.md5(data.encode('UTF-8')).hexdigest()
write_data(dig)