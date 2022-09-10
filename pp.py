'''
yasser={'friends':["Assem","Zakii","Amr"],'family':['MOna','bcnb','vb']}
print(yasser['friends'][1])
'''

'''x1=int(input())'''
'''
if x != x1 : 
    print("not equal")
    if x <x1:
        print("x1 greater than x")
    elif x>x1:
        print("x greater than x1")    
else:
    print("equal")    
'''
'''
arr=[1,11,20,45,2,3,5,10]
x=0
for x in arr:
    if(x%2 ==0):
        print(x)
'''

'''
def maxfunc(x,y):
    if(x>y):
        print("x is greater y ")
        return x
    elif(y>x):
        print("x is greater y ")
        return y 

x=maxfunc(5,8)
print(x)
'''
from Car import Car
from Cat import Cat
c=Car()
c.print_data()
c1=Car()
c1.print_data()

c2=Cat()
c2.print_meow()

