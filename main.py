import time
import math
import os

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_S = ["S", "s"]
quitgame = ["Quit", "quit", "quit game", "Quit game", "quit Game", "Quit Game"]
back = ["Back", "back"]
required = ("\nYour current options are A, B, and C\n")
use_back = ("\nYour current options are Back\n")
a_or_b = ("\nYour current options are A, and B\n")
sword = 0

def clear_screen():
    os.system('cls')

def leave():
    clear_screen()
    print("Thanks for playing!")
    os.system('exit')

def menu():
    clear_screen()
    print("\n\n\nText Adventure 1")
    print("\n\n\nA. Start")
    print("B. Stop?")
    print("C. Quit Game")
    print("\nHint: type in save at any time to save & quit your game!")
    choice = input(">>> ")
    if choice in answer_A:
        intro()
    elif choice in answer_B:
        stop()
    elif choice in answer_C:
        leave()
    elif choice in answer_S:
        easter_egg()
    else:
        print (a_or_b)
        menu()
        
def stop():
    clear_screen()
    print("\nYeah... I don't really know either...")
    choice = input(">>> ")
    if choice in back:
        menu()
    else:
        clear_screen()
        print(use_back)
        stop()

def intro():
    clear_screen()
    print("\nA. Live\nB. Die")
    choice = input(">>> ")
    if choice in answer_A:
        option_live()
    elif choice in answer_B:
        lose()
    else:
        clear_screen()
        print (a_or_b)
        intro()




def lose():
    clear_screen()
    print("\nYou died!")
    print("\n\nA. Main Menu \nB. Try Again")
    choice = input(">>> ")
    if choice in answer_A:
        menu()
    elif choice in answer_B:
        intro()
    else:
        print(a_or_b)
        option_die()



def option_live():
    clear_screen()
    print("\n You lived but then you fell into a hole. Your left leg is broken. You can: \nA. Yell all night and day for someone \nB. Try to climb out of the hole")
    choice = input(">>> ")
    if choice in answer_A:
        option_yell()
    elif choice in answer_B:
        option_climb()
    else:
        print(a_or_b)
        option_live



def option_yell():