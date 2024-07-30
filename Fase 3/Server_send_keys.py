import socket
import time

with open("/home/tfg/server/Fase3/victim_ip.txt", "r") as f:
        IP = f.read()

PORT = 8081
ADDR = (IP, PORT)


def sender():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect(ADDR)
        
        with open("/home/tfg/server/Fase3/keys/key.pkl", "rb") as f:
                data = f.read()
                server.send("key.pkl".encode())
                time.sleep(2)
                server.send(data)

        server.close()


if __name__ == '__main__':
        sender()
