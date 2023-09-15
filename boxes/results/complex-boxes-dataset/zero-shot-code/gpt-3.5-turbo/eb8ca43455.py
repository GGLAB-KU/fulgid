box_0 = []
box_1 = ['horse', 'puzzle', 'earring', 'desert', 'comet']
box_2 = []
box_3 = ['note', 'controller', 'mountain', 'lipstick']
box_4 = ['shampoo']
box_5 = ['scarf']
box_6 = ['lock', 'coral', 'planet', 'key']
box_7 = ['drum', 'shoes', 'bag', 'perfume', 'moon']
box_8 = []

# Put the car into Box 3
box_3.append('car')

# Remove the shampoo from Box 4
box_4.remove('shampoo')

# Put the microscope and the river into Box 7
box_7.extend(['microscope', 'river'])

# Remove the scarf from Box 5
box_5.remove('scarf')

# Put the lightning and the storm into Box 1
box_1.extend(['lightning', 'storm'])

# Put the wallet and the elephant and the glasses into Box 3
box_3.extend(['wallet', 'elephant', 'glasses'])

# Move the desert and the earring from Box 1 to Box 4
box_4.extend(['desert', 'earring'])
box_1.remove('desert')
box_1.remove('earring')

# Swap the perfume in Box 7 with the coral in Box 6
box_7.remove('perfume')
box_6.remove('coral')
box_7.append('coral')
box_6.append('perfume')

# Replace the perfume and the planet with the pillow and the island in Box 6
box_6.remove('perfume')
box_6.remove('planet')
box_6.extend(['pillow', 'island'])

# Move the island and the key from Box 6 to Box 4
box_4.extend(['island', 'key'])
box_6.remove('island')
box_6.remove('key')

# Put the key and the submarine and the desert into Box 5
box_5.extend(['key', 'submarine', 'desert'])

# Put the jacket and the plane and the storm into Box 4
box_4.extend(['jacket', 'plane', 'storm'])

# Move the earring from Box 4 to Box 5
box_5.append('earring')
box_4.remove('earring')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)