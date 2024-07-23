#Ques:1 Write a function in python to read the content from a text 'ABC.txt' line by line and display the same on screen.

def read_and_display_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')  
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
read_and_display_file('ABC.txt')


#Ques:2 Write a function in Python to count and display the total number of words in a text file 'ABC.txt'.

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            total_words = len(words)
            print(f"Total number of words in {filename}: {total_words}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_words_in_file('ABC.txt')


#Ques:3 Write a function in python to count uppercase character in a text file 'ABC.txt'.

def count_uppercase_characters(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            uppercase_count = sum(1 for char in text if char.isupper())
            print(f"Total number of uppercase characters in {filename}: {uppercase_count}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_uppercase_characters('ABC.txt')


#Ques:4 Write a function display_words() in python to read lines from a text file 'story.txt', and dispaly those words, which are less than 4 characters.

def display_words(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                short_words = [word for word in words if len(word) < 4]
                for word in short_words:
                    print(word)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

display_words('story.txt')
