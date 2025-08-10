import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8767))
print("connected to server on 9000")
name = "Anish Kumar"
while True:
    int_client = int(input("Enter your integer between 1 to 100: "))
    msg = f"Client of {name},{int_client}"
    client_socket.send(msg.encode())
    reply = client_socket.recv(1024).decode()
    server_name_full, int_server = reply.split(",")
    server_name_full = server_name_full.strip()
    int_server = int(int_server.strip())
    server_name = server_name_full.replace("Server of ", "")
    print(f"Client's name: {name}")
    print(f"Client's integer: {int_client}")
    print(f"Server's name: {server_name}")
    print(f"Server's integer: {int_server}")
    print(f"Full message sent: Client of {name}, {int_client}")
    print(f"Full message received: {server_name_full}, {int_server}")
    print(f"The Sum of both integers: {int_client + int_server}")
    break

client_socket.close()