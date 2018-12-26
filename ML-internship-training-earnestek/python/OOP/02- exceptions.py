import sys
relist = [1,0,3.4]

''' for i in relist:
    if i == 0:
        continue
    print(10/i)
     '''
for i in relist:
    try:
        print("The element is ", i)
        result = 10/(int(i))
        print(f"Result = {result}")
    except:
        print(f"Got an error ")
