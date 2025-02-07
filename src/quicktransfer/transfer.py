import socket
import os
import tqdm
import argparse

PORT = 12345

def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        print(f"[*] Starting server on 0.0.0.0:{PORT}")
        server.bind(('0.0.0.0', PORT))
        server.listen(1)
        print("[*] Server started. Waiting for connections...")
        print("[*] Your IP address is:", socket.gethostbyname(socket.gethostname()))
        
        client, addr = server.accept()
        print(f"[+] {addr} is connected.")
        
        filename = client.recv(1024).decode()
        filesize = int(client.recv(1024).decode())
        
        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", 
                            unit="B", unit_scale=True, unit_divisor=1024)
        
        with open(f"received_{filename}", "wb") as f:
            while True:
                bytes_read = client.recv(4096)
                if not bytes_read:
                    break
                f.write(bytes_read)
                progress.update(len(bytes_read))
        
        print(f"\n[+] File {filename} received successfully")
        client.close()
        server.close()
        
    except Exception as e:
        print(f"[!] Server error: {str(e)}")
        if 'server' in locals():
            server.close()

def send_file(host, filename):
    try:
        if not os.path.exists(filename):
            print(f"[!] File {filename} not found!")
            return
            
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"[*] Connecting to {host}:{PORT}...")
        client.settimeout(10)
        client.connect((host, PORT))
        print("[+] Connected successfully!")
        
        client.send(filename.encode())
        filesize = os.path.getsize(filename)
        client.send(str(filesize).encode())
        
        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", 
                            unit="B", unit_scale=True, unit_divisor=1024)
        
        with open(filename, "rb") as f:
            while True:
                bytes_read = f.read(4096)
                if not bytes_read:
                    break
                client.sendall(bytes_read)
                progress.update(len(bytes_read))
        
        print(f"\n[+] File {filename} sent successfully")
        client.close()
        
    except ConnectionRefusedError:
        print(f"[!] Connection refused! Make sure the server is running on {host}:{PORT}")
    except socket.timeout:
        print(f"[!] Connection timed out! Check if {host} is correct and reachable")
    except Exception as e:
        print(f"[!] Error: {str(e)}")
    finally:
        if 'client' in locals():
            client.close()

def main():
    parser = argparse.ArgumentParser(description="Simple P2P File Transfer")
    parser.add_argument('--mode', choices=['send', 'receive'], required=True,
                      help='Choose to send or receive')
    parser.add_argument('--file', help='File to send')
    parser.add_argument('--host', help='Host to connect to')
    args = parser.parse_args()
    
    if args.mode == 'receive':
        start_server()
    elif args.mode == 'send':
        if not args.file or not args.host:
            print("[!] Both --file and --host are required for send mode")
            return
        send_file(args.host, args.file)

if __name__ == "__main__":
    main()