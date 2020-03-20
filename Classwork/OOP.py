#3-16-2020

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.color = color


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)


# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print()
print()
print(p.x, p.y)
print(q.x, q.y)

p.x = 4
p.y = 8
print('p.x',p.x, 'p.y', p.y)
print(q.x, q.y)

#print(p is q)
