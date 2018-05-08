from oops.interitance.Enemy import Troll,Vampyre

ugly_troll = Troll("pug")

print("ugly troll - {}".format(ugly_troll));

another_troll = Troll("ug")
print("antoher troll - {}".format(another_troll))

vamp = Vampyre("Vlad")
print (vamp)

print ("-" *  40)

while vamp.alive:
    vamp.take_damage(1)
    print (vamp)
    
