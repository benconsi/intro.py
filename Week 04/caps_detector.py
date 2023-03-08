word = input("Enter your word: ")
if "n" in word:
    print("n was found")

caps_count = 0
for char in word:
    if char == char.upper():
        caps_count += 1
if caps_count