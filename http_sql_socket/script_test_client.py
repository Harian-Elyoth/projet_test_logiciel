import time

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
		port_nb = 60002

	elif client_nb == "2":
		is_valid = True
		port_nb = 60003

	else:
		print("Commande invalide, veuillez réesayer.\n")
		is_valid = False

print("Creation du websocket...\n")
client_socket = socket_comm("127.0.0.1", port_nb)
client_socket.listen(5)
time.sleep(3)
client_socket.connect("127.0.0.1", 60001)

print("Creation du client HTTP...\n")
client = http_client("127.0.0.1", port_nb, "127.0.0.1", 60000, 5)
header = {"Content-type": "text/plain"}

(error, resp) = client.request('GET', '/', header, '')

if(error == 0):
	if(resp == b'server : OK'):
		print("Le serveur est disponible:\n")
	else:
		print("Le serveur n'est pas disponible.\n")
else:
	print("La requête a échouée, code error : " + str(error) + '\n')

valid_username = False
username = 'Vide'
while (valid_username == False):
	print("Veuillez entrer votre identifiant:\n")
	username = input("> ")
	(error, resp) = client.request('POST', '/username', header, username)

	if(error == 0):
		if(resp == b'username : OK'):
			valid_username = True
		else:
			print("Votre identifiant est incorrect.\n")
	else:
		print("La requête a échouée, code error : " + str(error) + '\n')

valid_password = False
while valid_password == False:
	print("Veuillez entrer votre mots de passe:\n")
	body = input("> ")
	body=body+' '+username
	(error, resp) = client.request('POST', '/password', header, body)

	if(error == 0):
		if(resp == b'password : OK'):
			valid_password = True
		else:
			print("Votre mots de passe est incorrect.\n")
	else:
		print("La requête a échouée, code error : " + str(error) + '\n')

print("\nFélicitation, vous êtes connecté sur le meilleur chat des EISE5 !\n")
print("Veuillez tapez join pour rejoindre un salon, create pour creer un nouveau salon ou bien quit pour fermer l'application :\n")

is_valid 	= False
is_joining 	= False
is_creating = False

## CHOICE ACTION LOOP

while (is_valid == False):

	choice = input("> ")

	if choice == 'quit':
		is_valid = True
		print("\nNous sommes triste de vous voir quittez le meilleur chat des EISE5 !\n")
		exit()

	elif choice == 'join':
		is_valid = True
		
		(error, resp) = client.request('GET', '/room', header, '')

		if(error == 0):
			resp_str = resp.decode("utf-8")
			
			print("Liste des salons disponible :\n\n")
			print(resp_str)

			is_joining = True
		else:
			print("La requête a échouée, code error : " + str(error) + '\n')

	elif choice == 'create':
		is_valid = True

		print("Vous allez maintenant créer un nouveau salon.")
		is_creating = True

	else:
		print("Commande invalide, veuillez réesayer.")
		is_valid = False

## JOIN ROOM CHOICE LOOP
if is_joining == True:

	room_exist == False
	while room_exist == False:

		print("Veuillez taper le nom du salon que vous souhaitez rejoindre.")
		chan = input("> ")

		(error, resp) = client.request('POST', '/room', header, chan)
		if(error == 0):
			if(resp == b'room : OK'):
				print("Le salon " + chan + " est disponible.\n")
				room_exist = True
			else:
				print("Le salon " + chan + " n'est pas disponible ou n'existe pas.\n")
				room_exist = False
		else:
			print("La requête a échouée, code error : " + str(error) + '\n')
			room_exist = False


elif is_creating == True:

	room_create = False
	while room_create == False:

		print("Veuillez taper le nom du salon que vous souhaitez créer.")
		chan = input("> ")

		(error, resp) = client.request('POST', '/create', header, chan)
		if(error == 0):
			if(resp == b'create : OK'):
				print("Le salon " + chan + " est créé.\n")
				room_create= True
			else:
				print("Vous ne pouvez pas créer le salon " + chan + ".\n")
				room_create = False
		else:
			print("La requête a échouée, code error : " + str(error) + '\n')
			room_exist = False

print("Bienvenue sur le salon " + chan + " !")
print("(taper quit pour fermer l'application)\n")

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

