import random
class Enemy:

    def __init__(self, name="Enemy", hit_point=0, lives=1):
        self.name = name
        self.hit_point = hit_point
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_point = self.hit_point - damage
        if remaining_point >= 0:
            self.hit_point = remaining_point
            print("I took {} point damage")
        else:
            self.lives -= 1
            if self.lives > 0:
                print ("{0.name} lost a life".format(self))
            else:
                print ("{0.name} is dead".format(self))
                self.alive=False

    def __str__(self):
        return "Name: {0.name},Lives: {0.lives},hit points : {0.hit_point}".format(self)

class Troll(Enemy):
    def __init__(self, name):
        #super(Troll, self).__init__(name=name,lives=1,hit_point=23)
        super(Troll, self).__init__(name=name,lives=1,hit_point=23)


class Vampyre(Enemy):
    def __init__(self,name):
       super(Vampyre, self).__init__(name=name,lives=3,hit_point=12)

    def dodges(self):
        if random.randint(1,3) == 3:
            print ("********* {0.name} ***********".format(self))
            return True
        else:
            return False
    def take_damage(self, damage):
        if not self.dodges():
            super(Vampyre, self).take_damage(damage=damage)


