import os
import requests
import json
import platform

room_name = input("Room Name  : ")
room_url = input("Room URL (https://<replit project name>.<acc name>.repl.co) : ")

f = open("info.json","w")
f.write(json.dumps({"name":room_name, "url" : room_url}))
f.close()

def P():
    response = requests.get(f"https://backendjustchat.darkmash.repl.co/find/{room_name}")
    return response.text == room_url

def start_server(ip, port):
    if not P():
        if platform.system().lower() == "linux":
            os.system(f"python3 verify.py {ip} {port}")
        else:
            os.system(f"python verify.py {ip} {port}")      
    print("WAIT 10 SECS")
    time.sleep(10)
    if not P():
        print("The room url and the url provided didnt match or someother error!! Quiting")
        quit()

    os.system(f"python3 api.py {ip} {port}")

def main():
    start_server("0.0.0.0", 8000)
   
if __name__ == "__main__":
    main()
