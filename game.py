from random import choice
print('lets start the game')
l=['rock','paper','scisor']
a=input('enter your choice:')
if a  not in l:
    print('please enter anyone of these',l)
else:
    b=choice(l)
    print('computer choice is:',b)
    if (a=='rock' and b=='paper') or (a=='paper' and b=='scisor') or (a=='scisor' and b=='rock'):
        print("computer won the game")
    elif (a=='rock' and b=='scisor') or ( a=='paper' and b=='rock') or (a=='scisor' and b=='paper'):
        print('you won the game')
    else:
        print('match tied')
