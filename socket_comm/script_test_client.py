from socket_comm import socket_comm
import time

client_socket = socket_comm()
client_socket.listen("127.0.0.1", 60000, 5)
time.sleep(1)

client_socket.connect("127.0.0.1", 60001)
time.sleep(.2)

client_socket.send_message("Hello server!")
time.sleep(.5)

client_socket.send_message("Hello again server!")
time.sleep(.5)

client_socket.stop_threads = True
