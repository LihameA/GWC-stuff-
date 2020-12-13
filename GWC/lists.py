'''
from random import *
#This is a LIST of women in tech
womenInTech = ["Amanda Randle", "Dr. Aprille Joy Ericsson", "Cindy Alvarez","Dorothy Vaughan","Jess Lee"]

#This is a FOR loop that prints women in tech
    #For the item (women)in the list (womenInTech) print the item (women)
for women in womenInTech:
    print(women)

#one way to print out the number of women in tech in my list
print("This is the number of women attending the conference: ")
print(len(womenInTech))

#Storing the size of the list in a variable called 'numberOfWomen'
numberOfWomen = len(womenInTech)
print("This is the number of women attending the conference: %d" %(numberOfWomen))


#Checking to see if jess Lee is in the list
print("Jess Lee in the list")
print("Jess Lee" in womenInTech)#This will return true!

#(Testing) Checking to see if kris Jenner is in the list
print("Is Kris Jenner a computer scientist")
print("Kris Jenner" in womenInTech)

#Seeing a loop using  the built in funtcion called 'range '

#This is how many times the for loop runs
limit = range(len(womenInTech))
for i in limit:
    print(womenInTech[i]) #womenInTech[i] accesses the elemnt at the index i

#Choosing a random guest speaker
aRandomNumber = randint(0,4) #randint is a built in function that
                             #takes in a start and end
print("The random number generator chose: %d" %(aRandomNumber))

randomGuestSpeaker = womenInTech [aRandomNumber]
print(randomGuestSpeaker)


anExample = "Apo!"
print(len(anExample))
#Output: 4
print("A" in anExample)
#Output:True
print(anExample[0])
#Output: A
print(anExample[1]+ anExample[2]+ anExample[3])
# Output: po
