import socket
import random


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 9000))
server_socket.listen()
print("Server is listening on 9000...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")
while True:
    data = conn.recv(1024).decode()
    if not data:
        print("Client disconnected")
        break
    client_name, int_client = data.split(",")
    client_name_full = client_name.strip()
    int_client = int(int_client.strip())
    if int_client < 1 or int_client > 100:
        print("Invalid integer. Exiting...")
        break
    name = "2301MC40"
    int_server = random.randint(1, 100)
    server_name_full = f"Server of {name}"
    client_name = client_name_full.replace("Client of ", "")
    server_name = name
    print(f"Client's name: {client_name}")
    print(f"Client's integer: {int_client}")
    print(f"Server's name: {server_name}")
    print(f"Server's integer: {int_server}")
    print(f"Full message received: {client_name_full}, {int_client}")
    print(f"Full message sent: {server_name_full}, {int_server}")
    print(f"The sum: {int_client + int_server}")
    reply = f"{server_name_full},{int_server}"
    conn.send(reply.encode())


conn.close()