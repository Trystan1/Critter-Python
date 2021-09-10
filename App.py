from Critter import Critter

def main():
    bob = Critter()
    while bob.isAlive():
        action = input('What would you like Critter to do?')
        if action == 'eat':
            bob.feed()
        elif action == 'sleep':
            bob.sleep()
    print('Critter has died.')

if __name__ == '__main__':
    main()
