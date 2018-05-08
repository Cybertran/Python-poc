class Kettle(object):
 power_source = "electricity"

 def __init__(self,make,price):
    self.make = make
    self.price = price
    self.on = False

def switch_on(self):
    self.on=True

kenwood = Kettle("kenwood",8.90)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.5
print(kenwood.price)

hemilton = Kettle("Hemilton",14.54)

print(hemilton.price)
print(hemilton.make)
print("Models : name = {0.make} and price =  {0.price}".format(kenwood))

#kenwood.power = 150 # instance variable avaible only in kenwood
#print(hemilton.power)

print(Kettle.power_source)
print(hemilton.power_source)

print(kenwood.__dict__)
