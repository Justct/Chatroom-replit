import os

def start_server(ip, port):
    os.system(f"python3 Chatroom/api.py {ip} {port}")

def main():
    start_server("0.0.0.0", 8000)
   
if __name__ == "__main__":
    main()
