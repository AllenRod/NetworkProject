import socket
import time

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.0.0.1', 10021))
    
    # send init msg 
    s.send('Accept')
    
    msg = s.recv(100)
    total_len = -1
    if msg.startswith('Size'):
        total_len = int(msg.split(':')[1])
        
    print(total_len)
    
    s.send('Start')
    
    received = s.recv(1024)
    work = received
    while len(work) < total_len:
        received = s.recv(1024)
        work += received
        
    print(len(work))
        
    s.send('Done')
    
    s.close()