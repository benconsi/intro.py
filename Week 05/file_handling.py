
# Create and open a file for the purpose of re-writing
file_out = open("file.txt", "w")
file_out.write("This is the first line.\n")
file_out.write("this is the second line.\n")
file_out.close()

# Create and open a file for the purpose of appending (adding to the existent)
file_out = open("file_append.txt", "a")
file_out.write("This is the first line.\n")
file_out.write("this is the second line.\n")
file_out.close()

# Open a file for the purpose of reading
file_in = open("file.txt", "r")
print(file_in.read())
file_in.close()

phonebook_dictionary = {}
phonebook_file_in = open("phonebook.txt", "r")

phrase = "Name Phone"
ph = phrase.split(" ")
print(ph)

