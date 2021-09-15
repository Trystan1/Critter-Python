# from Food import Food
from time import sleep

class Critter:

    __isAlive = True
    __hasWon = False
    __foodLevel = 5
    __tiredness = 0
    __exercise = 5

    def __init__(self, name):
        self.name = name

    def isAlive(self):
        return self.__isAlive

    def __die(self):
        self.__isAlive = False

    def __victory(self):
        self.__hasWon = True

    def hasWon(self):
        return self.__hasWon

    def sleeps(self):
        print(f'{self.name} sleeps.')
        i = 1
        while i <= 3:
            sleep(1)
            self.sleepNoise()
            i += 1

        self.__tiredness = 0
        self.__foodLevel -= 3
        self.__exercise -= 1
        if self.__foodLevel <= 0:
            print(f'{self.name} starves to death.')
            self.__die()

    def feed(self):

        if self.__isAlive:
            print(f'{self.name} eats.')
            i = 1
            while i <= 3:
                sleep(1)
                self.eatNoise()
                i += 1

            self.__foodLevel += 1
            self.__tiredness += 1
            if self.__foodLevel > 10:
                print(f'{self.name} over ate')
                self.__die()
            elif self.__tiredness > 5:
                print(f'{self.name} is sleepy from so much food.')
                self.sleeps()

    def exercise(self):

        if self.__isAlive:
            print(f'{self.name} exercises.')
            i = 1
            while i <= 3:
                sleep(1)
                self.exerciseNoise()
                i += 1

            self.__exercise += 6
            self.__foodLevel -= 1
            self.__tiredness += 2
            if self.__exercise >= 10:
                self.__victory()
            elif self.__exercise <= 0:
                print(f'{self.name} has wasted away from lack of exercise')
                self.__die()

    def display(self):
        print(f'Food: {self.__foodLevel} \nTiredness: {self.__tiredness} \nExercise: {self.__exercise}')