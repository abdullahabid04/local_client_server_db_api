from _thread import *
import logging
import traceback
import socket
import sys
import os

from communication import Communication


logger = logging.getLogger(__name__)
print("Starting Server.....")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Waiting for the server to start.....")
host = "192.168.231.141"
port = 5555


def start_server():
    print("Waiting foe new connections.....")
    server.listen()
    current_client = 0
    while True:
        conn, addr = server.accept()
        print("New connection established")
        start_new_thread(threaded_client, (conn, current_client))
        current_client += 1


def bind_server(host_, port_):
    try:
        server.bind((host_, port_))
        print("Server Started")
        return True
    except socket.error as e:
        print(str(e))
        return False


def is_socket_closed(sock: socket.socket) -> bool:
    try:
        print("Checking if the connection is still alive.....")
        data = sock.recv(16, socket.MSG_DONTWAIT | socket.MSG_PEEK)
        if len(data) == 0:
            return True
        else:
            return False
    except BlockingIOError:
        return True
    except ConnectionResetError:
        return True
    except Exception as e:
        logger.exception("unexpected exception when checking if a socket is closed")
        return True
    finally:
        print("Connection is alive")
        return False


def threaded_client(cxn, client_id):
    comm = Communication(client_id)
    reply = ""
    while True:
        try:
            data = cxn.recv(4096).decode()
            if not data:
                print("Disconnected")
                break
            else:
                reply = comm.send_request(data)
                print("Received ", data)
                print("Sending ", reply)
            cxn.sendall(reply.encode())
            print("Sent SuccessFully")
            print("Waiting for new request.....")
        except Exception as e:
            traceback.print_exc()
            print(e)
            break
    print("Lost Connection")
    cxn.close()


def main():
    is_bind = bind_server(host, port)
    if is_bind:
        start_server()
    else:
        pass


if __name__ == "__main__":
    main()
