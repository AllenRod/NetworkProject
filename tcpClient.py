import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.0.0.1', 10021))
    f = open('t1.txt', 'rb')
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)
    data = s.recv(10)
    if data:
        print(data)
    s.close()