import unittest
import random
import string

#USER RELATED
from POC5 import create_user
from POC5 import connect_user
from POC5 import exit
#ROOM RELATED
from POC5 import print_public_room
from POC5 import print_private_room
from POC5 import delete_room
from POC5 import create_room
from POC5 import invite_user
#MESSAGE RELATED
from POC5 import send_to_all
from POC5 import send_to

class TestQuickToolsMethods(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_create_user(self):
        # si l'utilisateur a tapé "create" alors la fonction doit renvoyer True
        self.assertTrue(create_user("create"))
        # si l'utilisateur a fait une faute de frappe alors la fonction doit renvoyer False
        self.assertFalse(create_user("crete"))
        # si l'utilisateur a tapé "create" suivi d'un autre mot alors la fonction doit renvoyer False
        self.assertFalse(create_user("create user"))

    def test_connect_user(self):
        #si l'utilisateur a tapé "login" alors la fonction doit renvoyer assertTrue
        self.assertTrue(connect_user("login"))
        # si l'utilisateur a tapé "log" alors la fonction doit renvoyer False
        self.assertFalse(connect_user("log"))
        # si l'utilisateur a tapé "login" suivi d'un autre mot alors la fonction doit renvoyer False
        self.assertFalse(connect_user("login bin"))

    def test_exit(self):
        # si l'utilisateur a tapé "exit" alors la fonction doit renvoyer True
        self.assertTrue(exit("exit"))
        # si l'utilisateur a fait une faute de frappe alors la fonction doit renvoyer False
        self.assertFalse(exit("xit"))
        # si l'utilisateur a tapé "exit" suivi d'un autre mot alors la fonction doit renvoyer False
        self.assertFalse(exit("exit room"))

    def test_print_public_room(self):
        # si l'utilisateur a tapé "public" alors la fonction doit renvoyer True
        self.assertTrue(print_public_room("public"))
        # si l'utilisateur a fait une faute de frappe alors la fonction doit renvoyer False
        self.assertFalse(print_public_room("pblic"))
        # si l'utilisateur a tapé "exit" suivi d'un autre mot alors la fonction doit renvoyer False
        self.assertFalse(print_public_room("public room"))

    def test_print_private_room(self):
        # si l'utilisateur a tapé "private" alors la fonction doit renvoyer True
        self.assertTrue(print_private_room("private"))
        # si l'utilisateur a fait une faute de frappe alors la fonction doit renvoyer False
        self.assertFalse(print_private_room("privat"))
        # si l'utilisateur a tapé "private" suivi d'un autre mot alors la fonction doit renvoyer False
        self.assertFalse(print_private_room("private room"))

    def test_delete_room(self):
        # si l'utilisateur a tapé "delete [num_room]" alors la fonction doit renvoyer True
        self.assertTrue(delete_room("delete 5"))
        # si l'utilisateur a tapé "delete" seulement alors la fonction doit renvoyer False
        self.assertFalse(delete_room("delete"))
        # si l'utilisateur a fait une faute de frappe alors la fonction doit renvoyer False
        self.assertFalse(delete_room("delte"))

    def test_create_room(self):
        # si l'utilisateur a tapé "room" alors la fonction doit renvoyer True
        self.assertTrue(create_room("room"))
        # si l'utilisateur a fait une faute de frappe alors la fonction doit renvoyer False
        self.assertFalse(create_room("rome"))
        # si l'utilisateur a rajouté un argument alors la fonction doit renvoyer False
        self.assertFalse(create_room("room 2"))

    def test_invite_user(self):
        # si l'utilisateur a tapé "invite [other_user_name] [num_room]" alors la fonction doit renvoyer True
        self.assertTrue(invite_user("invite other_user_name 0"))
        # si l'utilisateur a fait une faute de frappe alors la fonction doit renvoyer False
        self.assertFalse(invite_user("invite simon5"))
        #si l'utilisateur inverse l'ordre des arguments :
        self.assertFalse(invite_user("invite 5 other_user_name"))
        #si l'utilisateur oublie un argument alors la fonction doit renvoyer False
        self.assertFalse(invite_user("invite other_user_name"))
        self.assertFalse(invite_user("invite 5"))

    def test_send_to_all(self):
        # si l'utilisateur a tapé "sendtoall" alors la fonction doit renvoyer True
        self.assertTrue(send_to_all("sendtoall"))
        # si l'utilisateur a rajouté un argument alors la fonction doit renvoyer False
        self.assertFalse(send_to_all("sendtoall 5"))
        # si l'utilisateur a fait une faute de frappe alors la fonction doit renvoyer False
        self.assertFalse(send_to_all("send to all"))
        # si l'utilisateur a confondu deux fonctions alors la fonction doit renvoyer False
        self.assertFalse(send_to_all("sendto other_user_name"))

    def test_send_to(self):
        # si l'utilisateur a tapé "sendto [other user name]" alors la fonction doit renvoyer True
        self.assertTrue(send_to("sendto other_user_name"))
        # si l'utilisateur a oublié un argument alors la fonction doit renvoyer False
        self.assertFalse(send_to_all("sendto"))
        # si l'utilisateur a fait une faute de frappe alors la fonction doit renvoyer False
        self.assertFalse(send_to_all("send to "))
        # si l'utilisateur a confondu deux fonctions alors la fonction doit renvoyer False
        self.assertFalse(send_to_all("sendtoall other_user_name"))
