cars = ["BMW", "Mercedes", "Ford"]

for car in cars:
    print("Car:", car)

for time in range(2):
    print("How are you\nI'm fine")

# print a letter 50 times
# "end=" shows the output all on one line
# "sep=" se[erates each character with something you allocate
for character in range(50):
    print("x", sep="", end="")

#n, i and uppercase detector
word = input("\nEnter a word: ")
for letter in word:
    if letter == "n":
        print("The letter n was found in your word")
    if letter == "i":
        print("the letter i was found in your word")
    if letter == letter.upper():
        print("An upper case was detected")

if "n" in word:
    print("n was found")

is_uppercase = 0
for characterr in word:
    if character == character.upper():
    is_uppercase += 1
if is_uppercase >0:
    print("At least 1 captial letter was found")




