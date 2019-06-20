import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
#This encode convert the unicode in UTF-8 iternally
sock.send(cmd)
while True:
    data = sock.recv(512)
    if (len(data)<1):
        break
    print(data.decode(),end=" ")
sock.close()
