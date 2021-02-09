# script for lunching sever

import time, os

from http_server import http_server
from socket_comm import socket_comm

if __name__ == '__main__':

	print("Creation du websocket...\n")
	server_socket = socket_comm()
	print(server_socket.listen("127.0.0.1", 60000, 5))
	print(server_socket.listen("127.0.0.1", 60001, 5))
	time.sleep(5)
	print(server_socket.connect("127.0.0.1", 50000))
	print(server_socket.connect("127.0.0.1", 50001))

	time.sleep(20)
	server_socket.stop_threads = True

	command = 'kill -9 $(lsof -t -i tcp:60000)'
	os.system(command)
	command = 'kill -9 $(lsof -t -i tcp:60001)'
	os.system(command)
