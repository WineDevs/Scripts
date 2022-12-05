def Example_Function():
    print('Hello World!')

Example_Function() # This function print "Hello World!"
# For example let's create simple calc function

def Calc(a,b): # This function return A+B
    return a+b # Return

# Let's call it

Calc(2,2) # It return 4

# To display this function use print function
print(Calc(2,2))

# Also you can use "eval" function, but it's not secure
# For example, let's calculate 2+2 using the eval function

eval('2+2') # It return 4 but it's not safe because you can enter malicious code

# Let's look at global variables and local

a = 10 # It's global variable

def Function():
    a = 0 # This is a local variable we can't use it outside of def
    
    # But to remove it, just write the word "global"and variables at the beginning of def

# Example

x = 5 # Global var

def Global_Vars():
    global x # Now we are working with a global variable

    x-=3 # X minus 3

#Call this
Global_Vars()

# If we print it it return 2
print(x)