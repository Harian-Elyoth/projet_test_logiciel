import time, os

from http_client import http_client
from socket_comm import socket_comm

print("Vous avez lancé la beta du meilleur chat des EISE5 !\n")
print("Veuillez entrer 1 si vous êtes le 1er client et 2 si vous êtes le 2nd client\n")

port_nb = 0
is_valid = False
while is_valid == False:

	client_nb = input("> ")
	if client_nb == "1":
		is_valid = True
		port_list = 50000
		port_conn = 60000

	elif client_nb == "2":
		is_valid = True
		port_list = 50001
		port_conn = 60001

	else:
		print("Commande invalide, veuillez réesayer.\n")
		is_valid = False

print("Creation du websocket...\n")
client_socket = socket_comm()
print(client_socket.listen("127.0.0.1", port_list, 5))
time.sleep(5)
print(client_socket.connect("127.0.0.1", port_conn))

print("\nVeuillez entrer votre message :")

while (True):
	print('\n')
	mes = input("> ")

	if mes == "quit":
		print("\nNous sommes triste de vous voir quittez le meilleur chat des EISE5 !\n")
		client_socket.stop_threads = True
		time.sleep(2)
		exit()

	client_socket.send_message(mes)
	time.sleep(1)

command = 'kill -9 $(lsof -t -i tcp:50000)'
os.system(command)
command = 'kill -9 $(lsof -t -i tcp:50001)'
os.system(command)
