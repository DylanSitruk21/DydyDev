import jpysocket
import socket
from _thread import *


def new_client(client_socket, thread_num):
    msg_recv = client_socket.recv(1024)  # Receive UserName
    msg_recv = jpysocket.jpydecode(msg_recv)
    client_name = msg_recv.split(': ')[1]
    client_names.append(client_name)
    while True:
        msg_recv = client_socket.recv(1024)  # Receive msg
        msg_recv = jpysocket.jpydecode(msg_recv)  # Decrypt msg
        if msg_recv:
            print(msg_recv, "(thread number:", thread_num, ")")
            msg_split = msg_recv.split('\"')
            # answer = msg_split[3]
            message = client_name + ":" + msg_split[1]
            receiver = msg_recv.split()[-1]
            if client_names.count(receiver) == 1:
                msg_send = jpysocket.jpyencode(message)  # Encrypt The Msg
                receiver_id = client_names.index(receiver)
                client_sockets[receiver_id].send(msg_send)  # Send Msg
            else:
                print("Error: There is " + str(client_names.count(receiver)) + " \'" + receiver + "\' in the list")
                msg_send = jpysocket.jpyencode("Server: This user doesn't exist ..")
                client_socket.send(msg_send)  # Send Msg

    # connection.close()


if __name__ == '__main__':

    client_sockets = []
    client_names = []
    host = 'localhost'  # Host Name
    port = 12345  # Port Number
    ThreadCount = 0
    server_socket = socket.socket()  # Create Socket
    print("Server socket is: ", server_socket)
    server_socket.bind((host, port))  # Bind Port And Host
    server_socket.listen(5)  # Socket is Listening
    print("Socket Is Listening....")
    while True:
        socket, address = server_socket.accept()  # Accept the Connection
        client_sockets.append(socket)
        print("Client socket is: ", socket)
        print("Connected To ", address)
        ThreadCount += 1
        start_new_thread(new_client, (socket, ThreadCount,))
        print('Thread counter = ' + str(ThreadCount))

    # s.close()  # Close connection
    # print("Connection Closed.")
