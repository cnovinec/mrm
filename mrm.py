# mount rowan mystery code for Novtronics TTD4092
# started 10DEC2023
# main program for MRM terminal

# list of items to inport for the program
import cmd
import csv
import textwrap
import sys
import time
import datetime
import os
import random
from tqdm import tqdm
from easteregg import car_print


screen_width = 100

class user:
    def __init__(user):
        user.name = ''
        user.current_question = 0
        user.total_questions = 4
        user.row = 0
        user.answer = ''
        user.current_quetion_field = ""
        user.key = ''
        user.current_time = ''
        user.random_no = 0
        user.countdown_complete = False
        user.first_time = True
        user.game_over = False
myuser = user()

# Title screen
def title_screen_functions():
    option = input('>')
    if option.lower() == ('login'):
        user_login()
        setup_TTD()
    elif option.lower() == ('create user'):
        create_user()
        os.system('clear')
        main_screen()
    elif option.lower() == ('.admin!!'):
        admin_check()
    elif option.lower() == ('shutdown'):
        shutdown()
    elif option.lower() == ('.exit!!'):
        myuser.game_over = True
        exit_program()


    while option.lower() not in ['login', 'create user', '.admin!!', 'shutdown', '.exit!!']:
        print('Incorrect input please enter login or create user')
        option = input('>')
        if option.lower() == ('login'):
            user_login()
            setup_TTD()
        elif option.lower() == ('create user'):
            create_user()
            os.system('clear')
            main_screen()
        elif option.lower() == ('.admin!!'):
            admin_check()
        elif option.lower() == ('shutdown'):
            shutdown()
        elif option.lower() == ('.exit!!'):
            myuser.game_over = True
            exit_program()

# user options to call from anywhere
def user_options():
    if myuser.answer.lower() == '.admin!!':
        admin_check()
    elif myuser.answer.lower() == 'logout':
        main_screen()
    elif myuser.answer.lower() == 'shutdown':
        shutdown()
    elif str(myuser.answer) == '.exit!!':
        myuser.game_over = True
        main_screen()
        exit_program()

# Login function
def user_login():
    for try_user_pw in range(3):
            # asks for user converts to lower to ensure always match
            username = input("Username: ").lower()
            password = input("Password: ")
            found = False

            # checks for input from user
            if username == '' or password == '':
                print('No username or password entered try again.')
                trys_left = 2 - try_user_pw

                # if for loop runs and user and passport does not match print error message and go back to main screen
                if trys_left == 0:
                    print("You have not entered the correct username or password.")
                    print("You will now be taken to the main screen.")
                    time.sleep(4.0)
                    main_screen()

                print(f'{trys_left} attempts remaining.')

            else:
                # open csv and performs task
                with open('u-p.csv', 'r') as file_check:
                    reader = csv.reader(file_check)
                    next(reader, None)


                    for row in reader:
                        # checks every row in the csv for a exact match for 'username' and 'password'
                        if row[0] == username and row[1] == password:
                            # states user and pw added to dict
                            print('Access Granted')
                            print('Press ENTER key to continue . . .', end="")
                            input()
                            myuser.name = username
                            load_user_save_data()
                            found = True

                    # if user name and password match not present return error message
                    if found == False:
                        print('Incorrect User Name or Password Please Try again.')
                        trys_left = 2 - try_user_pw
                        print(f'{trys_left} attempts remaining.')

                        # if for loop runs and user and passport does not match print error message and go back to main screen
                        if trys_left == 0:
                            print("You have not entered the correct username or password.")
                            print("You will now be taken to the main screen.")
                            time.sleep(4.0)
                            main_screen()

            # if un & pw found break for loop
            if found == True:
                break

