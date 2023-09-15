box_0 = []
box_1 = ['necklace', 'star', 'hat', 'octopus']
box_2 = ['telescope', 'car', 'pot', 'motorcycle']
box_3 = ['butterfly', 'skirt', 'headphone', 'perfume']
box_4 = ['razor']
box_5 = []
box_6 = []
box_7 = ['tree']
box_8 = []
box_9 = ['glove', 'note', 'earring', 'rain']

# Replace the doll and the tree and the fridge with the star and the hat and the octopus in Box 2
box_2.remove('doll')
box_2.remove('tree')
box_2.remove('fridge')
box_2.extend(['star', 'hat', 'octopus'])

# Move the pot and the motorcycle from Box 6 to Box 2
box_6.remove('pot')
box_6.remove('motorcycle')
box_2.extend(['pot', 'motorcycle'])

# Swap the shorts in Box 6 with the wallet in Box 5
box_6.remove('shorts')
box_5.remove('wallet')
box_6.append('wallet')
box_5.append('shorts')

# Remove the plane from Box 8
box_8.remove('plane')

# Remove the seaweed and the lock from Box 1
box_1.remove('seaweed')
box_1.remove('lock')

# Remove the thunder from Box 3
box_3.remove('thunder')

# Swap the rain in Box 9 with the rocket in Box 1
box_9.remove('rain')
box_1.remove('rocket')
box_9.append('rocket')
box_1.append('rain')

# Empty Box 5
box_5.clear()

# Replace the butterfly and the skirt with the headphone and the perfume in Box 3
box_3.remove('butterfly')
box_3.remove('skirt')
box_3.extend(['headphone', 'perfume'])

# Replace the bowl with the tree in Box 7
box_7.remove('bowl')
box_7.append('tree')

# Move the pot and the car from Box 2 to Box 1
box_2.remove('pot')
box_2.remove('car')
box_1.extend(['pot', 'car'])

# Remove the rocket and the glove from Box 9
box_9.remove('rocket')
box_9.remove('glove')

# Replace the wallet with the bus in Box 6
box_6.remove('wallet')
box_6.append('bus')

# Swap the car in Box 1 with the motorcycle in Box 2
box_1.remove('car')
box_2.remove('motorcycle')
box_1.append('motorcycle')
box_2.append('car')

# Move the bus from Box 6 to Box 9
box_6.remove('bus')
box_9.append('bus')

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