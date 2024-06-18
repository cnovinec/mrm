# Mount Rowan Mystery Time Travel Device program interface
#### Video Demo:  <[MRM TTD4092 video demo](https://www.youtube.com/watch?v=y2Y22vVYpBw&ab_channel=KILRSHEEP)>
#### Description:
Intro to program:
Hi there my name is Callan and I will be talking about my program which is for the Novtronics Time Trave Device 4092 which is a fictional device that will be used as a prop and aid to an escape room/treasure hunt style game for students at the school I teach.
This program is designed to run in the cmd terminal window on the RaspberryPI and to emulate the OS of the fictional TTD4092. Its basic function allows the user to create an account and stores their progression through the game. Throughout the program it gives users feedback on how they are going and weather they do anything incorrect. Through the program they are also able to control the RaspberryPi by shutting down the pysical RaspberryPi device.

Key Files and their functions:
Why did I choose these files types? I chose these file types as python was one of the smaller languages to keep tight with large functionallity. I chose to store username and passwords unhased at this point of time as the device will be completely used off grid and only be used to log in and store their game progression. The others I chose to use the csv files as I was able to keep the file size small and was going to be editable in excel which I could then easily transfer over to the Pi when question have been completed. Keeping it as a CSV file I am at anystage able to edit potential errors every quicky which could be an on the go fix.
Eventually I would like to try and change this to a SQL db as this would shrink the code that little bit more. I am yet to fully check how to install SQL on the RaspberryPI.
    - mrm.py - this is the main program which runs and manipulates the cmd terminal once commands are entered.
    - u-p.csv - stores username and passwords and allows mrm.py to check if the user exists
    - user_save_data.csv - stores user data and allows the program to load where the user was upto and keep track of that successfully
    - mrmquestions.csv - stores questions for the program to present to user. stores answers to check when user enters their answer and finally if correct stores key to be printed out key for them to user.
    - rand_wrong.csv - stores all random wrong statements to be called by mrm.py to be printed to the user when inccorect answer is entered in the calibration screen.
    - easteregg.py - allows when function called to print easteregg in terminal. This was used to keep the code clean as there were plans to add a few other eastereggs

Features and functions:
User functions: This section will talk specifically about the user fucntion that I have embbeded so that the program can be used effectivly.
    -Create user - this function allows the user to choose a username and password that dont already exist in the db. The username must not match an already existing one and it must have a  password. When username and password is accepted by the system the program will also create and update the user save data file making a new slot for the new user.
    -Login - Allows a user that already has a username and password created to load into the program to where they are upto in the game progression
    -logout - allows the user from anyscreen other than the countdown screen to type logout and the program will take them to the main screen
    -Shutdown - allows the user from anyscreen other than the countdown screen to type shutdown and the program shutdown the RaspberryPi
    -show keys - allows the user in the calibration screen to type 'show keys' to show all keys the user has succesfully recived to this point in order
    -Easter eggs - allows the user in the calibration screen to type '88 miles per hour' to have the program run the easteregg program associated with that cmd.

Background functions:
Mainscreen
Splash screens - gives the appreance that the device is starting up like a real OS.
Wrong answer - randomly generates a number from 0 to 116 and then gets the the 'statment' from rand_wrong.csv and prints to user
Countdown - grabs system time adds 30 mins and then will continue to change time while user enters incorrect time. Ends when user enters correct answer or time runs out

Admin functions:
.admin!! - allows admin to show all username, passwords and user save data and prints on screen for the admin to check or use.
.exit!! - allows admin exit the program without shutting down the Pi for any sort of fault finding or maintenance

Plan for project start to completion
Below I have written a rough outline of task/milestones I will be working through to have this project up and running for students this year (2024)

list planned stages of full project:
- [x] Plan ideas and basic function of program - Brain storm
- [X] Code main program fault find alpha test. Database soulutions
- [X] Acquire Rasberry Pi and components for final project configuration
- [X] Test Rasberry Pi and components for proof of hardware concept
- [X] Test Rasberry Pi and mrm.py code
- [X] Acquire case to fit all conponents of RaspberryPI and battery
- [X] Develop all questions for project
- [X] Purchase novtronics.com
- [X] Add questions, answers and keys to project db solution
- [X] Add questions and set up website for clues and information
- [X] Full software test
- [X] Full hardware and software test on RaspberryPI
- [X] Use CAD software to develop mounting solution for all hardware components
- [X] Test fit and run ensuring no issues casued by chassis design - CAD changes if needed.
- [X] Full beta testing of fully fitted out hardware and software. Aim to find bugs hardware issues or even 'hacks'
- [X] Final testing
- [] Project implemntation - school term 3 in Aus Monday 22 July 2024 - 0900 AEST

