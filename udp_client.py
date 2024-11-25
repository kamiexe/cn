import socket

# Create a UDP client socket
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port (same as the TCP server)
server_address = ('localhost', 65432)

# Send a message to the server
message = "Hello, TCP Server!"
udp_client_socket.sendto(message.encode(), server_address)
print(f"Message sent: {message}")

# UDP cannot directly receive TCP responses.
# You may simulate a response from the server by handling the logic explicitly.
udp_client_socket.close()
