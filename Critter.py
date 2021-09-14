class Critter:
    __isAlive = True
    __foodLevel = 5
    __tiredness = 0

    def isAlive(self):
        return self.__isAlive

    def __die(self):
        self.__isAlive = False

    def sleep(self):
        print('Critter sleeps.')
        self.__tiredness = 0
        self.__foodLevel -= 3
        if (self.__foodLevel <= 0):
            print('Critter starves to death.')
            self.__die()

    def feed(self):
        if self.__isAlive:
            print('Critter eats.')
            self.__foodLevel += 1
            self.__tiredness += 1
            if self.__foodLevel > 10:
                print('Critter over ate')
                self.__die()
            elif self.__tiredness > 5:
                print('Critter is sleepy from so much food.')
                self.sleep()
                # this is a test
