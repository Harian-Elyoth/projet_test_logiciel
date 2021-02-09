# script for lunching sever

import time

from http_server import http_server
from socket_comm import socket_comm

if __name__ == '__main__':

	print("Creation du Serveur HTTP...\n")
	serv_test = http_server("127.0.0.1", 60000)

	print("Creation du websocket...\n")
	server_socket = socket_comm("127.0.0.1", 60001)
	server_socket.listen(5)
	time.sleep(3)
	server_socket.connect("127.0.0.1", 60002)
	# server_socket.connect("127.0.0.1", 60003)

	print("Lancement du Serveur HTTP...\n")
	serv_test.run()

	time.sleep(2)
	server_socket.stop_threads = True