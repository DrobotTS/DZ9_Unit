# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здоровья.
# Юнит может учеличить навык силы, ловкости и интелекта на 1 балл. Возможный максимум 10.
#
# Реализовать класс Unit, с нужным функционалом.


class UnitGame:

    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.power = 1
        self.dexterity = 1
        self.intellect = 1

    def __str__(self):
        return f"name: {self.name}, " \
               f"clan: {self.clan}, " \
               f"health: {self.health}, " \
               f"power: {self.power}, " \
               f"dexterity: {self.dexterity}, " \
               f"intellect: {self.intellect}"

    def __repr__(self):
        return f"{self.name} - {self.health}"

    def treatment_unit(self):
        if 10 <= self.health <= 90:
            self.health += 10
        elif self.health == 0:
            return "Game over"
        else:
            return "Full health"

    def power_unit(self):
        self.power += 1 if 0 < self.power < 10 else print("Check your power")

    def dexterity_unit(self):
        self.dexterity += 1 if 0 < self.dexterity < 10 else print("Check your dexterity")

    def intellect_unit(self):
        self.intellect += 1 if 0 < self.intellect < 10 else print("Check your intellect")

    # def clan_unit(self):
    #     if self.clan == "standart" or self.clan == "soldier" or self.clan == "scientist":
    #         return f"{self.name} - {self.clan}"
    #     else:
    #         return "Check your clan"
