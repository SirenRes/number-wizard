from json.tool import main
import sys
import random
import time

class Menu:
    difficulty = "Easy"
    def __init__(ctx):
        print("""
------------------------
Welcome to the Number Guessing Game!
------------------------
        =*===
       $$- - $$$
       $ <    D$$
       $ -   $$$
 ,     $$$$  |
///; ,---' _ |----.
 \ )(           /  )
 | \/ \.   '  _.|  \              $
 |  \ /(   /    /\_ \          $$$$$
  \ /  (       / /  )         $$$ $$$
       (  ,   /_/ ,`_,-----.,$$  $$$
       |   <----|  \---##     \   $$
       /         \\\           |    $
      '   '                    |
      |                 \      /
      /  \_|    /______,/     /
     /   / |   /    |   |    /
    (   /--|  /.     \  (\  (_
     `----,( ( _\     \ / / ,/
           | /        /,_/,/
          _|/        / / (
         / (        ^-/, |
        /, |          ^-   """)
        ctx.res()
    @classmethod
    def start(ctx):
        print(Menu.difficulty)
        ctx.hp = 3
        def easy():
            number = random.randint(1, 10)
            while True:
                try:
                    guess = int(input("Enter your guess:\n"))
                except:
                    print("Please make sure you have entered a valid number.")
                    continue
                else:
                    if number == guess and ctx.hp > 0:
                        print("Loading, please wait...")
                        time.sleep(2)
                        print(''' _nnnn_                      
        dGGGGMMb     ,"""""""""""""""""""""""""""""""""""""""""".
       @p~qp~~qMb    | You guessed Right! You have won the game! |
       M|@||@) M|   _;..........................................'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' hjm''')
                        break
                    elif number != guess and ctx.hp > 0:
                        print("Loading, please wait...")
                        time.sleep(2)
                        print(''' ,        ,
                                /(        )`
                                \ \___   / |
                                /- _  `-/  '
                               (/\/ \ \   /\
                               / /   | `    \
                               O O   ) /    |
                               `-^--'`<     '
                   TM         (_.)  _  )   /
|  | |\  | ~|~ \ /             `.___/`    /
|Wrong Guess! You lost a health point!|`-----' /
`__| |  \| _|_ / \  <----.     __ / __   \
                    <----|====O)))==) \) /====
                    <----'    `--' `.__,' \
                                 |        |
                                  \       /
                             ______( (_  / \______
                           ,'  ,-----'   |        \
                           `--{__________)        \/''')
                        ctx.hp -= 1
                        continue
                    if ctx.hp == 0:
                        print("No health points left!\nGame over.")
                        time.sleep(2)
                        ctx.exit()
        def normal():
            number = random.randint(1, 50)
            while True:
                try:
                    guess = int(input("Enter your guess:\n"))
                except:
                    print("Please make sure you have entered a valid number.")
                    continue
                else:
                    if number == guess and ctx.hp > 0:
                        print("Loading, please wait...")
                        time.sleep(2)
                        print(''' _nnnn_                      
        dGGGGMMb     ,"""""""""""""""""""""""""""""""""""""""""".
       @p~qp~~qMb    | You guessed Right! You have won the game! |
       M|@||@) M|   _;..........................................'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' hjm''')
                        break
                    elif number != guess and ctx.hp > 0:
                        print("Loading, please wait...")
                        time.sleep(2)
                        print(''' ,        ,
                                /(        )`
                                \ \___   / |
                                /- _  `-/  '
                               (/\/ \ \   /\
                               / /   | `    \
                               O O   ) /    |
                               `-^--'`<     '
                   TM         (_.)  _  )   /
|  | |\  | ~|~ \ /             `.___/`    /
|Wrong Guess! You lost a health point!|`-----' /
`__| |  \| _|_ / \  <----.     __ / __   \
                    <----|====O)))==) \) /====
                    <----'    `--' `.__,' \
                                 |        |
                                  \       /
                             ______( (_  / \______
                           ,'  ,-----'   |        \
                           `--{__________)        \/''')
                        ctx.hp -= 1
                        continue
                    if ctx.hp == 0:
                        print("No health points left!\nGame over.")
                        time.sleep(2)
                        ctx.exit()
            
        def hard():
            number = random.randint(1, 100)
            while True:
                try:
                    guess = int(input("Enter your guess:\n"))
                except:
                    print("Please make sure you have entered a valid number.")
                    continue
                else:
                    if number == guess and ctx.hp > 0:
                        print("Loading, please wait...")
                        time.sleep(2)
                        print(''' _nnnn_                      
        dGGGGMMb     ,"""""""""""""""""""""""""""""""""""""""""".
       @p~qp~~qMb    | You guessed Right! You have won the game! |
       M|@||@) M|   _;..........................................'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' hjm''')
                        break
                    elif number != guess and ctx.hp > 0:
                        print("Loading, please wait...")
                        time.sleep(2)
                        print(''' ,        ,
                                /(        )`
                                \ \___   / |
                                /- _  `-/  '
                               (/\/ \ \   /\
                               / /   | `    \
                               O O   ) /    |
                               `-^--'`<     '
                   TM         (_.)  _  )   /
|  | |\  | ~|~ \ /             `.___/`    /
|Wrong Guess! You lost a health point!|`-----' /
`__| |  \| _|_ / \  <----.     __ / __   \
                    <----|====O)))==) \) /====
                    <----'    `--' `.__,' \
                                 |        |
                                  \       /
                             ______( (_  / \______
                           ,'  ,-----'   |        \
                           `--{__________)        \/''')
                        ctx.hp -= 1
                        continue
                    if ctx.hp == 0:
                        print("No health points left!\nGame over.")
                        time.sleep(2)
                        ctx.exit()
        {"Easy": easy, "Normal": normal, "Hard": hard}.get(Menu.difficulty)()
    @classmethod
    def settings(ctx):
        ctx.dif = input("Select the difficulty:\n1-) Easy\nn2-) Normal\n3-) Hard\n")
        if ctx.dif == "1":
            print("Difficulty is set by default.")
            ctx.res()
        elif ctx.dif == "2":
            Menu.difficulty = "Orta"
            print("Difficulty is set to Normal.")
            ctx.res()
        elif ctx.dif == "3":
            Menu.difficulty = "Zor"
            print("Difficulty is set to Hard.")
            ctx.res()
        else:
            print("Difficulty has not been changed!")
            ctx.res()
    @classmethod
    def exit(ctx):
        print("Checking out...")
        time.sleep(2)
        sys.exit()
    @classmethod
    def res(ctx):
        ctx.entry = input("Main Menu\n1-) Begin\n2-) Settings\n3-) Exit\n")
        ctx.bum = {"1": ctx.start, "2": ctx.settings, "3": ctx.exit}
        try:
            ctx.bum[ctx.entry]()
        except:
            print("You did not enter a valid number.")
        else:
            pass