import socket
import threading
import sys


HOST = "127.0.0.1"
PORT = 4040 



def hear_the_server(client:socket.socket):
  
  
  while True :
    msg = client.recv(2048).decode("utf-8")
    if msg:
      username = msg.split(":")[0]
      contant  = msg.split(":")[1]
      print(f"[SERVER][{username}] {contant}")
    else:
      print("[SERVER] CLient Send an Empty massege!")


def send(client:socket.socket):
  print("'leave' for leave")
  while True:
      msg = input("[SERVER] Send message:")
      if msg:
        if msg == "leave":
          sys.exit()
        client.sendall(msg.encode())

      else:
        print("[SERVER] Message can't be empy!")

def talk_to_server(client:socket.socket):
  username = input("[SERVER] Enter username: ")
  if username:
    client.sendall(username.encode())
  else:
    print("[SERVER] Username can't be Empty!!")
    exit(0)
  
  threading.Thread(target=hear_the_server, args=(client,)).start()
  
  send(client)

def main():
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    
    client.connect((HOST,PORT))
    print(f"[SERVER] You sucessfully connected to server.")
  except:
    print(f"The Server you're trying t connect {HOST}:{PORT} is down at the moment.")


  talk_to_server(client)
if __name__ =="__main__":
  main()
