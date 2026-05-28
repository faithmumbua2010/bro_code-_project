# input() = A function that prompts the user to enter data 
#           Returns the entered data as a string

name=input("What is your name?: ") # this will prompt the user to enter their name and it will return the entered data as a string
age = int (input("How old are you?: ")) # this will prompt the user to enter their age and it will return the entered data as a string

   
age= age + 1 # this will add 1 to the age entered by the user and store it back in the age variable 



print(f"Hello {name}!") # this will print Hello followed by the name entered by the user
print("HAPPY BIRTHDAY!") # YOU use a f-string if inserting variables into a string, otherwise you can just use a regular string

print(f"You are {age} years old.") # this will print You are followed by the age entered by the user


