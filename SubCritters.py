from Critter import Critter
from time import sleep

class Dog(Critter):

    def eatNoise(self):
        i = 1
        while i <= 3:
            sleep(1)
            print('bark!')
            i += 1

    def sleepNoise(self):
        i = 1
        while i <= 3:
            sleep(1)
            print('zWoofz')
            i += 1

    def exerciseNoise(self):
        i = 1
        while i <= 3:
            sleep(1)
            print('Woof')
            i += 1


class Cat(Critter):

    def eatNoise(self):
        i = 1
        while i <= 3:
            sleep(1)
            print('Prr')
            i += 1

    def sleepNoise(self):
        i = 1
        while i <= 3:
            sleep(1)
            print('zPrrz')
            i += 1

    def exerciseNoise(self):
        i = 1
        while i <= 3:
            sleep(1)
            print('Meow')
            i += 1

class Rat(Critter):

    def eatNoise(self):
        from time import sleep
        i = 1
        while i <= 3:
            sleep(1)
            print('Nom')
            i += 1

    def sleepNoise(self):
        from time import sleep
        i = 1
        while i <= 3:
            sleep(1)
            print('zSqueakz')
            i += 1

    def exerciseNoise(self):
        from time import sleep
        i = 1
        while i <= 3:
            sleep(1)
            print('Squeak')
            i += 1
