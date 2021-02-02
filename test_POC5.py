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
