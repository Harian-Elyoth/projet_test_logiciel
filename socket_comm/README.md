# Spécification des codes erreurs pour la communication par socket

## Premier delivrable

Branche contenant le premier delivrable pour le communication par socket bi-directionnelle pour une connection unique. 

Fonction __new__ de socket_comm :

		-> -1  : L'adresse IP n'a pas le bon type
		-> -2  : L'adresse IP n'a pas le bon format
		-> -3  : Le port n'a pas le bon type
		-> -4  : Le port n'est pas entre 0 et 65535
		-> -5  : Le port est indisponible

Fonction listen de socket_comm :
		->  0  : Tout s'est bien déroulé
		-> -1  : Le backlog n'a pas le bon format
		-> -2  : Le port est indisponible

Fonction connect de socket_comm :
		->  0  : Tout s'est bien déroulé
		-> -1  : L'adresse IP n'a pas le bon type
		-> -2  : L'adresse IP n'a pas le bon format
		-> -3  : Le port n'a pas le bon type
		-> -4  : Le port n'est pas entre 0 et 65535
		-> -5  : Le port est indisponible
		-> -6  : Le serveur n'est pas accesible
