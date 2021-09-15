from SubCritters import *

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
        elif action == 'sleep':
            bob.sleeps()
        elif action == 'exercise':
            bob.exercise()
        bob.display()

    if bob.hasWon():
        print(f'{name} has reached peak physical fitness.')
        print(f'{name} has achieved victory')
    else:
        print(f'{name} has died.')

if __name__ == '__main__':      # if I have started running my code from this file then run the function
    main()
