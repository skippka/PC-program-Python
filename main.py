import random
import time
from colorama import Fore, Back, Style, init




class PREFIX:
    CORRECT_PREFIX = Fore.GREEN + "[i] - " + Style.RESET_ALL
    INFO_PREFIX = Fore.BLUE + "[i] - " + Style.RESET_ALL
    WARN_PREFIX = Fore.YELLOW + "[i] - " + Style.RESET_ALL
    ERROR_PREFIX = Fore.RED + "[i] - " + Style.RESET_ALL


def show_current_time():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(PREFIX.INFO_PREFIX + 'Time now: ' + current_time)
    return current_time

def random_greeting():
    greeting = random.choice(
        [ "Welcome back!",
          "Hello, nice to see you!",
          "Greetings, User!",
          "Hi there! How can I assist you today?",
          "Hello! Ready to get started?"
          ]
    )
    print(greeting)


commands = ['help', 'info', 'view_passwords', 'return']

def access_prot_func():
    password_prot_func = input(PREFIX.INFO_PREFIX + "Enter your password to access your protected resources: ")


    if password_prot_func == "qwerty123":
        print(PREFIX.CORRECT_PREFIX + "Access granted!")
        time.sleep(3)

    while True:
        print(Fore.RED + "###########################################")
        print(Fore.RED + "##                                       ##")
        print(Fore.RED + "##    ###############################    ##")
        print(Fore.RED + "##    ##                           ##    ##")
        print(Fore.RED + "##    ##     Protected Resources   ##    ##")
        print(Fore.RED + "##    ##                           ##    ##")
        print(Fore.RED + "##    ##   1. View commands        ##    ##")
        print(Fore.RED + "##    ##   2. Edit secure data     ##    ##")
        print(Fore.RED + "##    ##   3. Enter commands       ##    ##")
        print(Fore.RED + "##    ##   4. Return               ##    ##")
        print(Fore.RED + "##    ##                           ##    ##")
        print(Fore.RED + "##    ###############################    ##")
        print(Fore.RED + "##                                       ##")
        print(Fore.RED + "###########################################")
        print(Fore.RED + "###########################################")
        print(Fore.RED + "##       Keyboard                ##      ##")
        print(Fore.RED + "##   ____________________________##      ##")
        print(Fore.RED + "##  |  |  |  |  |  |  |  |  |  |  |      ##")
        print(Fore.RED + "##  |__|__|__|__|__|__|__|__|__|__|      ##")
        print(Fore.RED + "##  [_____________________________]      ##")
        print(Fore.RED + "###########################################")

        choise = input("Choose an option: ")

        if choise == "1":
            print(" ")
            print("All comands available:")
            print(commands)
            print(" ")
            return
        elif choise == "2":
            print("Edit secure data")
        elif choise == "3":
            commands_entered = input("Enter command: ")
            if commands_entered == "help":
                print("This a program PC in python code")
            elif commands_entered == "info":
                print("PC Information ")
            elif commands_entered == "view_password":
                print("Command avalaible: "+ commands)
            elif commands_entered == "return":
                main()
        elif choise == "4":
            main()
        else:
            print("Invalid choise variant")



    else:
        print(PREFIX.ERROR_PREFIX + "Access denied!")


def main_computer_if_protected_resources():

    global password_prot_func


def main():

    password = input("Enter your password: ")

    correct_password = "qwerty"

    if password == correct_password:
        print("Login to system...")
        time.sleep(3)
        print(PREFIX.CORRECT_PREFIX + "Login successful!")
        print("Hello PC user")
        is_running = True
    else:
        print(PREFIX.ERROR_PREFIX + "Wrong password")
        again = input("Do you want to try again? (Y/N)")
        if again == "Y":
            main()
        else:
            is_running = False

        is_running = False

    while is_running:

        init(autoreset=True)

        print(Fore.GREEN + "###########################################")
        print(Fore.GREEN + "##                                       ##")
        print(Fore.GREEN + "##    ###############################    ##")
        print(Fore.GREEN + "##    ##                           ##    ##")
        print(Fore.GREEN + "##    ##       Python Computer     ##    ##")
        print(Fore.GREEN + "##    ##                           ##    ##")
        print(Fore.GREEN + "##    ##   1. Show current time    ##    ##")
        print(Fore.GREEN + "##    ##   2. Random greeting      ##    ##")
        print(Fore.GREEN + "##    ##   3. Access protected     ##    ##")
        print(Fore.GREEN + "##    ##      function             ##    ##")
        print(Fore.GREEN + "##    ##   4. Exit                 ##    ##")
        print(Fore.GREEN + "##    ##                           ##    ##")
        print(Fore.GREEN + "##    ###############################    ##")
        print(Fore.GREEN + "##                                       ##")
        print(Fore.GREEN + "###########################################")
        print(Fore.GREEN + "###########################################")
        print(Fore.GREEN + "##       Keyboard                ##      ##")
        print(Fore.GREEN + "##   ____________________________##      ##")
        print(Fore.GREEN + "##  |  |  |  |  |  |  |  |  |  |  |      ##")
        print(Fore.GREEN + "##  |__|__|__|__|__|__|__|__|__|__|      ##")
        print(Fore.GREEN + "##  [_____________________________]      ##")
        print(Fore.GREEN + "###########################################")

        choice = input("Enter your choice: ")
        if choice == "1":
            show_current_time()
        elif choice == "2":
            random_greeting()
        elif choice == "3":
            access_prot_func()
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choise variant")

if __name__ == "__main__":
    main()



