class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""welcome to Chatbook !! How could you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           - > """)
        if user_input == "1":
            self.signup()

        elif user_input == "2":
            self.signin()

        elif user_input == "3":
            self.my_post()

        elif user_input == "4":
            self.sendmsg()

        else:
            exit()


    def signup(self):
        email = input("Enter your email here -> ")
        pwd = input("setup your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signedup successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the main menu")
        else:
            usname = input("Enter your email.username here -> ")
            pwd = input("Enter your password -> ")

            if self.username == usname and self.password == pwd :
                print("You have signed in successfully")
                self.loggedin = True
            else:
                print("Please input correct credentials ..")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == False:
            print("You need to signin first to post somethin ")
            self.menu()
        else:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
            self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter the msg to be sent")
            frnd = input("Name the friend ")
            print(f"your msg has been sent to {frnd}")
            self.menu()

        else:
            print("You need to signin first to send a msg")
            self.menu()


         





obj = chatbook()
