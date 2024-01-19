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
    
class Grid:
    def __init__(self):
        self.input = input
        self.dice = [random.randint(1, 6) for i in range(9)]
        self.dice.sort(reverse=True)
        self.diagonal = self.get_diagonal()
        self.balanced = self.get_balanced()


    def get_balanced(self):
        self.balanced_grid = [
            [self.dice[1], self.dice[5], self.dice[2]],
            [self.dice[7], self.dice[0], self.dice[8]],
            [self.dice[3], self.dice[6], self.dice[4]]]
        
        scores = [sum(self.balanced_grid[x]) for x in range(3)]
        scores += [sum(self.balanced_grid[x][y] for x in range(3)) for y in range(3)]
        scores.append(sum(self.balanced_grid[x][x] for x in range(3)))
        scores.append(sum(self.balanced_grid[x][2-x] for x in range(3)))
        scores.sort(reverse=True)
        return scores[:-2]



    def get_diagonal(self):
        self.diagonal_grid = [
            [self.dice[1], self.dice[5], self.dice[4]],
            [self.dice[7], self.dice[0], self.dice[8]],
            [self.dice[3], self.dice[6], self.dice[2]]]
        
        scores = [sum(self.diagonal_grid[x]) for x in range(3)]
        scores += [sum(self.diagonal_grid[x][y] for x in range(3)) for y in range(3)]
        scores.append(sum(self.diagonal_grid[x][x] for x in range(3)))
        scores.append(sum(self.diagonal_grid[x][2-x] for x in range(3)))
        scores.sort(reverse=True)
        return scores[:-2]
    
    def __str__(self):
        s = f'''
Dice rolled: {self.dice}

Max Diagonal:
{self.diagonal_grid[0][0]} | {self.diagonal_grid[0][1]} | {self.diagonal_grid[0][2]}
--+---+--
{self.diagonal_grid[1][0]} | {self.diagonal_grid[1][1]} | {self.diagonal_grid[1][2]}
--+---+--
{self.diagonal_grid[2][0]} | {self.diagonal_grid[2][1]} | {self.diagonal_grid[2][2]}
{self.diagonal}

Balanced:
{self.balanced_grid[0][0]} | {self.balanced_grid[0][1]} | {self.balanced_grid[0][2]}
--+---+--
{self.balanced_grid[1][0]} | {self.balanced_grid[1][1]} | {self.balanced_grid[1][2]}
--+---+--
{self.balanced_grid[2][0]} | {self.balanced_grid[2][1]} | {self.balanced_grid[2][2]}
{self.balanced}
'''
        return s