# Create user function
def create_user():
    test_user_pass_input = False
    print("Please create an account")

    while test_user_pass_input != True:
        # amend u-p to add user and pword if no account was found
        username = input("Username: ").lower()
        password = input("Password: ")
        valid_user = False
        user_exists = False
        pass_check = False

        while pass_check == False:
            # checks to see if username or password have been entered
            if username == '' or password == '':
                print('No username or password entered try again.')
                pass_check = True

            elif username == 'doc':
                print("Hey thats my account you cant use that!")
                pass_check = True

            elif test_user_pass_input == False:
                with open('u-p.csv', 'r') as file_check:
                    reader = csv.reader(file_check)
                    next(reader, None)

                    for row in reader:
                        # checks every row in the csv for a exact match for 'username' and 'password'
                        if row[0] == username:
                            # states user and pw added to dict
                            print('User already exists. Please choose another username')
                            user_exists = True
                            pass_check = True

                    if user_exists == False:
                        valid_user = True
                        pass_check = True

                if valid_user == True:
                    test_user_pass_input = True

        if test_user_pass_input == True:
            # opens file and amends then closes
            with open("u-p.csv", "a") as file_update:

                writer = csv.DictWriter(file_update, fieldnames=["username","password"])
                writer.writerow({"username": username, "password": password})

            myuser.name = username
            create_user_save_data()
            # states user and pw added to dict
            print('Username and Password successfully created')
            print('Press ENTER key to continue . . .', end="")
            input()

# admin function to check all users and their progress
def admin_check():
    # open csv and performs task
    print('User names and passwords')
    with open('u-p.csv', 'r') as file_check:
        reader = csv.reader(file_check)
        next(reader, None)

        for row in reader:
            print(row)

    print()
    print('User save data')
    with open('user_save_data.csv', 'r') as file_check:
        reader = csv.reader(file_check)
        next(reader, None)

        for row in reader:
            print(row)

    print()
    print('Admin access pannel')
    print('Press ENTER key to continue . . .', end="")
    input()
    main_screen()

# creates user save data row
def create_user_save_data():
    user_row = -1
    with open('user_save_data.csv', 'r') as file_check:
        reader = csv.reader(file_check)

        # checks for total users and updates myuser.row
        for row in reader:
            user_row += 1

            if row[1] == myuser.name:
                # set myuser.row
                myuser.row = user_row
                break

        myuser.row = user_row

    with open("user_save_data.csv", "a") as file_update:
        writer = csv.DictWriter(file_update, fieldnames=["user_row","username","current_question","countdown_complete","answer0","answer1","answer2","answer3"])
        writer.writerow({"user_row": myuser.row,"username": myuser.name,"current_question": 0, "countdown_complete": False})

# load user save data
def load_user_save_data():
    with open('user_save_data.csv', 'r') as file_check:
        reader = csv.reader(file_check)
        next(reader, None)

        for row in reader:
            if row[1] == myuser.name:
                myuser.row = int(row[0])
                myuser.current_question = int(row[2])
                myuser.countdown_complete = row[3]
                if myuser.countdown_complete == 'False':
                    myuser.countdown_complete = False
                else:
                    myuser.countdown_complete = True

