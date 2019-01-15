import threading
import os
import socket


def RecvProcess ( UDP_Socket, LocalAddrInfo ):
    print('UDP Recver is UP')
    while 1:
        data, PeerAddr = UDP_Socket.recvfrom ( 1024 )
        if data == 'local exit' and LocalAddrInfo == PeerAddr:
            print('RecvProcess was terminated!')
            break
        #data = raw_input ()
        print('%s(MessageFrom %s:%d)' % ( data, PeerAddr[0], PeerAddr[1] ))

if __name__ == '__main__':
    #Create UDP socekt
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #Get local machine name
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    addrinfo = ( myaddr, 5060 )
    print(myaddr)
    s.bind( addrinfo )
    #Start the Recv process
    threadrecv = threading.Thread ( target = RecvProcess, args = (s, addrinfo) )
    threadrecv.start ()
    while 1:
        val = raw_input()
        if val == 'exit':
            s.sendto ( 'local exit', addrinfo )
            break
        s.sendto ( val, ( '192.168.3.36', 5060) )
    print('quit')
