from Critter import Critter
from time import sleep

class Dog(Critter):

    def eatNoise(self):
        print('bark!')

    def sleepNoise(self):
        print('zWoofz')

    def exerciseNoise(self):
        print('Woof')

class Cat(Critter):

    def eatNoise(self):
        print('Prr')

    def sleepNoise(self):
        print('zPrrz')

    def exerciseNoise(self):
        print('Meow')

class Rat(Critter):

    def eatNoise(self):
        print('Nom')

    def sleepNoise(self):
        print('zSqueakz')

    def exerciseNoise(self):
        print('Squeak')