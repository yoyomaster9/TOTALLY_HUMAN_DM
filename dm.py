import random
import re

class Roll:
    def __init__(self, input):
        self.input = input
        self.simulate()

    def simulate(self):
        # use above code to simulate roll
        # will return a string, and set values
        # self.output & self.result
        l = [x for x in re.split('(d)|(kh)|(kl)', self.input) if x != None]
        l = ['1' if x == '' else x for x in l]
        n = int(l[l.index('d') - 1])
        s = int(l[l.index('d') + 1])
        self.rolls = [random.randint(1, s) for x in range(n)]

        if 'kh' in l or 'kl' in l:
            self.keeps = []
            if 'kh' in l:
                max_n = int(l[l.index('kh') + 1])
                self.keeps += sorted(self.rolls)[-max_n:]
            if 'kl' in l:
                min_n = int(l[l.index('kl') + 1])
                self.keeps += sorted(self.rolls)[:min_n]
        else:
            self.keeps = self.rolls.copy()
        self.result = sum(self.keeps)
        
    def __str__(self):
        s = ', '.join(f'~~{x}~~' for x in self.rolls)
        for x in self.keeps:
            s = s.replace(f'~~{x}~~', str(x), 1)
        return f'{self.input}({s}) = `{self.result}`'

    def __repr__(self):
        return self.__str__()