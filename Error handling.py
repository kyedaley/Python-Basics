# This is basic demonstration of error handling.

# So lets say you want persons age but they put string instead of int.

age = int(input("Insert your age: ")) # So this will work fine if its int (integer e.g 5, 3) but if string cause error

print("I am: ", age) # his should display age right?

# However if we use string we get following error
# ValueError: invalid literal for int() with base 10

# Theres many ways to go around this 1 been just changing int to str
# Or creating try statement, a try statement can be used as error handler view following code

try: # Testing sort of phaze
    age = int(input("Insert your age: ")) # Gets input
    print(age) # Displays it
except:
    print("An error has occured") # This is if an error happens however we can direct the error to problem we have

# So say you want to direct the error to ValueError to give custom response

try: # Testing
    age = int(input("Insert your age: "))
    print(age)
except ValueError: # The exception ValueError is way to pin point if error ValueError comes up to do something below
    print("Please type in a number")
