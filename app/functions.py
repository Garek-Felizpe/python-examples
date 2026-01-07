
def greetings():
    print("Hello, World!")

greetings() #Print "Hello, World!"


def greetings_name(name):
    print(f"Hello, {name}!")

greetings_name("Alice") #Print "Hello, Alice!"
greetings_name("Bob") #Print "Hello, Bob!"


def sum(a, b):
    return a + b

resultado = sum(3, 4)
print(resultado)  # Print 7


square = lambda x: x ** 2
print(square(5))  # Print 25


def function():
    local_var = 10
    print(local_var) # Accessible within the function

global_var = 20

def function2():
    print(global_var) # Accessible anywhere


function() # Print 10
function2() # Print 20
print(global_var) # Print 20
print*(local_var) # Generates an error, because local_var is not defined globally