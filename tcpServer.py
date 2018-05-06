import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('10.0.0.1', 10021))
    s.listen(5)
    while 1:
        (clientsocket, address) = s.accept()
        l = clientsocket.recv(1024)
        print(l)
        while (l):
            l = clientsocket.recv(1024)
            print(l)
        clientsocket.send('Yo')
        
        clientsocket.close()
        
    s.close()