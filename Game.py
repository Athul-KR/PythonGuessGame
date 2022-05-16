import random as r

rndnum = r.randint(100, 999)
print(rndnum)
rndnum = str(rndnum)

def guess():
    def call(rndnum):
        num = input("Enter the Number \n")
        if (num == rndnum):
            print("Correct !!!  \n Random numb is ", rndnum)
            exit()
        count = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if (num[j] == rndnum[i]):
                    count = count + 1
                    break
        postn = 0
        for i in range(0, 3):
            if (num[i] == rndnum[i]):
                postn = postn + 1
        return (count, postn)


    for i in range(0, 3):
        count, postn = call(rndnum)
        print(count, "Number Correct and ", postn, " number in correct position \n")
guess()
for i in range(0,3):
    print("Do You Want To Play Again?? ")
    re=input("yes or no ")
    if (re == 'y'):
        guess()
    else:
        print("THANK YOU FOR PLAYING ")
        break
