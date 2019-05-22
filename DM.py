import random

def roll(s): # Simulates rolls of the form #d#+#d#..
    l = []
    s = s.lower()
    for i in s.split('+'):
        try:
            if i[0] == 'd':
                i = '1' + i
        except:
            i = '1' + i
        [n, max] = [int(x) for x in i.split('d')]
        for j in range(n):
            l.append(random.randint(1, max))
    return l

#
# class Player():
#     def __init__(self):
