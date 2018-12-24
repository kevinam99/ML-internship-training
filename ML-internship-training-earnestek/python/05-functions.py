#Functions
a = 10
def printNameAndMessage(name, msg):
    print(f"Hello {name}, The message for you is {msg}")

def funnc():
    #print commentge
    '''block comm'''
    print("yeah!")
    global a
    print(a)

    
def addNums(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

#When number of args is unknown

print(addNums(5,4,3,2,1)) #passing a tuple as an arg

#print(funnc.__doc__)
funnc()
printNameAndMessage("Nolan", "Thank you for your movies")