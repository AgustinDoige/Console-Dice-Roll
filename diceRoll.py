"""
Objective:
Make a program that will take a command like "2d12" and roll two twelve-sided dice.
Also allow it to take a command like "4d6x4", and roll four six-sided dice, four times.
Finally, also something like "4d6x4&2d6"
"""
from random import randint as rr

class Dice:
    def __init__(self,st):
        temp = st.split("d")
        self.sides = int(temp[1])
        self.amount = int(temp[0])
        self.name = st
    
    def roll(self):
        res = []
        for _ in range(self.amount):
            res.append(rr(1,self.sides))
        return res

    def info(self):
        return (self.name,self.sides,self.amount)

def roller(tst):
    a = tst.split("x")
    if (len(a)>1):
        repeat = int(a[-1])
        b = a[0]
        del a
    else:
        repeat = 1
        b = a[0]
        del a
    
    c = b.split("&")
    dd = []
    for rollCall in c:
        dd.append(Dice(rollCall))

    for i in range(1,repeat+1):
        print("x{}:".format(i))
        for dice in dd:
            print(dice.name, dice.roll())


def main():
    man = "AdB -> roll A amount of B-sided dice\nAdBxC -> roll A amount of B-sided dice C times\nAdB&CdD&...xN -> roll AdB&N and also CdDxN and so on..."
    print(man)
    inp = input("Write Roll:\t")
    roller(inp)

main()