# Test for text based combat

class Monster:
    """A monster to be attacked."""

    def __init__(self, name, health):
        self.name = name
        self.health = health
    def __delete__(self, instance):
        print("It's remnants wither away.")
        del self.name
        del self.health

class Player:
    """Stats for the player."""

    def __init__(self, health, power):
        self.health = health
        self.power = power

class NoMonster(Exception):
    pass


user_char = Player(100, 10)
monster_list = []

def get_monster(name):
    """Returns Monster instance for \"name\" """

    monster = []
    for ii in range(len(monster_list)):
        if monster_list[ii].name == name:
            monster.append(monster_list[ii])
            break
    if len(monster) == 0:
        raise NoMonster
    else:
        return monster[0]

def spawn(name, health):
    """Spawns a monster."""

    try:
        get_monster(name)
        print("That monster already exists.")
    except NoMonster:
        monster = Monster(name, health)
        monster_list.append(monster)
        print("{} arrives with {} health.".format(monster.name, monster.health))

def attack(name):
    """Attack a monster."""

    try:
        monster = get_monster(name)
        monster.health = monster.health - user_char.power
        print("{} took {} damage.".format(monster.name, user_char.power))
        if monster.health <= 0:
            print("{} has been defeated!".format(monster.name))
            monster_list.remove(monster)
            del monster
        else:
            print("{} has {} health left.".format(monster.name, monster.health))
    except NoMonster:
        print("That monster doesn't exist.")


while True:
    try:
        eval(input('\n> Make a move: '))
    except NameError:
        print('Action not recognized.')
