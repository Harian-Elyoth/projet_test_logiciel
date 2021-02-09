from http_client import http_client

client = http_client("127.0.0.1", 65500, "127.0.0.1", 60000, 5)
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
	body = input("Veuillez entrer votre identifiant:\n")
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
	body = input("Veuillez entrer votre mots de passe:\n")
	(error, resp) = client.request('POST', '/password', header, body)

	if(error == 0):
		if(resp == b'password : OK'):
			valid_password = True
		else:
			print("Votre mots de passe est incorrect.\n")
	else:
		print("La requête a échouée, code error : " + str(error) + '\n')

print("Félicitation, vous êtes connecté sur le meilleur chat des EISE5!\n")
