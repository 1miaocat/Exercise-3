# Exercise 3


avogadro_num = 6.022*(10**23)

def num_atoms(amount_in_grams, atomic_weight = 196.97):
    mole = amount_in_grams / atomic_weight
    number_of_atoms = mole * avogadro_num
    return number_of_atoms

print(num_atoms(10))
print(num_atoms(10, 12.001))
print(num_atoms(10, 1.008))
