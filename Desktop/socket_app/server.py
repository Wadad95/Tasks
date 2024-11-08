import socket
import threading

def handle_client(client_socket):
    try:
        # Ta emot namn från klienten
        name = client_socket.recv(1024).decode('utf-8')
        if not name:
            print("Client did not send a name.")
            return
        print(f"Client {name} connected.")
        
        while True:
            # Vänta på meddelande från klienten
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"Client {name} has disconnected.")
                break
            
            print(f"Message from {name}: {message}")
            
            # Skicka svar till klienten
            client_socket.send(f"Server received: {message}".encode('utf-8'))
        
    except Exception as e:
        print(f"Error handling client {name}: {e}")
    
    finally:
        # Stäng anslutningen när klienten kopplas bort
        print(f"Closing connection with {name}")
        client_socket.close()
        print(f"Client {name} connection closed.")

def start_server():
    host = "127.0.0.1"
    port = 49153

    try:
        # Skapa serverns socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server listening on {host}:{port}")
        
        while True:
            # Vänta på anslutningar
            client_socket, addr = server_socket.accept()
            print(f"Connection established with {addr}")
            
            # Starta en tråd för att hantera varje klient
            threading.Thread(target=handle_client, args=(client_socket,)).start()
    
    except Exception as e:
        print(f"Error starting server: {e}")
    
    finally:
        # Stäng serverns socket när den stängs
        print("Server shutting down.")
        server_socket.close()
        print("Server socket closed.")

if __name__ == "__main__":
    start_server()
