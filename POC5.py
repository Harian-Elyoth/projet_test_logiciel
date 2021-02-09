import sqlite3
import string
from string import printable


def create_user(motcle):
    #detection de chiffres
    t = False
    for i in range(len(motcle)):
        t = (motcle[i].isdigit())
        if ( t == True):
            print("votre mot contient un chiffre")
            return False
    #verification de la taille
    if (len(motcle) != 6):
        print("votre mot n'est pas de la bonne taille")
        return False
    elif( motcle == "create"):
        print("C'est exact !")
        return True
    else:
        return False


def connect_user(motcle):
    #detection de chiffres
    t = False
    for i in range(len(motcle)):
        t = (motcle[i].isdigit())
        if ( t == True):
            print("votre mot contient un chiffre")
            return False
    if (len(motcle) != 5):
        print("votre mot n'est pas de la bonne taille")
        return False
    elif motcle == "login" :
        print("C'est exact !")
        return True
    else:
        return False

def exit(motcle):
    #detection de chiffres
    t = False
    for i in range(len(motcle)):
        t = (motcle[i].isdigit())
        if ( t == True):
            print("votre mot contient un chiffre")
            return False
    if (len(motcle) != 4):
        print("votre mot n'est pas de la bonne taille")
        return False
    elif motcle == "exit" :
        print("C'est exact !")
        return True
    else:
        return False


def print_public_room(motcle):
    #detection de chiffres
    t = False
    for i in range(len(motcle)):
        t = (motcle[i].isdigit())
        if ( t == True):
            print("votre mot contient un chiffre")
            return False
    if (len(motcle) != 6):
        print("votre mot n'est pas de la bonne taille")
        return False
    elif motcle == "public" :
        print("C'est exact !")
        return True
    else:
        return False

def print_private_room(motcle):
    #detection de chiffres
    t = False
    for i in range(len(motcle)):
        t = (motcle[i].isdigit())
        if ( t == True):
            print("votre mot contient un chiffre")
            return False
    if (len(motcle) != 7):
        print("votre mot n'est pas de la bonne taille")
        return False
    elif motcle == "private" :
        print("C'est exact !")
        return True
    else:
        return False

def delete_room(motcle):

    # si l'utilisateur a tapé "delete [num_room]" alors la fonction doit renvoyer True
    if (len(motcle) < 8):
        print("votre mot n'est pas de la bonne taille")
        return False
    elif(motcle[0:7] != "delete "):
        return False
    t = False
    for i in range(8,len(motcle)):
        t = (motcle[i].isdigit())
        if ( t == False):
            print("erreur")
            return False
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
    ret5 = False
    ret6 = False
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
    #private
    while(ret5 == False):
        print("Pour afficher une liste de toutes les rooms privees, tapez private")
        s = input()
        ret5 = print_private_room(s)

    #delete
    while(ret6 == False):
        print("Pour supprimer une room, tapez delete [num_room]")
        s = input()
        ret6 = delete_room(s)




if __name__ == '__main__':
    main()
