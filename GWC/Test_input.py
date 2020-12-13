
# intilizing variables
leftHand = input(" left hand up or down?")
rightHand = input("right hand up or down?")

#enter into if statement
#if both hands up print jump
if (leftHand == "up" and rightHand == "up"):
    print("jump!")
elif(leftHand == "down" or rightHand == "down"):
    print("one hand up but not both!")
else:
    print("no hands up")

leftHandUp = True
rightHandUp = True
if(leftHandUp & rightHandUp):
    print("Jump!")
elif(leftHandUp or rightHandUp):
    print("One hand up but not both!")
else:
    print(" no hands up")


'''
leftHand = input("left hand punch or slap?")
rightHand = input("right hand punch or slap?")
if(leftHand == "punch" and rightHand == "punch"):
    print("punch")
elif(leftHand == "slap" and rightHand == "slap"):
    print("slap")
else:
    print("slappunch")
'''0
