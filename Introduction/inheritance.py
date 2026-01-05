# Example from youtube
# General and Particular rule in programming
# "General" refers to a broad concept or rule, 
# while "Particular" refers to a specific instance or detail of that concept

class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def double_speed(self):
        self.speed *= 2

    def take_damage(self, amount):
        self.health -= amount


class Warrior(Character):
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed) #avoid to overwrite the parent __init__
        self.toughness_modifier = 0.90

    def take_damage(self, amount):
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)


warrior = Warrior(100, 50, 10)
print(f'Initial health: {warrior.health}')

warrior.take_damage(40)
print(f'Health after damage: {warrior.health}')

        

