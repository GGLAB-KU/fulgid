box_0 = ['butterfly', 'speaker']
box_1 = ['grass', 'fish']
box_2 = ['microwave', 'glove', 'leaf']
box_3 = ['scarf', 'shark', 'glasses']
box_4 = ['pot', 'sock', 'card', 'earring', 'thunder']

# Put the polish and the dog into Box 0
box_0.extend(['polish', 'dog'])

# Put the beach and the controller and the truck into Box 3
box_3.extend(['beach', 'controller', 'truck'])

# Put the starfish into Box 1
box_1.append('starfish')

# Remove the pot and the card from Box 4
box_4.remove('pot')
box_4.remove('card')

# Swap the earring in Box 4 with the truck in Box 3
box_4.remove('earring')
box_3.remove('truck')
box_4.append('truck')
box_3.append('earring')

# Replace the starfish and the fish and the grass with the dress and the console and the blender in Box 1
box_1.remove('starfish')
box_1.remove('fish')
box_1.remove('grass')
box_1.extend(['dress', 'console', 'blender'])

# Replace the glove with the skirt in Box 2
box_2.remove('glove')
box_2.append('skirt')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)