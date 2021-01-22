# Spécification des codes erreurs pour le serveur HTTP

Fonction __init__ de http_serveur :

		-> 	0  : Tout s'est bien déroulé 
		-> -1  : L'adresse IP n'a pas le bon type 
		-> -2  : L'adresse IP n'a pas le bon format
		-> -3  : Le port n'a pas le bon type
		-> -4  : Le port n'est pas entre 0 et 65535
		-> -5  : Le port est indisponible

Fontion do_GET de http_client :

		->  0 : Tout s'est bien déroulé
		-> -1 : Le GET a échoué

Fonction do_POST de http_client :

		->  0  : Tout s'est bien déroulé
		-> -1  : Le POST a échoué

