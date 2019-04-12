import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.bind(('',2222));

s.listen(10);
i=0;
while True:
    conn, addr = s.accept();
    print 'connected: ', addr
    print 'i:  ', i
    i += 1
    while True:
        data = conn.recv(1024)
        if  data=="close":
            break;
        conn.send(data);
        print 'data: ',data
     
    conn.close();
    