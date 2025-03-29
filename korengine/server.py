import asyncio
import socket
from korengine.Game_class import Game
from EntityData import EntityData  # Assuming you have the EntityData class

daGameInstance = None
clients = set()  # Track connected clients

async def handle_client(reader, writer):
    """Handles communication with a single client."""
    global clients
    address = writer.get_extra_info('peername')
    print(f"New connection from {address}")
    clients.add(writer)  # Track connected clients

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            message = data.decode()
            print(f"Received from {address}: {message}")
            
            # Send an acknowledgment
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
                entity_data = EntityData(entity.name, entity.position[0], entity.position[1])
                entities_data.append(entity_data.serialize())

            update_message = "|".join(entities_data)  # Use '|' as a separator for multiple entities

            # Send update to all clients
            for client in clients.copy():  # Use copy() to avoid modification issues
                try:
                    client.write(update_message.encode())
                    await client.drain()
                except Exception:
                    clients.remove(client)  # Remove disconnected clients

        await asyncio.sleep(0.1)  # Send updates every 100ms

async def start_server(gameInstance: Game, host='0.0.0.0', port=5555):
    """Starts the server and continuously sends game updates."""
    global daGameInstance
    daGameInstance = gameInstance
    server = await asyncio.start_server(handle_client, host, port)
    
    addr = server.sockets[0].getsockname()
    print(f"Server started on {addr}")

    # Start the update loop
    asyncio.create_task(send_entity_updates())

    async with server:
        await server.serve_forever()
