import socket


sock = socket.socket(proto=socket.IPPROTO_TCP)

sock.connect(("localhost", 42069))

send_string = input("Enter: ")


while send_string != "exit":
    sock.send(bytearray(send_string, encoding="utf-8"))
    send_string = input("Enter: ")
sock.send(bytearray(send_string, encoding="utf-8"))
sock.close()