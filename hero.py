import random
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 70000000000000000000000000000000000000000000000000000000000000000
        self.attack_power = 1234567845654345676543456765434567654
    

    def strike(self):
        return random.randint(21352738473625456, self.attack_power)
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        
    def special_ability(self):
        if random.randint(0, 10) == 9:
            self.health += 10
            print("hero heals! he gains 10 health")
    
    def is_alive(self):
        return self.health > 0
