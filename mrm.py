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
        user.total_questions = 38
        user.row = 0
        user.answer = ''
        user.correct_answer = 'portal'
        user.current_quetion_field = ""
        user.key = ''
        user.current_time = ''
        user.random_no = 0
        user.countdown_complete = False
        user.first_time = True
        user.access_TTD = False
        user.game_over = False
myuser = user()

# Title screen
def title_screen_functions():
    option = input('>')
    if option.lower().strip() == ('login'):
        user_login()
        setup_TTD()
    elif option.lower().strip() == ('create user'):
        create_user()
        os.system('clear')
        main_screen()
    elif option.lower().strip() == ('.admin!!'):
        admin_check()
    elif option.lower().strip() == ('shutdown'):
        shutdown()
    elif option.lower().strip() == ('.exit!!'):
        myuser.game_over = True
        exit_program().strip()


    while option.lower() not in ['login', 'create user', '.admin!!', 'shutdown', '.exit!!']:
        print('Incorrect input please enter login or create user')
        option = input('>')
        if option.lower().strip() == ('login'):
            user_login()
            setup_TTD()
        elif option.lower().strip() == ('create user'):
            create_user()
            os.system('clear')
            main_screen()
        elif option.lower().strip() == ('.admin!!'):
            admin_check()
        elif option.lower().strip() == ('shutdown'):
            shutdown()
        elif option.lower().strip() == ('.exit!!'):
            myuser.game_over = True
            exit_program()

# user options to call from anywhere
def user_options():
    if myuser.answer.lower().strip() == '.admin!!':
        admin_check()
    elif myuser.answer.lower().strip() == 'logout':
        main_screen()
    elif myuser.answer.lower().strip() == 'shutdown':
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
        writer = csv.DictWriter(file_update, fieldnames=["user_row","username","current_question","countdown_complete","access_TTD","answer0","answer1","answer2","answer3","answer4","answer5","answer6","answer7","answer8","answer9","answer10","answer11","answer12","answer13","answer14","answer15","answer16","answer17","answer18","answer19","answer20","answer21","answer22","answer23","answer24","answer25","answer26","answer27","answer28","answer29","answer30","answer31","answer32","answer33","answer34","answer35","answer36","answer37","answer38","answer39","answer40"])
        writer.writerow({"user_row": myuser.row,"username": myuser.name,"current_question": 0, "countdown_complete": False, "access_TTD": False})

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

                myuser.access_TTD = row[4]
                if myuser.access_TTD == 'False':
                    myuser.access_TTD = False
                else:
                    myuser.access_TTD = True

