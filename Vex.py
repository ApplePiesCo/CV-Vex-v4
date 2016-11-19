#Imports
import time
import sqlite3
from hashlib import md5


#Re-Marks...
print("""
Creator: Mr. Apple
Imports: KLS Productions Login System.
Program Name: Vex
""")
      
time.sleep(1)
      
print("""
Description: An Artificial Intelligence Conversation Bot.
Warnings: IN THIS VERSION IT WONT SAVE THE ANSWERS YOU INPUT.
Example: VEX: What is you favorite color?
        User: Square.
         VEX: YOU'RE DUMB!!
              *CRASH*
              *Reboot*
    Computer: BLAH, BLAH, BLAH.
              Login. (1)
              Creat New User? (2)
        User: 1
              *Login*
         VEX: Hello Welcome (INSERT USER NAME HERE!)
         VEX: Im going to ask you some questions so I can know more about you.
         VEX: *Asking questions AGAIN*
""")
      
time.sleep(1)
      
print("""
Version: 0.V 1
""")


 #logins
class Login():

    def __init__(self, database = "database.db"):
        self.db = sqlite3.connect(database)
        self.sql = self.db.cursor()

        self.sql.execute("CREATE TABLE IF NOT EXISTS database (username TEXT, password TEXT);")

    def new_user(self, username, password):
        self.sql.execute("INSERT INTO database (username, password) VALUES (?, ?);",
                         (username, md5(password.encode()).hexdigest()))
        self.db.commit()

    def check(self, username, password):
        self.sql.execute("SELECT * FROM database WHERE username = ? AND password = ?",
                         (username, md5(password.encode()).hexdigest()))
        data = self.sql.fetchall()
        if len(data) < 1:
            return False
        elif len(data) == 1:
            return True
        else:
            print("Duplicate login entry in database, please remove the duplicate user")

db = Login()



def login():
    username = input("Username: ")
    password = input("Password: ")

    if not db.check(username, password):
        return False
    else:
        return username

def createnew():
    username = input("New Username: ")
    while True:
        password = input("New Password: ")
        retype = input("Retype Password: ")
        if password == retype:
            break
        print("Passwords did not match!")
    db.new_user(username, password)



print('''
------------------------------
1) Login
2) Create New User
------------------------------
''')
while True:
    option = input(">> ")
    if option == "1" or option.lower == "login":
        user = login()
        if user:
            print("Welcome", user)
        else:
            print("Invalid username/password!")
            continue
        break
    elif option == "2" or option.lower == "create new user":
        createnew()
    else:
        print("Please enter one of the above options")
        continue


#CODE
time.sleep(2)
print("Hello and welcome " + username + ", my name is Vex.")
print("Can I just ask you some questions so I learn more about you?")

print("How old are you?")
player_age = input()

print("What's your favorite number?")
favorite_number = input()
if favorite_number == "8":
        print("Nice the lucky number 8!")
elif favorite_number == "69":
        print("Immature you're grounded!!!")
elif favorite_number == "21":
        print("HeHeHe, MY NAME IS JEFF!")
else:
        print("Nice I like " + favorite_number + " too but, my favorite number is 8!")

print("What is your favorite Color?")
favorite_color = input()
if favorite_color == "ORANGE":
        print("THAT'S NOT A COLOR THATS A FRUIT!!")
