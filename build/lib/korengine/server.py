import asyncio
import socket
from korengine.Game_class import Game
from korengine.EntityData import EntityData  # Assuming you have the EntityData class

daGameInstance = None
clients = set()  # Track connected clients

async def handle_client(reader, writer):
    """Handles communication with a single client and passes data to the game instance."""
    global clients
    address = writer.get_extra_info('peername')
    print(f"New connection from {address}")
    clients.add(writer)  # Track connected clients

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break  # Connection was closed by the client
            message = data.decode()
            print(f"Received from {address}: {message}")
            
            # Assuming the message is in the format "player_name,x_position,y_position"
            try:
                # Split the message into components
                player_data = message.split(',')
                if len(player_data) > 0:
                    player_name = player_data[0]
                    x_position = float(player_data[1])
                    y_position = float(player_data[2])

                    # Create an entity with the received player data
                    entity = EntityData(player_name, x_position, y_position)

                    # Pass the data to the game instance (assuming OnClientDataReceived is implemented)
                    if daGameInstance:
                        daGameInstance.OnClientDataReceived(entity)

            except Exception as e:
                print(f"Error processing client data: {e}")
            
            # Send an acknowledgment to the client
            writer.write("Message received".encode())
            await writer.drain()

    except Exception as e:
        print(f"Error handling client {address}: {e}")
    finally:
        print(f"Connection closed: {address}")
        clients.remove(writer)  # Remove disconnected clients
        writer.close()
        await writer.wait_closed()

async def send_entity_updates():
    """Continuously sends all entity data to connected clients."""
    global daGameInstance, clients
    while True:
        if daGameInstance:
            entities_data = []
            for entity in daGameInstance.allEntities:  # Assuming `entities` is a list of entity objects
                # Assuming `EntityData` can serialize the entity to a string format
                entity_data = EntityData(entity.name, entity.position[0], entity.position[1])
                entities_data.append(entity_data.serialize())

            update_message = "|".join(entities_data)  # Use '|' as a separator for multiple entities

            # Send update to all clients
            for client in clients.copy():  # Use copy() to avoid modification issues during iteration
                try:
                    print(f"Server sending: {update_message}")
                    client.write(update_message.encode())
                    await client.drain()
                except Exception as e:
                    print(f"Error sending update to client: {e}")
                    clients.remove(client)  # Remove disconnected clients

        await asyncio.sleep(0.1)  # Send updates every 100ms

async def start_server(gameInstance: Game, host='0.0.0.0', port=5555):
    """Starts the server and continuously sends game updates."""
    global daGameInstance
    daGameInstance = gameInstance
    server = await asyncio.start_server(handle_client, host, port)
    
    addr = server.sockets[0].getsockname()
    print(f"Server started on {addr}")

    # Start the update loop to send entity data periodically
    asyncio.create_task(send_entity_updates())

    async with server:
        await server.serve_forever()  # Run the server forever
