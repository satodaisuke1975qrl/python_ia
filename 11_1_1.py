class Character:

    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    def show_profile(self):
        print(self.name)
        print(self.age)
        print(self.speed)


class Magician(Character):

    # __init__も上書きできます
    def __init__(self, name, age, speed, magic_power):
        super().__init__(name, age, speed)
        self.magic_power = magic_power

    def show_profile(self):
        # print(self.name)
        # print(self.age)
        # print(self.speed)
        # 上の3行は、Characterのshow_profileメソッドで同様のことをしているので、
        # それを呼び出すほうが楽
        super().show_profile()
        print(self.magic_power)

class Musician(Character):

    def __init__(self, name, age, speed, musical_power):
        super().__init__(name, age, speed)
        self.musical_power = musical_power

    def show_profile(self):
        super().show_profile()
        print(self.musical_power)

phoebe = Magician('phoebe', 28, 100, 'motion_sickness')
phoebe.show_profile()

porter = Musician('porter', 32, 200, 'something_conforting')
porter.show_profile()
