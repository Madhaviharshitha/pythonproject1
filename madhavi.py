balance=0
def deposit():
    global balance
    amount=int(input("Enter amount"))
    balance=balance+amount

def withdraw():
    global balance
    amount=int(input("Enter amount"))
    balance=balance-amount

def balcheck():
    global balance
    print('available balance', balance)

def menu():
    print('1.Deposit\n 2.withdraw\n 3.Balance')
    ch=int(input("Enter your choice"))
    if ch==1:
        deposit()
    elif ch==2:
        withdraw()
    elif ch==3:
        balcheck()
from colorama import Fore,Back,Style
def welcome():
    print(Fore.BLUE+"Welcome to MGC ATM")
    pin=int(input("Enter your ATM pin number"))
    if pin==123:
        menu()
    else:
        print("Invalid pin number")
        welcome()
welcome()