# update user save data
def user_save_data():
    field_names = ["user_row","username","current_question","countdown_complete","answer0","answer1","answer2","answer3"]

    user_save_data_temp = {}

    with open('user_save_data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        user_save_data_temp = [row for row in csv_reader]
        # print print(user_save_data_temp)

    #print(user_save_data_temp[myuser.row])
    myuser.current_quetion_field = field_names[myuser.current_question + 4]
    user_save_data_temp[myuser.row].update({myuser.current_quetion_field: myuser.answer})
    myuser.current_question += 1
    user_save_data_temp[myuser.row].update({"current_question": myuser.current_question})
    #print(user_save_data_temp[myuser.row])
    #input()

    with open('user_save_data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(user_save_data_temp)

    # Delete when completed as used for only testing perposes
    #with open('user_save_data.csv', 'r') as file_check:
        #reader = csv.reader(file_check)

        #for row in reader:
            #print(row)

    #print('Answer succesfully added')
    #print('Press ENTER key to continue . . .', end="")
    #input()

#print current quesiton
def print_current_question():
    with open('mrmquestions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if int(row[0]) == myuser.current_question:
                print(f'Q{myuser.current_question + 1}: ', end='')
                print(row[1])

#check answer that has been entered for a match with the current question the user is up too.
def check_answer():
    with open('mrmquestions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        answer_found = False

        for row in reader:
            #print(row)
            if int(row[0]) == myuser.current_question and row[2] == myuser.answer:
                answer_found = True
                print_key()
                print('Correct, your next question will now be loaded.')
                print('Please copy down your key it will be useful.')
                print('Your key is:', myuser.key)
                print('Press ENTER key to continue . . .', end="")
                input()
                user_save_data()
                os.system('clear')
                break

        if answer_found == False:
            wrong_answer_random()

# initalizing screen for TTD4092
def int_screen():
    os.system('clear')
    splash_screen()
    time.sleep(3)
    os.system('clear')
    print('##########################################################################')
    print('#                      Loading version 8.4.21                            #')
    print('##########################################################################')
    print('#                           Please wait                                  #')
    print('#                                                                        #')
    print('##########################################################################')
    time.sleep(5)
    main_screen()

def splash_screen():
    print(r"""
  _   _            _                   _
 | \ | |          | |                 (_)
 |  \| | _____   _| |_ _ __ ___  _ __  _  ___ ___
 | . ` |/ _ \ \ / / __| '__/ _ \| '_ \| |/ __/ __|
 | |\  | (_) \ V /| |_| | | (_) | | | | | (__\__ \
 |_| \_|\___/_\_/_ \__|_|  \___/|_| |_|_|\___|___/
            / ____|
           | |     ___  _ __ _ __
           | |    / _ \| '__| '_ \
           | |___| (_) | |  | |_) |
            \_____\___/|_|  | .__/
                            | |
                            |_|
#######################################################
#                     TTD4092                         #
#                  Copyright 2023                     #
#   Created by Head Programmer and CEO Mr Novinec     #
####################################################### """)

# create main screen for TTD4092
def main_screen():
    if myuser.game_over == True:
        exit_program()
    else:
        os.system('clear')
        print('##########################################################################')
        print('#                  Welcome to the Novtronics TTD4092                     #')
        print('##########################################################################')
        print('#                            - Login -                                   #')
        print('#                         - Create User -                                #')
        print('##########################################################################')
        print('Please type your option below.')
        title_screen_functions()

# questions and answer prompt screen showing current % tracking bar
def prompt():
    if myuser.current_question == myuser.total_questions:
        if myuser.countdown_complete == True:
            ttd_completion_screen()

        elif myuser.countdown_complete == False:
            countdown()

    else:
        current_percent = round(myuser.current_question / myuser.total_questions * 100)
        print("=================================================================")
        print('TTD4092 Calibration completion level')
        for i in range(myuser.current_question):
            print('-', end='')
        print(f"{current_percent}%")
        print("=================================================================")
        print_current_question()
        print('Type your answer below')
        answer = input('>')
        myuser.answer = answer.lower()

        # safety exit for me to fix any issues that might be found while program is running
        if answer.lower() == '.exit!!':
            myuser.game_over = True
            exit_program()
        elif answer.lower() == '.admin!!':
            admin_check()
        elif answer.lower() == 'logout':
            main_screen()
        elif answer.lower() == 'show keys':
            print_all_keys()
        # easter egg from back to the future
        elif answer.lower().strip() == '88 miles per hour':
            print("PUT EASTER EGG HERE")
            car_print()
            time.sleep(5)
            os.system('clear')
        elif answer.lower() == 'shutdown':
            shutdown()
        elif answer.lower().strip() != '.exit!!':
            check_answer()


# wrong answer to question print random incorrect message
def wrong_answer_random():
    # remember to change range if wrong answers change
    myuser.random_no = random.randint(0,116)

    #opens wrong answer file and using random int selects to print chosen line
    with open('rand_wrong.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if int(row[0]) == myuser.random_no:
                print(row[1])

    print('Press ENTER key to continue . . .', end="")
    input()
    os.system('clear')

# print key or next question clue hint
def print_key():
    with open('mrmquestions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if int(row[0]) == myuser.current_question:
                myuser.key = str(row[3])

# prints all users keys they have completed
def print_all_keys():
    with open('mrmquestions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if int(row[0]) == myuser.current_question:
                break

            elif int(row[0]) < myuser.current_question:
                print(f'Q{int(row[0]) + 1} key: ', end='')
                print(row[3])

        print('Press ENTER key to continue . . .', end="")
        input()
        os.system('clear')

# when all answer complete play count down timer giving 30 mins to get the right key from head of game
def countdown():
    # Initializing a date and time
    date_and_time = datetime.datetime.today()
    print("Original time:")
    print(date_and_time.strftime('%H:%M:%S'))

    # Calling the timedelta() function
    time_change = datetime.timedelta(minutes=30)
    myuser.current_time = date_and_time + time_change

    # Printing the new datetime object
    print("Changed time:")
    print(myuser.current_time.strftime('%H:%M:%S'))

    while myuser.answer != 'answer1':
        os.system('clear')
        new_date_time = datetime.datetime.today()
        time_rem = myuser.current_time - new_date_time

        # Extracting hours, minutes, and seconds from the timedelta object
        hours, remainder = divmod(time_rem.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Printing the time remaining in the desired format
        print('Calibration complete you now have 30 mins to enter the final passcode')
        print("Time remaining: {:02}:{:02}:{:02}".format(hours, minutes, seconds))
        print('Passcode: ', end='')
        myuser.answer = input('>').lower()

    os.system('clear')
    myuser.countdown_complete = True
    update_user_countdown()

# updates user countdown_complete
def update_user_countdown():
    field_names = ["user_row","username","current_question","countdown_complete","answer0","answer1","answer2","answer3"]

    user_save_data_temp = {}

    with open('user_save_data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        user_save_data_temp = [row for row in csv_reader]
        # print print(user_save_data_temp)

    user_save_data_temp[myuser.row].update({"countdown_complete": myuser.countdown_complete})

    # re-writes user data
    with open('user_save_data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(user_save_data_temp)

# takes user to the TTD screen for them to use to teleport to differnet times
def ttd_completion_screen():
    is_int = False
    if myuser.first_time == True:
        myuser.current_time = datetime.datetime.today().year

        while is_int == False:
            print('This is now your device to travel to any year you wish be carefull on what you do there though')
            print('Your current year is: ', end='')
            print(myuser.current_time)
            print('Enter new time destination:')
            myuser.answer = input('>')
            if myuser.answer in ['logout', '.admin!!', 'shutdown', '.exit!!']:
                user_options()

            elif myuser.answer.isnumeric():
                is_int = True
                break

            else:
                print('Please enter digit!')
                time.sleep(2)
                os.system('clear')

        myuser.first_time = False

    elif myuser.first_time == False:
        while is_int == False:
            print('Your current year is: ', end='')
            print(myuser.current_time)
            print('Enter new time destination:')
            myuser.answer = input('>')
            if myuser.answer in ['logout', '.admin!!', 'shutdown', '.exit!!']:
                user_options()
            elif myuser.answer.isnumeric():
                is_int == True
                break

            else:
                print('Please enter digit!')
                time.sleep(2)
                os.system('clear')

    statment1 = "Hold on to your butts!"
    for character in statment1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

    time.sleep(2)
    print()
    with tqdm(total=50, bar_format="{l_bar}{bar:100}") as pbar:
        for i in range(50):
            time.sleep(0.1)
            pbar.update(1)
    myuser.current_time = myuser.answer

    os.system('clear')
    prompt()

# system exit function
def exit_program():
    myuser.game_over = True
    os.system('clear')
    sys.exit(0)

# shutdown function do I want to add one to the program
def shutdown():
    os.system('clear')
    print('##################################################################')
    print('##################################################################')
    print(' Shutdown sequence initiated please wait for device to power off. ')
    print('##################################################################')
    print('##################################################################')
    time.sleep(3)
    os.system('shutdown -h now')
    time.sleep(4)

# mrm function
def start_game():
    return

# main game loop which continually prompts user unless .game_over == True
def main_loop():
    while myuser.game_over == False:
        prompt()

# shows user the first message from doc while their .question_number is 0
def setup_TTD():
    if myuser.current_question == 0:
        os.system('clear')
        print('Subject: Time Travel Device Activation - Security Protocol')
        time.sleep(3.0)

        greeting1 = "Hey " + myuser.name.capitalize() + ",""\n"
        for character in greeting1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.07)

        print()
        time.sleep(0.05)

        greeting2 = "Doc here. I've successfully hacked into the TTD, but there's a security protocol that I have set in place.\n"
        for character in greeting2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.07)

        greeting3 = "Before you can get it to work, you'll need to calibrate and build it.\n"
        for character in greeting3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.07)

        greeting4 = "It's all part of ensuring the right hands control this powerful tech.\n"
        for character in greeting4:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.07)

        greeting5 = "Get ready from here its up to you and your team to fix the TTD. Only the worthy will succeed.\n"
        for character in greeting5:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.07)

        greeting6 = "Let's make sure we're all on the same timeline.\n"
        for character in greeting6:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.07)

        print()
        time.sleep(0.05)

        greeting7 = "Best of luck, Doc\n"
        for character in greeting7:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.07)

        print('Press ENTER key to continue . . .', end="")
        input()
    os.system('clear')
    main_loop()

#starts program and keeps it running
int_screen()
