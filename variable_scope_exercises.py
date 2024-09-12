# What will the following code print and why? Don't run it until you have tried to answer.
num = 5

def my_func():
    print(num)

my_func()

# It will print 5. myFunc() has access to the outer scope's 'num' variable.


# What will the following code print and why? Don't run it until you have tried to answer.
num = 5

def my_func():
    num = 10

my_func()
print(num)

# it will print 5. myFunc() creates a new variable inside the local scope, it does not reassigns the outter scope to 10.


# What will the following code print and why? Don't run it until you have tried to answer.
num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)
# It will print 10. Inside myFunc() the variable num points to the outter global scope due to the 'global' keyword.


# What will the following code print and why? Don't run it until you have tried to answer.
def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()
# It will print 'Hello World'. The inner() function has access to the outer_var.


# What will the following code do? Don't run it until you have tried to answer.
def my_func():
    num = 10

my_func()
print(num)
# It will throw a nameError because num is not defined within the scope that its being accessed in.


# What will the following code print and why? Don't run it until you have tried to answer.
def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()
# It will print:
    # "Inner 1: 25"
    # "Inner 2: 15"
# inner_func1() creates a new 'x' variable and assigns it the value of 25.
# inner_func2() only has access to the x variable in the outer scope which is 15.
