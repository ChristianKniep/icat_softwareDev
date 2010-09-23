# Echo server program
import socket,time

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8888              # Arbitrary non-privileged port

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Pin it down on a Port
s.bind((HOST, PORT))

s.listen(1)


conn, addr = s.accept()
print 'Connected by', addr

while 1:
    data = conn.recv(10)
    time.sleep(5)
    print data
    

conn.close()
