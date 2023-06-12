class Pokemon:

    def __init__(self, name):
        self.name = name

    def race_value(self, hp, offence, defence, s_offence, s_defence, speed):
        print(self.name, hp, offence, defence, s_offence, s_defence, speed)


garchomp = Pokemon('garchomp')
garchomp.race_value(hp=108, offence=130, defence=95, s_offence=80, s_defence=85, speed=102)

print(garchomp.race_value)