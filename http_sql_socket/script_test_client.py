import time

from http_client import http_client
from socket_comm import socket_comm

print("Creation du websocket...\n")
client_socket = socket_comm("127.0.0.1", 60001)
client_socket.listen(5)
time.sleep(3)
client_socket.connect("127.0.0.1", 60000)


print("Creation du client HTTP...\n")
client = http_client("127.0.0.1", 65001, "127.0.0.1", 60000, 5)
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
while (valid_username == False):
	print("Veuillez entrer votre identifiant:\n")
	body = input("> ")
	(error, resp) = client.request('POST', '/username', header, body)

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
	(error, resp) = client.request('POST', '/password', header, body)

	if(error == 0):
		if(resp == b'password : OK'):
			valid_password = True
		else:
			print("Votre mots de passe est incorrect.\n")
	else:
		print("La requête a échouée, code error : " + str(error) + '\n')

print("\nFélicitation, vous êtes connecté sur le meilleur chat des EISE5 !\n")
print("Veuillez tapez room pour rejoindre la salon de test ou bien quit pour fermer l'application :\n")

is_valid = False
while (is_valid == False):

	choice = input("> ")

	if choice == 'quit':
		is_valid = True
		print("\nNous sommes triste de vous voir quittez le meilleur chat des EISE5 !\n")
		exit()

	elif choice == 'room':
		is_valid = True
		
		(error, resp) = client.request('GET', '/room', header, '')

		if(error == 0):
			if(resp == b'room : OK'):
				print("Le salon de test est disponible :\n")
			else:
				print("Le salon de test n'est pas disponible.\n")
		else:
			print("La requête a échouée, code error : " + str(error) + '\n')

	else:
		is_valid = False

print("Bienvenue sur le salon de test !\n\n")

while (True):
	print("Veuillez entrer votre message :\n")
	mes = input("> ")

	client_socket.send_message(mes)
	time.sleep(1)




