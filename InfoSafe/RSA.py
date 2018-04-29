import rsa

def read_data(path='/home/wlj/PycharmProjects/InfoSafe/date.txt'):
    with open(path) as f:
        data=f.read()
    return data.replace('\n','')

def write_data(data,path="/home/wlj/PycharmProjects/InfoSafe/code.txt"):
    with open(path, 'a') as f:
        f.write(data.decode('UTF-8',"ignore"))

key = rsa.newkeys(3000)
privateKey = key[1]
publicKey = key[0]
data =read_data().encode('UTF-8')
crypteddata = rsa.encrypt(data, publicKey)
write_data(crypteddata)
data = rsa.decrypt(crypteddata, privateKey)
data = data.decode()
print(crypteddata,data)
