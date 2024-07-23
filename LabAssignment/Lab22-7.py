 #Exception handeling
try:
    print(100/0)
except ZeroDivisionError as e:
    print(e)
    
try:
    print(int(input('Enter a int value')))   
except ValueError:
    print('Please enter a valid int value') 
    
try:
    open('abc.txt')
except FileNotFoundError:
    print('File does not exits')
    
try:
    print(int(input('Enter First int value')))
    print(int(input('Enter Second int value')))   
except ValueError:
    print('Please enter a valid int value') 
