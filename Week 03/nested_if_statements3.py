MENU = "l) login, q) Quit"
valid_username = "benconsi"
valid_password = "eldogma"
security_1 = "four"
security_2 = "green"
security_3 = "blue"

# MENU s in caps, and it means it's a CONSTANT
# The CONSTANT is a variable that never changes its value

print(MENU)
user_choice = input("Choose [l/q]: ")

if user_choice == "l":
    print("logging you in")
    entered_username = input("enter your username: ")
    entered_password = input("enter your password: ")
    if entered_username == valid_username and entered_password == valid_password:
        print("Please Answer the following security questions")
    else:
        print("invalid credentials")
    entered_security_1 = input("how many legs does a dog have?: ")
    entered_security_2 = input("what is the colour of grass?: ")
    entered_security_3 = input("what colour is the sky?: ")
    if entered_security_1 == security_1 and entered_security_2 == security_2 and entered_security_3 == security_3:
        print("Successfully logging in")
    else:
        print("invalid credentials")

elif user_choice == "q":
    print("quitting the program")
else:
    print("Invalid choice")




