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
    # si l'utilisateur a tapé "room" alors la fonction doit renvoyer True

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
    elif motcle == "room" :
        print("C'est exact !")
        return True
    else:
        return False


def invite_user(motcle):
    # si l'utilisateur a tapé "invite [other_user_name] [num_room]" alors la fonction doit renvoyer True
    if (len(motcle) < 8):
        print("votre mot n'est pas de la bonne taille")
        return False

    #split du mot cle en fonction des separateurs
    list_termes = motcle.split(' ')
    if (len(list_termes) < 3):
        print("vous n'avez pas rentré assez de termes")
        return False

    invite = list_termes[0]
    user_name = list_termes[1]
    num_room = list_termes[2]
    print("invite : ")
    print(invite)
    print("USER NAME : ")
    print(user_name)
    print("len de user name:")
    print(len(user_name))
    print("num room : ")
    print(num_room)

    if(invite != "invite"):
        print("le mot cle 'invite' a mal été orthographié")
        return False

    elif (len(user_name) == 0): # pas de user name
        print("user name invalide")
        return False

    t = False
    for i in range(len(num_room)):
        t = (num_room[i].isdigit())
        if ( t == False):
            print("num room invalide")
            return False
    return True


def send_to_all(motcle):
    # si l'utilisateur a tapé "sendtoall" alors la fonction doit renvoyer True
    #detection de chiffres
    t = False
    for i in range(len(motcle)):
        t = (motcle[i].isdigit())
        if ( t == True):
            print("votre mot contient un chiffre")
            return False
    if (len(motcle) != 9):
        print("votre mot n'est pas de la bonne taille")
        return False
    elif motcle == "sendtoall" :
        print("C'est exact !")
        return True
    else:
        return False

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
    ret7 = False
    ret8 = False
    ret9 = False
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
    #room
    while(ret7 == False):
        print("Pour ajouter une room, tapez room")
        s = input()
        ret7 = create_room(s)
    #invite_user
    while(ret8 == False):
        print("Pour inviter un autre user à rejoindre une room, tapez invite [user_name] [num_room]")
        s = input()
        ret8 = invite_user(s)
    #send_to_all
    while (ret9 == False):
        print("Pour envoyer un message à l'ensemble des utilisateurs, tapez sendtoall")
        s = input()
        ret9 = send_to_all(s)


if __name__ == '__main__':
    main()
