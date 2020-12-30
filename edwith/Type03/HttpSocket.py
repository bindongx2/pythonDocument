import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() #UTF-8로 ENCODE
mysock.send(cmd)

while True:
    data  = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode()) # UTF-8 --> 유니코드 형태로 DECODE
mysock.close()


# http header
# 띄어쓰기(header, body 구분값)
# http body