# update user save data
def user_save_data():
    field_names = ["user_row","username","current_question","countdown_complete","access_TTD","answer0","answer1","answer2","answer3","answer4","answer5","answer6","answer7","answer8","answer9","answer10","answer11","answer12","answer13","answer14","answer15","answer16","answer17","answer18","answer19","answer20","answer21","answer22","answer23","answer24","answer25","answer26","answer27","answer28","answer29","answer30","answer31","answer32","answer33","answer34","answer35","answer36","answer37","answer38","answer39","answer40"]

    user_save_data_temp = {}

    with open('user_save_data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        user_save_data_temp = [row for row in csv_reader]
        # print print(user_save_data_temp)

    #print(user_save_data_temp[myuser.row])
    myuser.current_quetion_field = field_names[myuser.current_question + 5]
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
                # sets varible and makes sure to wrap text to desired width
                max_width = 60
                wrapped_paragraph = textwrap.wrap(row[1], width=max_width)
                for line in wrapped_paragraph:
                    print(line)

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
            if myuser.access_TTD == True:
                ttd_completion_screen()
            else:
                access_denied()

        elif myuser.countdown_complete == False:
            countdown()

    else:
        current_percent = round(myuser.current_question / myuser.total_questions * 100)
        print_length = round(myuser.current_question / myuser.total_questions * 65)
        print("=================================================================")
        print('|              TTD4092 Calibration completion level             |')
        print("=================================================================")
        for i in range(print_length):
            print('-', end='')
        print(f"{current_percent}%")
        print("=================================================================")
        print_current_question()
        print('Type your answer below')
        answer = input('>')
        myuser.answer = answer.lower().strip()

        # safety exit for me to fix any issues that might be found while program is running
        if answer.lower().strip() == '.exit!!':
            myuser.game_over = True
            exit_program()
        elif answer.lower().strip() == '.admin!!':
            admin_check()
        elif answer.lower().strip() == 'logout':
            main_screen()
        elif answer.lower().strip() == 'show keys':
            print_all_keys()
        # easter egg from back to the future
        elif answer.lower().strip() == '88 miles per hour':
            car_print()
            time.sleep(5)
            os.system('clear')
        elif answer.lower().strip() == 'shutdown':
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
                # sets varible and makes sure to wrap text to desired width
                max_width = 65
                wrapped_paragraph = textwrap.wrap(row[1], width=max_width)
                for line in wrapped_paragraph:
                    print(line)


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

    # Calling the timedelta() function (30 mins is total time students do I go 60min)
    time_change = datetime.timedelta(minutes=30)
    myuser.current_time = date_and_time + time_change

    # Printing the new datetime object
    print("Changed time:")
    print(myuser.current_time.strftime('%H:%M:%S'))

    while myuser.answer != myuser.correct_answer:
        os.system('clear')
        new_date_time = datetime.datetime.today()
        time_rem = myuser.current_time - new_date_time

        # Extracting hours, minutes, and seconds from the timedelta object
        hours, remainder = divmod(time_rem.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # checks the user still has time to complete type the answer in the program
        if time_rem.seconds > 0 and time_rem.seconds < 1801:
            # Printing the time remaining in the desired format
            print('Calibration complete you now have 30 mins to enter the final answer')
            print("---------------------------------------------------------------------")
            max_width = 65
            wrapped_paragraph = textwrap.wrap("On your travels you would have seen Random words and years. First order these by date. Then what ever order they are in is there number. Use that number letter and it should make a word. For example dog is third in the timeline use the third letter ‘g’.", width=max_width)
            for line in wrapped_paragraph:
                print(line)
            print("---------------------------------------------------------------------")
            print("Time remaining: {:02}:{:02}:{:02}".format(hours, minutes, seconds))
            print('Answer: ', end='')
            myuser.answer = input('>').lower().strip()

        else:
            break

    if myuser.answer == myuser.correct_answer:
        os.system('clear')
        myuser.countdown_complete = True
        myuser.access_TTD = True
        update_user_countdown()
        pass_timer()

    else:
        os.system('clear')
        myuser.countdown_complete = True
        myuser.access_TTD = False
        update_user_countdown()
        fail_timer()

# updates user countdown_complete
def update_user_countdown():
    field_names = ["user_row","username","current_question","countdown_complete","access_TTD","answer0","answer1","answer2","answer3","answer4","answer5","answer6","answer7","answer8","answer9","answer10","answer11","answer12","answer13","answer14","answer15","answer16","answer17","answer18","answer19","answer20","answer21","answer22","answer23","answer24","answer25","answer26","answer27","answer28","answer29","answer30","answer31","answer32","answer33","answer34","answer35","answer36","answer37","answer38","answer39","answer40"]

    user_save_data_temp = {}

    with open('user_save_data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        user_save_data_temp = [row for row in csv_reader]
        # print print(user_save_data_temp)

    user_save_data_temp[myuser.row].update({"countdown_complete": myuser.countdown_complete, "access_TTD": myuser.access_TTD})

    # re-writes user data
    with open('user_save_data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(user_save_data_temp)

# create a screen to print amessage to the user that they did not complete the screen in time and they missed out on the treasure.
def fail_timer():
    os.system('clear')
    print(r"""
                ____ ___  ____  _____
               / ___/ _ \|  _ \| ____|
              | |  | | | | | | |  _|
              | |__| |_| | |_| | |___
             __\____\___/|____/|_____|___
            | ____|  _ \|  _ \ / _ \|  _ \
            |  _| | |_) | |_) | | | | |_) |
            | |___|  _ <|  _ <| |_| |  _ <
            |_____|_| \_\_| \_\\___/|_| \_\
#######################################################
#                     Error code 418                  #
#######################################################
#              TTD4092 Code Malfunction               #
# This time location file is corrupt and cant be used #
#     The device will now load its defult program     #
####################################################### """)
    time.sleep(5)
    os.system('clear')
    for i in range(100):
        print('##################################################################')
        print('##################################################################')
        print(f'    TTD4092 SELF REBOOT - TTD4092 Loading version 8.4.21 %{i}    ')
        print('##################################################################')
        print('##################################################################')
        time.sleep(.1)
        os.system('clear')
        myuser.countdown_complete = True
        update_user_countdown()

# creates a screen to print a message that user has won and gets the treasuer
def pass_timer():
    os.system('clear')
    print(r"""

 __     ______  _    _   _____ _____ _____    _____ _______
 \ \   / / __ \| |  | | |  __ \_   _|  __ \  |_   _|__   __|
  \ \_/ / |  | | |  | | | |  | || | | |  | |   | |    | |
   \   /| |  | | |  | | | |  | || | | |  | |   | |    | |
    | | | |__| | |__| | | |__| || |_| |__| |  _| |_   | |
  __|_|_ \____/ \____/ _|_____/_____|_____/__|_____|__|_|
 |  ____|  __ \ / __ \|  \/  |   |  __ \ / __ \ / ____|
 | |__  | |__) | |  | | \  / |   | |  | | |  | | |
 |  __| |  _  /| |  | | |\/| |   | |  | | |  | | |
 | |    | | \ \| |__| | |  | |   | |__| | |__| | |____
 |_|    |_|  \_\\____/|_|  |_|   |_____/ \____/ \_____|

#######################################################
#   You did it now you have shown me you are worthy   #
#  I have programmed the device to take you the year  #
#        where I hid the treasure which is 2077       #
####################################################### """)
    time.sleep(10)
    os.system('clear')
    print('##################################################################')
    print('##################################################################')
    print(f'   Take this CODE and YEAR to Mr Novinec to get your prize       ')
    print('           Code: 8B3K-9P6X-2A1Z     Year: 2077                    ')
    print('##################################################################')
    print('##################################################################')
    time.sleep(5)
    print('Press ENTER to load the Novtronics TTD4092 software.              ')
    input('>').lower().strip()
    os.system('clear')
    print(r"""
                ____ ___  ____  _____
               / ___/ _ \|  _ \| ____|
              | |  | | | | | | |  _|
              | |__| |_| | |_| | |___
             __\____\___/|____/|_____|___
            | ____|  _ \|  _ \ / _ \|  _ \
            |  _| | |_) | |_) | | | | |_) |
            | |___|  _ <|  _ <| |_| |  _ <
            |_____|_| \_\_| \_\\___/|_| \_\
#######################################################
#                     Error code 418                  #
#######################################################
#              TTD4092 Code Malfunction               #
# This time location file is corrupt and cant be used #
#     The device will now load its defult program     #
####################################################### """)
    time.sleep(7)
    os.system('clear')
    for i in range(100):
        print('##################################################################')
        print('##################################################################')
        print(f'    TTD4092 SELF REBOOT - TTD4092 Loading version 8.4.21 %{i}    ')
        print('##################################################################')
        print('##################################################################')
        time.sleep(.1)
        os.system('clear')

# takes user to the TTD screen for them to use to teleport to differnet times
def ttd_completion_screen():
    is_int = False
    if myuser.first_time == True:
        myuser.current_time = datetime.datetime.today().year

        while is_int == False:
            print('##################################################################')
            print('#      Novtronics TTD4092 - SN: 150-32-020 - version 8.4.21      #')
            print('##################################################################')
            print('#                  Time Travel User Interface                    #')
            print('##################################################################')
            print(f'               Your current year is:{myuser.current_time}        ')
            print('##################################################################')
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
            print('##################################################################')
            print('#      Novtronics TTD4092 - SN: 150-32-020 - version 8.4.21      #')
            print('##################################################################')
            print('#                  Time Travel User Interface                    #')
            print('##################################################################')
            print(f'                Your current year is:{myuser.current_time}       ')
            print('##################################################################')
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

# access denied screen if the user does not answer the question in time
def access_denied():
    os.system('clear')
    print(r"""
##################################################################
##################################################################
#       _   ___ ___ ___ ___ ___   ___  ___ _  _ ___ ___ ___      #
#      /_\ / __/ __| __/ __/ __| |   \| __| \| |_ _| __|   \     #
#     / _ \ (_| (__| _|\__ \__ \ | |) | _|| .` || || _|| |) |    #
#    /_/ \_\___\___|___|___/___/ |___/|___|_|\_|___|___|___/     #
##################################################################
##################################################################
#   You do not have the correct credentials to use this device   #
#                   ERROR Code: 403 Forbidden                    #
##################################################################
##################################################################
#         Please contact Novtronics for technical support        #
#                               or                               #
#               Please logout or shutdown the device             #
##################################################################
##################################################################""")
    print('Please type your option here.')
    myuser.answer = input('>').lower().strip()
    if myuser.answer in ['logout', '.admin!!', 'shutdown', '.exit!!']:
        user_options()

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

        greeting2 = "Doc here. I've successfully hacked into the TTD and I have put a security protocol in place.\n"
        for character in greeting2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)

        greeting3 = "Before you can get the TTD4092 to work, you'll need to calibrate and build it.\n"
        for character in greeting3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)

        greeting4 = "It's all part of ensuring the right hands control this powerful tech.\n"
        for character in greeting4:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)

        greeting5 = "Get ready from here its up to you and your team to fix the TTD. Only the worthy will succeed.\n"
        for character in greeting5:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)

        greeting6 = "Let's make sure we're all on the same timeline. See you then if you are worthy.\n"
        for character in greeting6:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)

        print()
        time.sleep(0.05)

        greeting7 = "Best of luck, Doc\n"
        for character in greeting7:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)

        print('Press ENTER key to continue . . .', end="")
        input()
    os.system('clear')
    main_loop()

#starts program and keeps it running
int_screen()
