from socket_comm import socket_comm
import time

server_socket = socket_comm("127.0.0.1", 60001)
server_socket.listen(5)
time.sleep(3)

server_socket.connect("127.0.0.1", 60000)
time.sleep(.5)

server_socket.send_message("Hello client!")
time.sleep(.5)

server_socket.send_message("Hello again client!")
time.sleep(.5)

server_socket.stop_threads = True
