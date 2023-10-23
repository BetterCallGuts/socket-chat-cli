import socket 
import threading
import time


HOST = '127.0.0.1'
PORT = 4040   #0: 65535
LIMIT= 5
Active_clients = []


def listen_for_massg(client:socket.socket, username):
  while 1:
    res = client.recv(2048).decode("utf-8")
    if res:
      msg = f"{username}: {res}"
      send_massege_to_all( msg)

    else:
      print(f"The message send from {username} is empty")



def send_massege_to_client(client:socket.socket, msg):
  
  client.sendall(msg.encode())  

def send_massege_to_all( masseg):
  
  for user in Active_clients:
    send_massege_to_client(user[1], masseg)



def handle_client(client:socket.socket, addr:tuple):

  print(f"[SERVER] CLient{addr[0]}:{addr[1]} is connected!")

  while True:
    username = client.recv(2048).decode("utf-8")
    if username:
      Active_clients.append((username, client))
      threading.Thread(target=send_massege_to_all, args=(f"[SERVER] {username} joined the chat!",))
      break
    else:
      print("Client user name is Empty")
  threading.Thread(target=listen_for_massg  , args=(client, username)).start()

def main():
  print(f"[SERVER] creating the server", end="", flush=1)
  for i in range(3):
    time.sleep(1)
    print(".", end="", flush=1)
  print("")

  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print(f"[SERVER] Server is starting", end="", flush=1)
  for i in range(3):
    time.sleep(1)
    print(".", end="", flush=1)
  print("")
  try:
    server.bind((HOST, PORT))

    server.listen(LIMIT)
    is_server_open = True
    print(f"[SERVER] Server is listining in {HOST}:{PORT}")
    while is_server_open:
      client, addr = server.accept()
      # print(client,"____" ,addr)
      threading.Thread(target=handle_client, args=(client, addr)).start()

  except:

    print(f"[SERVER] Unable to bind in {HOST}:{PORT}")



if __name__ == "__main__":
  
  main()

  