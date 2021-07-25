import time


def welcome(bot_name, birth_year):
    print(f"Hey! My name is {bot_name}.")
    print("I was created in " + birth_year + ".")

def prompt_name():
    print("Please, remind me your name.")
    name = input("> ")
    print("What a great name you have, " + name + "!")

def reckon_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    rem3 = int(input("> "))
    rem5 = int(input("> "))
    rem7 = int(input("> "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"Your age is {str(age)}: that's a good time to start programming!!")

def count():
    print("Now I will prove to you that I can count to any number you want.")
    num = int(input("> "))
    i = 0
    while i <= num:
        print(i, "!")
        i += 1

def exam():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    while True:
        choice = int(input("> "))
        if choice == 2:
            print("Completed, u rock!")
            break
        else:
            print("Please, try again.")

def bye():
    print("""
Congratulations, have a nice day!



            Made With <3 By Ayman (SpyHimself)
""")


welcome("Osa", "2021")
prompt_name()
reckon_age()
count()
time.sleep(1)
exam()
bye()
