from random import choice
n=int(input('enter number of players:'))
l1=[]
i=0
while(i<=n):
    name=input('enter player name:')
    if name.isalpha():
        l1.append(name)
        i=i+1
    else:
        print('enter only names')
        i=i+0
l2=[]
l3=[]
for i in range(1,(len(l1)+1)):
    l2.append(i)

for i in range(len(l2)):
               k=choice(l2)
               l3.append(k)
               l2.remove(k)
z=zip(l1,l3)
result=sorted(z,key=lambda x:x[1])
print('batting order:')
for (a,b) in result:
    print(a,b)
