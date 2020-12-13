#FUNCTIONS-- make code not as long. Allows you to repeat a set group of instructions w/o re-writing code.
def say_hello():
    print("hello from a function")


def say_name(name):#nothing goes in parenthesis this is just to show that name is in there
    print("Hello %s" % (name))
say_name ("Lihame")


# This is an example on parameters
list = ["Apple","Banana","Candy"]
list1 = ["dog","cat", "mouse"]
list3 = ["fordham","barnard","queens"]
def print_names(names):
    for name in names:
        print(name)
print_names(list3) #This will print out list3, change it to print out other lists.
#To print each of these lists call the functon (print_name) and input different lists.

                                                                                                                                                                                                                                                                                                                                                               )
def process_input(answer):
    if answer == "hi":
        say_greeting(hey gurl)
    else:
        say_default (boo)

#Calculator
def add(num1,num2):
    sum=num1+num2
    return sum #testing return. Stores the info so there is no output

#    print(sum) You can only get an answer if you print the
add(10,5) #Change numbers in here to add different nums
print(add(10,5))


def add(num1,num2):
    sum = num1 +num2
    return sum

fransAge = 2019-add(1990,7)
print(fransAge)


# Scopes example
a =5 #Global Scope, varaible applys to whole thing.
def a variable():
    a=10 #Local scope, variable only applys to this part.
    #Answer will be 5 b/c global scope is the one used.

a = 5
def aVariable():
    a = 10  #B/c this varable it uses the local variable not the global one
    sum = a + 10
    print(sum)
aVariable () #Outout should be 20
