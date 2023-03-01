def my_calculator():
    print(5 * 5)


my_calculator()


def ask_for_name():
    name = input("Enter your name: ")


ask_for_name()

is_adult = False


def verify_age_auto(the_age):
    if the_age >= 18:
        print("You may enter!")
    else:
        print("You are not allowed in!")

verify_age_auto(18)

def welcome(someone):
    print("Welcome", someone, "we're excited to see you here")

welcome("Ben")

def goodbye(attendant):
    print("Goodbye", attendant, "have a good night")
goodbye("Ben")


def is_adult(an_age):
    if an_age >= 18:
        return True
    else:
        return False


if is_adult(10):
    print("welcome")
else:
    print("Sorry")


def multiply_by_five(number):
    return 5 * number

print(multiply_by_five(5))


