Debugging and issues faced while programming:
Currently I have found a range of issues with this program from small to large and this is a list of all issues needing to be listed and fixed weather it was something I completed right away or the next day. But thought it would be usful to keep track of, if I was to come back and make modification to at a later stage.

list of debug issue put lines of errror and code and issue discription:
- [X] fixed by changing word from any to ENTER - line 61 & 99 issue with any key registers any typed key but must click enter
- [X] fixed by changing myuser.game_over = to True (breaks while loop) - line 60 mrm.py does not sys.exit() even though i do when typed
- [X] fixed by adding setup_TTD() - line 38 when goes throuhg login function it then exits does not continue the program
- [X] fixed by adding main_screen() loop - line 30 after creating username program exits
- [X] fixed by adding code into mrm.py and entering loop if incorrect - line 41 if yhou do not enter the correct username or password 3 times you still pass through to main program and clues
- [X] fixed by adding 0 to current question - line 213 issue when user has logged in and logs out user current question stays so if you are to create a new user after loging out the new user gets the same current question.
- [X] fixed by correcting bool value - line 495 program works till code has to be entered into timer but then goes to black screen needs to go to prompt again I think
- [X] fixed by adding if statment after line 95 - line 125 only when no user entered and after 3rd try program still logs user in skips line 125. error is on line 95 as checks this first then skips the if function later
- [X] fixed by adding os.system('clear') - line 48 shutdown function using in main screen does not clear screen properly
- [X] fixed by editing bash ternminal and adding "nano ~/bashrc" then "trap '' 20" and "trap '' 2" - in bash on RaspberryPI users can use ctrl z/ ctrl c to end program
- [X] Fixed with "xterm -fullscreen - fa 'Monospace' -fs 15 bg black -fg red" - Issue getting screen fullscreen
- [X] Fixed with "nano ~/bashrc" then putting in line of cd to the file location then running the python program - Run python program at start up of terminal


Source code is located: <[Github source code](https://github.com/cnovinec/mrm)>
I have uploaded the source code and the important files that the program uses to opperate. I have not only uploaded a the cs50 video but a more detailed video to my YouTube which can be found here [NO VIDEO AVALIBLE YET]. Feel free to contact me on github or via my YouTube <youtube.com/@KILRSHEEP>

Conponent list - Below I have created a list for anyone wishing to replecate this project. It will have websites as well as links to CAD files of my chassis desgin.
- <[Raspberry Pi 4B Single Board Computer 8GB](https://www.jaycar.com.au/raspberry-pi-4b-single-board-computer-8gb/p/XC9104?pos=3&queryId=24a1c2c3684f4caf360c14185bba2180&sort=relevance&searchText=Raspberry%20Pi%204B)>
- <[Case heatink Heatsink Case with Dual Fan for RPi4](https://www.jaycar.com.au/heatsink-case-with-dual-fan-for-rpi4/p/XC9112?pos=6&queryId=8662e3467dc9c968a3db10f6ab7170ce&sort=relevance&searchText=Raspberry%20pi%20case)>
-  <[Display - 1024x600 HDMI 7in Screen with USB Capacitive Touch](https://www.jaycar.com.au/1024x600-hdmi-7in-screen-with-usb-capacitive-touch/p/XC9026)>
- Cables - HDMI to micro HDMI, USB c to USB a, USB a to micro USB  <>
- <[Battery - Cygnett ChargeUp Maxx Digital 30k Power Bank (Black)](https://www.jbhifi.com.au/products/cygnett-chargeup-maxx-digital-30k-power-bank-black?ab_version=B&gad_source=1&gclid=Cj0KCQjw_qexBhCoARIsAFgBleu9gyE6HHaScHiQTHva6gDxj99TcLwl8yPkD7jR5sFrOWgvmpOVhlEaAuMjEALw_wcB)>
- <[Case - Tactix Tough Case in Black - Medium](https://www.bunnings.com.au/tactix-tough-case-in-black-medium_p0492544)>
- <[CAD files](https://www.thingiverse.com/thing:6595698)>
- <[Keyboard - Logitech K380S Pebble Keys 2 Wireless Keyboard (Graphite)](https://www.jbhifi.com.au/products/logitech-k380s-pebble-keys-2-wireless-keyboard-graphite)>

