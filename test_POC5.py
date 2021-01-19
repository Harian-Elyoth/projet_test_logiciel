import unittest
from POC5 import create_user
import random
import string


class TestQuickToolsMethods(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_create_user(self):
        # si l'utilisateur a tapé "create" alors la fonction doit renvoyer True
        self.assertTrue(create_user("create"))
        # si l'utilisateur a tapé "crete" alors la fonction doit renvoyer False
        self.assertFalse(create_user("crete"))
        # si l'utilisateur a tapé "create" suivi d'un autre mot alors la fonction doit renvoyer False
        self.assertFalse(create_user("create user"))
