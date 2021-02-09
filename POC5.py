import sqlite3
import string
from string import printable


def create_user(motcle):
    if (len(motcle) != 6):
        print("votre mot n'est pas de la bonne taille")
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
    elif motcle == "login" :
        print("C'est exact !")
        return True
    else:
        return False

def exit(motcle):
    if (len(motcle) != 4):
        print("votre mot n'est pas de la bonne taille")
        return False
    elif motcle == "exit" :
        print("C'est exact !")
        return True
    else:
        return False


def print_public_room(motcle):
    if (len(motcle) != 6):
        print("votre mot n'est pas de la bonne taille")
        return False
    elif motcle == "public" :
        print("C'est exact !")
        return True
    else:
        return False

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

    ret = False
    ret2 = False
    ret3 = False
    ret4 = False
    #create user
    while(ret == False):
        print("Pour creer un user, tapez create")
        s = input()
        ret = create_user(s)
    #log
    while(ret2 == False):
        print("Pour se logger, tapez login")
        s = input()
        ret2 = connect_user(s)

    #exit
    while(ret3 == False):
        print("Pour sortir, tapez exit")
        s = input()
        ret3 = exit(s)
    #public
    while(ret4 == False):
        print("Pour afficher une liste de toutes les rooms publiques, tapez public")
        s = input()
        ret4 = print_public_room(s)

if __name__ == '__main__':
    main()
