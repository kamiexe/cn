import socket

# Create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'  # Server's IP address
port = 12345
client_socket.connect((host, port))
print(f"Connected to server at {host}:{port}")

# Send data to the server
message = input("Enter a message to send to the server: ")
client_socket.send(message.encode())

# Receive response from the server
response = client_socket.recv(1024).decode()
print(f"Received from server: {response}")

# Close the connection
client_socket.close()
