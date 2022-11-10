import random
while(True):
    rand1=random.randint(1,50)
    rand2=random.randint(1,50)
    ans=int(input('what is '+str(rand1)+'+'+str(rand2)+'?\n'))
    if( ans == (rand1+rand2)):
        print("The answer is \nNext Question correct:\n")
    else:
        print("Game Over\n")
        break