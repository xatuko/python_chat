import socket


sock = socket.socket(proto=socket.IPPROTO_TCP)
sock.bind(("", 42069))
sock.listen(1)

conn, addr = sock.accept()

print("Входящий адрес: ", addr)

recv_string = conn.recv(1024).decode(encoding="utf-8")

while recv_string != "exit":
    print("Message: ", recv_string)
    recv_string = conn.recv(1024).decode(encoding="utf-8")

sock.close()