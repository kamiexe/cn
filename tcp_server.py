import socket

# Create a TCP server socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to an address and port
server_address = ('localhost', 65432)
tcp_server_socket.bind(server_address)

# Listen for incoming connections
tcp_server_socket.listen(1)
print("TCP Server is listening...")

while True:
    # Accept a connection
    connection, client_address = tcp_server_socket.accept()
    try:
        print(f"Connection from {client_address}")
        
        # Receive data
        data = connection.recv(1024)
        if data:
            print(f"Received: {data.decode()}")
            
            # Send a response
            response = "Message received by TCP Server"
            connection.sendall(response.encode())
    finally:
        connection.close()
