from SubCritters import Dog
from SubCritters import Cat
from SubCritters import Rat

def main():

    critterType = str(input(f'what type of Critter would you like?: '))
    name = str(input('Name your Critter: '))

    if critterType == 'Dog':
        bob = Dog(name)
    elif critterType == 'Cat':
        bob = Cat(name)
    elif critterType == 'Rat':
        bob = Rat(name)

    while bob.isAlive() and bob.hasWon() != True:
        action = input(f'What would you like {name} to do?')
        if action == 'eat':
            bob.feed()
            bob.eatNoise()
        elif action == 'sleep':
            bob.sleeps()
            bob.sleepNoise()
        elif action == 'exercise':
            bob.exercise()
            bob.exerciseNoise()
        bob.display()
    if bob.hasWon():
        print(f'{name} has achieved victory')
    else:
        print(f'{name} has died.')

if __name__ == '__main__':
    main()
