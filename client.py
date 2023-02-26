import sys
from network import Network


print("Connecting to server.....")

try:
    net = Network()
    is_connected = True
    print("Connected to server")
except Exception as e:
    print("Connection to server failed")
    net = None
    is_connected = False
    print(e)


if is_connected is True and net is not None:
    print("Start Communicating")
    while True:
        command = str(input("command >> : "))
        if command == "exit":
            net.disconnect()
            print("Disconnected")
            break
        else:
            print("Sending request")
            net.send(command)
            print("Request Sent")
            print("Waiting for response")
            data = net.receive()
            print("Response received")
            print("Response : ", data)
    sys.exit()
