dict1 = {'a': 'apple', 'b': 'ball', 'l': 'test'}
dict2 = {'nonest': 'not nested', 'nest': {1: 'num1', 2: 'num2'}}
#access a value for a given key
print(dict1['b'])

print(dict1.get('b'))

#change the value for a key
dict1['b'] = 'bat'

var2 = dict2.get('nest')
print(var2.get(2))