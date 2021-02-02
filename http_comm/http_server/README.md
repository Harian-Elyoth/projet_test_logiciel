# Spécification des codes erreurs pour le serveur HTTP

Fonction __new__ de http_server :

		-> 	0  : Tout s'est bien déroulé 
		-> -1  : L'adresse IP n'a pas le bon type 
		-> -2  : L'adresse IP n'a pas le bon format
		-> -3  : Le port n'a pas le bon type
		-> -4  : Le port n'est pas entre 0 et 65535
		-> -5  : Le port est indisponible

Fontion do_GET de handler_http_serv :

		->  0 : Le endpoint est correct
		-> -1 : Le endpoint est incorrect

Fonction do_POST de handler_http_serv :

		->  0 : Le endpoint est correct
		-> -1 : Le endpoint est incorrect

