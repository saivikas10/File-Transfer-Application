import socket
#specifiying the address and port of server
ip_address=input('enter the ip address of server: ')
port = 10001

#creating a socket of ipv4 family type and TCP protocol
socketf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to server using TCP connection
socketf.connect((ip_address, port))
print("Connecting is being established\n")

#taking the contents of the directory
contents=socketf.recv(100000)
contentss=contents.decode('utf-8')

#while loop for requesting and receiving the files
while True:
        print(contentss)
        f=input("\ninput the file name you want to transfer else input 'no':")
        #checking if client wants to end the connection
        if f=='no':
                socketf.send(f.encode('utf-8'))
                break
        else:
                socketf.send(f.encode('utf-8'))
                print("sent the request")
                data=socketf.recv(100000)
                if data.decode('utf-8')=="False":
                        print("file not present\n")
                else:
                        data=socketf.recv(100000)
                        #downloading the file
                        with open('clientf/'+f, 'wb') as file:
                                print("requested the file ")
                                file.write(data)
                                print("file received\n")
                                file.close()
socketf.close()
print('connection ended')