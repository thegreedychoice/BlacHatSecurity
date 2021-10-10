import socket

target_host = "www.google.com"
target_port = 80

# create a socket object & configure first parameter for standard IPv4 or hostname and second for TCP Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print("Following response received: \n")
print(response.decode())
client.close()

# TODO - Update code for following assumptions
# 1. The connection to target will always succeed.
# 2. Server expects us to send data first instead of vice-versa.
# 3. Server will always return data to client in timely fashion.