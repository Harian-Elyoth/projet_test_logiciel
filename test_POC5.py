import unittest
import random
import string

#USER RELATED
from POC5 import create_user
from POC5 import connect_user
from POC5 import exit
#ROOM RELATED
from POC5 import print_public_room
from POC5 import print_public_room



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
        self.assertTrue(create_user("login"))
        # si l'utilisateur a tapé "log" alors la fonction doit renvoyer False
        self.assertFalse(create_user("log"))
        # si l'utilisateur a tapé "login" suivi d'un autre mot alors la fonction doit renvoyer False
        self.assertFalse(create_user("login bin"))

    def test_exit(self):
        # si l'utilisateur a tapé "exit" alors la fonction doit renvoyer True
        self.assertTrue(exit("exit"))
        # si l'utilisateur a fait une faute de frappe alors la fonction doit renvoyer False
        self.assertFalse(exit("xit"))
        # si l'utilisateur a tapé "exit" suivi d'un autre mot alors la fonction doit renvoyer False
        self.assertFalse(exit("exit room"))

        
