import os
import requests
import json
import platform

room_name = input("Room Name  : ")
room_url = input("Room URL (https://<replit project name>.<acc name>.repl.co) : ")

f = open("Chatroom-replit/info.json","w")
f.write(json.dumps({"name":room_name, "url" : room_url}))
f.close()

def P():
    response = requests.get(f"https://backendjustchat.darkmash.repl.co/find/{room_name}")
    return response.text == room_url

if P():
  os.system(f"python3 Chatroom-replit/api.py 0.0.0.0 8000")


def start_server(ip, port):
    if not P():
        if platform.system().lower() == "linux":
            os.system(f"python3 Chatroom-replit/verify.py {ip} {port}")
        else:
            os.system(f"python Chatroom-replit/verify.py {ip} {port}")      


    os.system(f"python3 Chatroom-replit/api.py {ip} {port}")

def main():
    start_server("0.0.0.0", 8000)
   
if __name__ == "__main__":
    main()
