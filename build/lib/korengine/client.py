import socket
import select
import threading
import time
from korengine.Game_class import Game
from korengine.Entity_class import Entity
from korengine.EntityData import EntityData  # Assuming you have the EntityData class

server_ip = "0.tcp.au.ngrok.io"
port = 11225
daGameInstance = None
daPlayer = None

def handle_server_messages(client):
    """Handles incoming messages without blocking and passes data to game instance."""
    while True:
        ready_to_read, _, _ = select.select([client], [], [], 0.1)  # Check if data is available
        if ready_to_read:
            try:
                response = client.recv(1024).decode()
                if not response:
                    print("Server closed connection")
                    break

                # Assuming the server sends a string of entity data (name,x,y|name2,x2,y2...)
                entity_strings = response.split("|")
                entities_data = []
                for entity_str in entity_strings:
                    entity = EntityData.deserialize(entity_str)
                    if entity:
                        entities_data.append(entity)

                # Now pass the data to the game instance
                if daGameInstance:
                    daGameInstance.OnServerDataReceived(entities_data)

            except Exception as e:
                print(f"Error handling server message: {e}")
                break

def send_player_data(client):
    """Continuously sends player entity data to the server."""
    while True:
        if daPlayer:  # Ensure the player exists
            # Prepare the player entity data to send
            entity_data = EntityData(daPlayer.name, daPlayer.position[0], daPlayer.position[1])
            client.send(entity_data.serialize().encode())
            time.sleep(0.1)  # Adjust the interval as necessary (e.g., 100ms)

def send_messages(client):
    """Handles user input separately to avoid blocking."""
    while True:
        message = input()  # This blocks, but it's in another thread
        if message.lower() == 'quit':
            break
        client.send(message.encode())

def start_client(gameInstance: Game, playerEntity: Entity):
    global daGameInstance
    global daPlayer
    daGameInstance = gameInstance
    daPlayer = playerEntity

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))
    client.setblocking(False)  # Make socket non-blocking

    # Start threads for sending and receiving
    recv_thread = threading.Thread(target=handle_server_messages, args=(client,), daemon=True)
    recv_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

    send_player_thread = threading.Thread(target=send_player_data, args=(client,))  # New thread to send player data
    send_player_thread.start()

    send_thread.join()  # Wait for user to finish input
    send_player_thread.join()  # Ensure the player data sending thread runs
    client.close()

if __name__ == "__main__":
    start_client()
