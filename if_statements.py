# if= Do some code IF some condition is TRUE 
#    ELSE do something else 

age =int (input("Enter your age: "))
if age >=18:  # any code underneath if statement should be indented
    print("You are now signed up!")
elif age<0:
    print("Invalid age")
elif age >=100:
    print("You are too old to sign up") # you will be allowed to sign in because of the order of your code
else:  
    print("You must be 18+ to register")


