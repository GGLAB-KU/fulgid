box_0 = ['toothbrush', 'flower', 'scissors']
box_1 = ['console', 'key', 'tiger', 'tree']
box_2 = ['grinder', 'cloud', 'thunder']
box_3 = ['keyboard', 'octopus', 'soap', 'hat']
box_4 = ['moon', 'pot', 'boot', 'polish']
box_5 = ['bag']
box_6 = []
box_7 = ['car', 'oven', 'submarine', 'ring', 'jungle']
box_8 = ['bell']
box_9 = ['cow', 'sandals', 'toy', 'makeup', 'shelf']
box_10 = ['dolphin', 'lightning', 'dress', 'planet', 'bowl']
box_11 = ['headphone', 'charger']

# Replace the bowl with the horse in Box 10
box_10[4] = 'horse'

# Put the flower and the bird into Box 3
box_3.extend(['flower', 'bird'])

# Swap the bag in Box 5 with the scissors in Box 0
box_0.remove('scissors')
box_5.remove('bag')
box_0.append('bag')
box_5.append('scissors')

# Replace the bell with the basket in Box 8
box_8.remove('bell')
box_8.append('basket')

# Remove the pot from Box 4
box_4.remove('pot')

# Swap the octopus in Box 3 with the sandals in Box 9
box_3.remove('octopus')
box_9.remove('sandals')
box_3.append('sandals')
box_9.append('octopus')

# Remove the scissors from Box 5
box_5.remove('scissors')

# Replace the submarine and the jungle with the blender and the tie in Box 7
box_7.remove('submarine')
box_7.remove('jungle')
box_7.append('blender')
box_7.append('tie')

# Move the basket from Box 8 to Box 6
box_8.remove('basket')
box_6.append('basket')

# Put the leaf into Box 10
box_10.append('leaf')

# Put the lion and the chair into Box 9
box_9.extend(['lion', 'chair'])

# Replace the moon with the necklace in Box 4
box_4.remove('moon')
box_4.append('necklace')

# Move the flower from Box 0 to Box 3
box_0.remove('flower')
box_3.append('flower')

# Empty Box 4
box_4 = []

# Replace the tie and the car and the oven with the toy and the dice and the rocket in Box 7
box_7.remove('tie')
box_7.remove('car')
box_7.remove('oven')
box_7.append('toy')
box_7.append('dice')
box_7.append('rocket')

# Remove the charger and the headphone from Box 11
box_11.remove('charger')
box_11.remove('headphone')

# Replace the basket with the drum in Box 6
box_6.remove('basket')
box_6.append('drum')

# Put the magnet and the dice and the grass into Box 1
box_1.extend(['magnet', 'dice', 'grass'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)
print("Box 10:", box_10)
print("Box 11:", box_11)