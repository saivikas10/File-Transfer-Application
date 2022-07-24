import socket
import os

#taking the contents name
contents=os.listdir("serverf/")
str='files:'
for i in contents:
    str=str+"\n"+i
stri=str.encode('utf-8')

#specifiying the port and ip address
port = 10001
ip_address = '127.0.0.1'

# using TCP connection for reliable transfer
socketf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#associating the socket to the port
socketf.bind((ip_address, port))
socketf.listen(1)
print(f'enter the {ip_address} in the client')
print('server is listening mode')

while True:
    #accepting the connection
    TCP_connection, client_address = socketf.accept()
    if TCP_connection:
        print("sending contents")
        #sending the directory contents
        TCP_connection.send(stri)
        while True:
            filename=TCP_connection.recv(10000).decode('utf-8')
            #stopping the connection
            if filename=="no":
                break
            print(f"received file request: {filename}")
            #checking if file is present in directory
            if filename in contents:
                TCP_connection.send('True'.encode('utf-8'))
                #sending the requested file
                with open('serverf/'+filename, 'rb') as file:
                    TCP_connection.send(file.read())
                    file.close()
            else:
                print("requested file not present")
                TCP_connection.send('False'.encode('utf-8'))
        break
socketf.close()
print('connection ended')