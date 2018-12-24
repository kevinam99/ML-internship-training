#tuple description
my_tuple = (1, 'hello', 4.0, [1,2,3], ('test'))

string_tup = ('hello', 1)
print(string_tup)

#accessing nested elements in a tuple

print(my_tuple[3][1])
#find element in tuple

print (1 in my_tuple) #returns a boolean value

#count total occurence of an element in a tuple

totalOccurences = my_tuple.count(1) #to find element 1

print (totalOccurences)