import socket

class Server:

    def send_file(data):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("192.168.1.123", 8080))

        client.send("AES_key.pkl".encode())

        client.sendall(data)
        client.send(b"<END>")

        client.close()


    def recive_file():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("192.168.1.123", 8080))
        server.listen()

        client, address = server.accept()

        file_name = client.recv(1024).decode()
        print(file_name)

        with open(file_name, "wb") as f:
            file_bytes = b""

            done = False

            while not done:
                data = client.recv(1024)
                if file_bytes[-5:] == b"<END>":
                    done = True
                else:
                    file_bytes += data

            print(file_bytes)
            f.write(file_bytes)

        server.close()
        client.close()

        return file_bytes