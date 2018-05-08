import socket
import thread
import math
import matrixOperation as mo
import time
    
def createWork(matrix, fold):
    work = []
    
    split = int(math.ceil(len(matrix) / fold))
    
    index = 0
    for i in range(fold):
        split_matrix = matrix[index : index + (split * (i + 1))]
        work.append(mo.convertMatrixToBytes(split_matrix))
        index += split
        
    return work

def workerNode(workersocket, addr, work):
    # initialization
    while True:
        msg = workersocket.recv(10)
        if msg == 'Accept':
            print(msg)
            break
    
    # send work to worker
    workersocket.send('Size:' + str(len(work)))
    
    while True:
        msg = workersocket.recv(10)
        if msg == 'Start':
            print(msg)
            break
    
    workersocket.send(work)
    
    # wait for response
    while True:
        msg = workersocket.recv(10)
        if msg == 'Done':
            print(msg)
            break
    workersocket.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('10.0.0.1', 10021))
    s.listen(10)
    
    infile1 = open('5000_1.txt', 'r')
    infile2 = open('t2.txt', 'r')
    matrix1 = mo.readMatrix(infile1)
    
    work = createWork(matrix1, 1)
    print(len(work))
    
    start_time = time.time()
    while True:
        try:
            (workersocket, addr) = s.accept()
            thread.start_new_thread(workerNode, (workersocket, addr, work[0]))
        except KeyboardInterrupt:
            print('Keyboard interruption')
            break
        
    s.close()
    
    end_time = time.time()
    diff = end_time - start_time
    print('Running time: ' + str(diff))
    
    infile1.close()
    infile2.close()