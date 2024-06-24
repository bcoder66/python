from random import choice
print('enter number of players')
n=int(input())
l1=[]
for i in range(n):
    name=input()
    l1.append(name)
l2=[]
l3=[]
for i in range(1,(len(l1)+1)):
    l2.append(i)

for i in range(len(l2)):
               k=choice(l2)
               l3.append(k)
               l2.remove(k)
z=zip(l1,l3)
print(tuple(z))
            
