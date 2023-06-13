class Character:

    def __init__(self, name, inst):
        self.name = name
        self.__inst = inst

    @property
    def instrument(self):
        return self.__inst

    @instrument.setter
    def instrument(self, new_gear):
        self.__inst = new_gear
        return '30'


matty = ('matty', 'vocal')
print(matty.inst)









