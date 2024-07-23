# Ques:1 Write a program to count the occurence of word 'INDIA' in a text file india.txt

def count_occurrences(filename, word):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            count += line.upper().count(word)
    return count
filename = "C:\\Users\\SAMYAK\\Desktop\\vs code\\LabAssignment\\LabAssignment20-7\\india.txt"
word = "INDIA"
occurrences = count_occurrences(filename, word)
print(f"The word '{word}' occurs {occurrences} times in the file '{filename}'.")


# Ques:2 Write a program to count and display the lines starting with 'T' in a text file story.txt

def count_and_display_lines_starting_with_T(filename):
    count = 0
    lines_starting_with_T = []
    with open(filename, "r") as file:
        for line in file:
            # Check if the line starts with 'T'
            if line.startswith('T'):
                count += 1
                lines_starting_with_T.append(line.strip())
    print(f"Number of lines starting with 'T': {count}")
    print("Lines starting with 'T':")
    for line in lines_starting_with_T:
        print(line)
filename = "C:\\Users\\SAMYAK\\Desktop\\vs code\\LabAssignment\\LabAssignment20-7\\story.txt"
count_and_display_lines_starting_with_T(filename)


#Ques:3 Write a program to count and display number of vowels and consonants in a file 'Myfile.txt'

def count_vowels_and_consonants(filename):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    consonant_count = 0
    with open(filename, "r") as file:
        content = file.read()
        for char in content:
            if char.isalpha():  
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")
filename = "C:\\Users\\SAMYAK\\Desktop\\vs code\\LabAssignment\\LabAssignment20-7\\Myfile.txt"
count_vowels_and_consonants(filename)

#Ques:4 Write a program to count and display number of words start with 'i' in file Word.txt

def count_words_starting_with_i(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        words = text.split()
        count = sum(1 for word in words if word.lower().startswith('i'))
        print(f"Number of words starting with 'i': {count}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
file_path = 'C:\\Users\\SAMYAK\Desktop\\vs code\\LabAssignment\\LabAssignment20-7\\Word.txt'
count_words_starting_with_i(file_path)


#Ques:5 Write a program to count and display number of words in a txet file Notes.txt

def count_words(filename):
    word_count = 0
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
    print(f"Number of words in '{filename}': {word_count}")
filename = "C:\\Users\\SAMYAK\\Desktop\\vs code\\LabAssignment\\LabAssignment20-7\\Notes.txt"
count_words(filename)


#Ques:6 Write a program to create a binary file 'Stu.dat' and Enter students rollno. Name and Marks till the user wants.

import struct
def write_student_data(filename):
    with open(filename, "wb") as file:
        while True:
            rollno = input("Enter roll number: ")
            name = input("Enter name: ")
            marks = float(input("Enter marks: "))
            data = struct.pack('i50sf', int(rollno), name.encode(), marks)
            file.write(data)
            cont = input("Do you want to add another student? (y/n): ")
            if cont.lower() != 'y':
                break
filename = "C:\\Users\\SAMYAK\\Desktop\\vs code\\LabAssignment\\LabAssignment20-7\\Stu.dat"
write_student_data(filename)


#Ques7:- Write a program to read a binary file 'Stu.dat' and display the record of students having marks greater than 81.

import struct
def read_student_data(filename):
    students_with_high_marks = []
    record_format = 'i50sf'
    record_size = struct.calcsize(record_format)
    with open(filename, "rb") as file:
        while True:
            record = file.read(record_size)
            if not record:
                break
            rollno, name, marks = struct.unpack(record_format, record)
            name = name.decode().strip('\x00')  
            if marks > 81:
                students_with_high_marks.append((rollno, name, marks))
    print("Students with marks greater than 81:")
    for rollno, name, marks in students_with_high_marks:
        print(f"Roll No: {rollno}, Name: {name}, Marks: {marks}")
filename = "C:\\Users\\SAMYAK\\Desktop\\vs code\\LabAssignment\\LabAssignment20-7\\Stu.dat"
read_student_data(filename)
