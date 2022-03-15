import os

list = os.listdir()
""" These commands deal with multiple files. NOTE: All of these functions are not case sensitive."""

""" Lists every file. """
def list():
    list = os.listdir()
    print(list)

""" Finds all files with exact letters, extension included. Ex: ".py" in "dolphin.py" is a match. """
def find(name):
    list = os.listdir()
    file_match = []
    for x in list:
        if name.lower() in x.lower():
            file_match.append(x)
    print(file_match)

""" Searches the file contents that contain the given word. Prints the filename, line num, and contents of matched string. """
def search(word, name=".txt"):
    list = os.listdir()
    string_match = []
    for x in list:
        if name.lower() in x.lower():
            file = open(x, "r")
            filelist = file.readlines()
            count = 1
            for y in filelist:
                if word.lower() in y.lower():
                    matched_string = x + ":Line " + str(count) + ":" + y
                    string_match.append(matched_string)
                count = count + 1
    print(string_match)

""" Deletes all files with exact letters. """
def remove(name):
    list = os.listdir()
    for x in list:
        if name.lower() in x.lower():
            os.remove(x)
            print("Deleted", x)





