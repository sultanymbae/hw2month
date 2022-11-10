class Hero:
    head = 1
    ability = True

    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage

    def heal(self):
        self.hp += 100

    def two_damage(self):
        self.damage *= 2

    def greetings(self):
        print(f'my name is {self.name}')

    def brand_phrase(self):
        print('good will win')


hero1 = Hero(name='Karl', nickname='Invoker', hp=780, damage=60)
hero2 = Hero(name='Pudge', nickname='Butcher', hp=800, damage=90)
hero3 = Hero(name='Gustavo', nickname='Gus', hp=1000, damage=200)
hero4 = Hero(name='Luffy', nickname='King', hp=700, damage=150)

hero1.heal()
print(hero1.hp)
hero2.two_damage()
print(hero2.damage)
hero3.greetings()
hero4.brand_phrase()


class Air(Hero):
    wings = 2

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')

    def __Gen_x(self):
        pass


class Space(Hero):
    tentacles = 12

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')

    def __Gen_x(self):
        pass


class Earthly(Hero):
    legs = 2

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')

    def __Gen_x(self):
        pass


hero1 = Air(name='Karl', nickname='Invoker', hp=780, damage=60)
hero2 = Space(name='Pudge', nickname='Butcher', hp=800, damage=90)
hero3 = Earthly(name='Gustavo', nickname='Gus', hp=1000, damage=200)
hero1.brand_phrase()
