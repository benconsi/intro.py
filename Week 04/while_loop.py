MENU = "l) Login, S) Sing up, q) Quit"

valid_username = ben
valid_password = benben

done = False
while True:
    print(MENU)
    user_choice = input("Choose [l/s/q]: ").lower()
    if user_choice == "l":
        print("logging you in...")
        entered_username = input("Enter your username: ")
        entered_password = input("enter your password: ")
        if entered_username == valid_username and entered_password == valid_passwrd
            print("Successfull Login")
            done = True
        else:
            print("Invalid Credentials")
            done = True
    elif user_choice == "s":
        print("Signing you up...")
    elif user_choice == "q":
        print("quitting the program...")
        done = True
    else:
        print("invalid choice.")




