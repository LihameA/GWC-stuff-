# Calculating the average, pseudo code in notebook

#Step 1: Find the sum
'''
ages = [2,22,16,4,17]
sum = 0
for age in ages:
     sum += age

#Print sum to verify that it is correct
print("The sum of all ages is %d"%(sum))

 #Divide by length
average = sum/len(ages)

print("The avergae age is %d" %(average))
'''

#This program will create a list of ages (through user input)AND calculates the averages

#This is a list that will store that will store all of teh users names
listOfAges = []

#This is a variable that acts as a counter for how many ages are in the list
numberOfAges = 0

#This will output 6 numbers (elements) because its starting at 0 (index) if i
#put it at 1 then it would print 5 b/c index would than be 1

while (numberOfAges <=5):
    #This retrieves user input and store it into a variable called 'age'
    age = input("Please enter an age:")
    age = int(age)
    print(age)
    listOfAges.append(age)
    numberOfAges+=1

print("Here is your list: ")
print(listOfAges)
#Calculating the ages 
