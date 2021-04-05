user = int(input("Sag eine Zahl "))

n = user
before = 1
be_before = 0
tot = 0
answer = 0


def num_ways():
    global tot, be_before, before
    
    tot = before + be_before
    be_before = before
    before=tot
    return tot


for x in range(n):
  answer = num_ways()


print(answer)






