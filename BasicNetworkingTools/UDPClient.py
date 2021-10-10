import socket

target_host = "127.0.0.1"
target_port = 9997

# create a socket object and configure parameters for standard Ipv4 or hostname and UDPClient
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(b"AAABBBCCC", (target_host, target_port))

# receive some data, it returns both data and remote host and port
data, addr = client.recvfrom(4096)

print("Following response received:")
print(data.decode())
client.close()