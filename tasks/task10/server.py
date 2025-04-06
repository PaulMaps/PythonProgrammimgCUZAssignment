import socket

HOST = 'localhost'  # or use '127.0.0.1'
PORT = 65432        # Choose a port number above 1024

try:
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))     # Bind the socket to host and port
    server_socket.listen()               # Start listening for connections

    print(f"Server is listening on {HOST}:{PORT}...")

    conn, addr = server_socket.accept()  # Accept a connection
    print(f"Connected by {addr}")

    message = "Hello from server!"
    conn.sendall(message.encode('utf-8'))  # Send the message

    conn.close()  # Close connection
    print("Server connection closed.")

except Exception as e:
    print(f"Server error: {e}")
