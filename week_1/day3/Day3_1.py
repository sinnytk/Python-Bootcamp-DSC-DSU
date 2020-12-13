#Understanding the Scopes

def alo():
    # it will make a variable a in local scope of this function
    # a = 20
    global a
    # glabal tell the funstion the a you will be refrening will be global a
    a = a * 10  
    print(f'funstion1 {a} {b}')

def alo2():
    print(f'function2 {a} {b}')

a = 2
b = 3

# __name__ 
# The __name__ variable (two underscores before and after) is a special Python variable. It gets its value depending on how we execute the containing script.
# When a Python interpreter reads a Python file, it first sets a few special variables. Then it executes the code from the file.
# when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program. But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.

def myFunction():    
   print('The value of __name__ is ' + __name__)

def main():
    myFunction()
    alo()
    alo2()

# Now the problem is when i import this file in Day3_2.py if my function are globaly calling each they will call them there too thats we use this 

if __name__ == "__main__":
    main()
    # now it will only call the function in this file make complications less