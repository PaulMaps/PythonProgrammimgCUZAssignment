import socket

HOST = 'localhost'
PORT = 65432

try:
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))  # Connect to the server

    # Receive the message
    data = client_socket.recv(1024)  # receive up to 1024 bytes
    print("Received from server:", data.decode('utf-8'))

    client_socket.close()

except ConnectionRefusedError:
    print("Server is not running or cannot be reached.")
except Exception as e:
    print(f"Client error: {e}")
 