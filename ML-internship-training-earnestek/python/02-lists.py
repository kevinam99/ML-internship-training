list1 = [2,4,5,6,72,17,54,1,3,2,2,44]

print(list1[2])
print(list1[1:3])
print(list1[:3])
print(list1[3:])
print(list1[-1])

print(len(list1))

list1.append(69)

print (list1)

list1.extend([3,4])
''' 
list1.extend('yes')#stores as 'y', 'e', 's'
print (list1)
list1.extend(['yes'])#stores as 'yes'
print (list1)
list1.extend(["yes"])
print (list1)

 '''
list1.insert(1,55)#(index, element)
print(list1)

print(list1.index(72))#value to be located, value MUST EXIST in the list
print(list1.index(2))

del (list1[5])
print(list1)

list1.sort()
print(list1)