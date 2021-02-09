import sqlite3
import string
from string import printable


def create_user(motcle):
    if (len(motcle) != 6):
        return False
    elif ( isinstance(motcle, str) == False  ):
        return False
    elif motcle == "create" :
        return True
    else:
        return False


def connect_user(motcle):
    return True

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
    print("Pour creer un user, tapez create")
    s = input()
    print(s)
    print(create_user(s))

if __name__ == '__main__':
    main()
