import socket

target_host = "127.0.0.1"
target_port = 9997

"""
UDP Client

Because UDP is a connectionless protocol, there is no call to connect() beforehand.
The last step is to call recvfrom() to receive UDP data back.  You will notice that
it returns both the data and the details of the remote host and port.
"""

if __name__ == "__main__":
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # send some data
    client.sendto(b"AAABBBCCC", (target_host, target_port))

    # receive some data
    data, addr = client.recvfrom(4096)

    print(data.decode())
    client.close()
