import sqlite3
import string
from string import printable


def create_user(motcle):
    if (len(motcle) != 6):
        print("votre mot n'est pas de la bonne taille")
        return False
    elif ( isinstance(motcle, str) == False  ):
        print("votre mot cle n'est pas un string")
        return False
    elif motcle == "create" :
        print("C'est exact !")
        return True
    else:
        return False


def connect_user(motcle):
    if (len(motcle) != 5):
        print("votre mot n'est pas de la bonne taille")
        return False
    elif ( isinstance(motcle, str) == False ):
        print("votre mot cle n'est pas un string")
        return False
    elif motcle == "login" :
        print("C'est exact !")
        return True
    else:
        return False

def exit(motcle):
    return True

def print_public_room(motcle):
    return True

def print_private_room(motcle):
    return True

def delete_room(motcle):
    return True

def create_room(motcle):
    return True

def invite_user(motcle):
    return True

def send_to_all(motcle):
    return True

def send_to(motcle):
    return True


def main():
    print("################################")
    print("         Bienvenue              ")
    print("################################")
    print("")
    #create user
    ret = False
    ret2 = False
    while(ret == False):
        print("Pour creer un user, tapez create")
        s = input()
        ret = create_user(s)

    while(ret2 == False):
        print("Pour se logger, tapez login")
        s = input()
        ret2 = connect_user(s)

if __name__ == '__main__':
    main()
