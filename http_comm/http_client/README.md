# Spécification des codes erreurs pour le client HTTP

Fonction __init__ de http_client :

		-> 	0  : Tout s'est bien déroulé 
		-> -1  : L'adresse IP du serveur n'a pas le bon type 
		-> -2  : L'adresse IP du serveur n'a pas le bon format
		-> -3  : Le port du serveur n'a pas le bon type
		-> -4  : Le port du serveur n'est pas entre 0 et 65535
		-> -5  : Le port du serveur est indisponible
		-> -6  : Le timeout du serveur n'a pas le bon type
		-> -7  : Le timeout du serveur n'est pas entre 10 et 60
		-> -8  : L'adresse IP du client n'a pas le bon type 
		-> -9  : L'adresse IP du client n'a pas le bon format
		-> -10 : Le port du client n'a pas le bon type
		-> -11 : Le port du client n'est pas entre 0 et 65535
		-> -12 : Le port du client est indisponible

Fontion connect de http_client :

		->  0 : Tout s'est bien déroulé
		-> -1 : Le client n'a pas réussi à se connecter au serveur

Fonction request de http_client :

		->  0 : Tout s'est bien déroulé
		-> -1  : La methode du serveur n'a pas le bon type 
		-> -2  : La methode du serveur n'est ni GET ni POST
		-> -3  : Le endpoint du serveur n'a pas le bon type
		-> -4  : Le endpoint du serveur n'a pas le bon format (expl : '/login/room')

