from os import error
import socket


sock = socket.socket(proto=socket.IPPROTO_TCP)

try:
    sock.bind(("192.168.11.148", 42069))
    sock.listen(-1)

except Exception as err:
    print(err)

else:
    conn, addr = sock.accept()
    print("Входящий адрес: ", addr)
    recv_string = conn.recv(1024).decode(encoding="utf-8")

    while recv_string != "exit":
        print("Message: ", recv_string)
        recv_string = conn.recv(1024).decode(encoding="utf-8")

finally:
    sock.close()