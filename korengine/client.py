import socket
import select
import threading

server_ip = "0.tcp.au.ngrok.io"
port = 11225

def handle_server_messages(client):
    """Handles incoming messages without blocking."""
    while True:
        ready_to_read, _, _ = select.select([client], [], [], 0.1)  # Check if data is available
        if ready_to_read:
            try:
                response = client.recv(1024).decode()
                if not response:
                    print("Server closed connection")
                    break
                print(f"\nServer response: {response}")
            except:
                break

def send_messages(client):
    """Handles user input separately to avoid blocking."""
    while True:
        message = input()  # This blocks, but it's in another thread
        if message.lower() == 'quit':
            break
        client.send(message.encode())

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))
    client.setblocking(False)  # Make socket non-blocking

    # Start threads for sending and receiving
    recv_thread = threading.Thread(target=handle_server_messages, args=(client,), daemon=True)
    recv_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

    send_thread.join()  # Wait for user to finish input
    client.close()

if __name__ == "__main__":
    start_client()
