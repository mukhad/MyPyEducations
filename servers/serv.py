import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.bind(('',1234));

s.listen(10);

conn, addr = s.accept();

print 'connected:', addr
    
while True:
    data = conn.recv(1024)
    if  data=="close":
        break;
    conn.send(data);
    print 'data: ',data
     
conn.close();
        

print ("hello")

