MENU = "l) login, q) Quit"
valid_username = "benconsi"
valid_password = "eldogma"
# MENU s in caps, and it means it's a CONSTANT
# The CONSTANT is a variable that never changes its value

print(MENU)
user_choice = input("Choose [l/q]: ")

if user_choice == "l":
    print("logging you in")
    entered_username = input("enter your username: ")
    entered_password = input("enter your password: ")
    if entered_username == valid_username and entered_password == valid_password:
        print("You have successfully logged in")
    else:
        print("invalid credentials")
elif user_choice == "q":
    print("quitting the program")
else:
    print("Invalid choice")

