import socket

def start_client():
    host = "127.0.0.1"
    port = 49153

    # Skapa en klient socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Anslut till servern
        client_socket.connect((host, port))
        
        # Skicka namn till servern
        name = input("Enter your name: ")
        client_socket.send(name.encode('utf-8'))
        
        while True:
            # Ta emot serverns meddelande
            server_response = client_socket.recv(1024).decode('utf-8')
            print(server_response)
            
            # Skicka ett meddelande till servern
            message = input(f"{name}: ")
            if message.lower() == 'exit':  # Klient slutar om 'exit' skrivs
                break
            client_socket.send(message.encode('utf-8'))
    
    except Exception as e:
        print(f"Error in client: {e}")
    
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    start_client()
