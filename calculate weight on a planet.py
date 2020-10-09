#Exercise 2
gravity_of_earth = 9.8

def calc_weight_on_planet(weight_on_earth, gravity_of_planet = 23.1):
    mass = weight_on_earth / gravity_of_earth
    effective_weight = mass * gravity_of_planet
    return effective_weight

print(calc_weight_on_planet(120, 23.1))
