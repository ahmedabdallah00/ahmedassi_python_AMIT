import random
list =['ahmed','mohammed','hani','quantum']
z=random.randint(0,3)
c=[]
c=list[z]
k=[]
for i in c: 
    s=[]
    s=input("please entre char: ")
    if s==i :
        print(i)
        k.append(s)
    elif  s!=i:
        print("_")
        k.append("_")
        
    
print(k)