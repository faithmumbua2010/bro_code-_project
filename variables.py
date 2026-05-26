# A variable is a container for storing data values(string, integer, float, boolean).
# In Python, you don't need to declare the type of variable, it is inferred from the value assigned to it.

first_name = "John"  # string variable
age = 30  # integer variable
height = 5.9  # float variable
is_student = True  # boolean variable

print(first_name) # Output: John
# if you type print("first_name") the output will be first_name instead of John

# you can also use an f-string to print variables .The f stands for "formatted string literals" and allows you to embed expressions inside string literals, using curly braces {}.
print(f"Hello{first_name}") # Output: Hello John
print(f"The age of {first_name} is {age} years")

# Boolean 
is_student =False
for_sale =False

if for_sale:
    print("That item is for sale ")
else :
    print("That item is NOT available")