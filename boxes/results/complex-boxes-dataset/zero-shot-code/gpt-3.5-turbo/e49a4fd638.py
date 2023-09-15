box_0 = ['skirt']
box_1 = ['grinder', 'apple', 'watch']
box_2 = []
box_3 = ['mask', 'glasses']
box_4 = ['ring', 'sandals']
box_5 = ['coat', 'doll', 'basket']
box_6 = ['grass', 'umbrella']
box_7 = ['shampoo', 'fork']
box_8 = ['bag', 'keyboard', 'bird', 'star']

# Put the tree into Box 3
box_3.append('tree')

# Replace the grinder with the needle in Box 1
box_1.remove('grinder')
box_1.append('needle')

# Swap the star in Box 8 with the sandals in Box 4
box_8.remove('star')
box_4.remove('sandals')
box_8.append('sandals')
box_4.append('star')

# Remove the fork and the shampoo from Box 7
box_7.remove('fork')
box_7.remove('shampoo')

# Swap the grass in Box 6 with the doll in Box 5
box_6.remove('grass')
box_5.remove('doll')
box_6.append('doll')
box_5.append('grass')

# Move the skirt from Box 0 to Box 5
box_0.remove('skirt')
box_5.append('skirt')

# Remove the umbrella from Box 6
box_6.remove('umbrella')

# Move the bag from Box 8 to Box 5
box_8.remove('bag')
box_5.append('bag')

# Put the brush and the game into Box 6
box_6.extend(['brush', 'game'])

# Remove the coat and the basket and the skirt from Box 5
box_5.remove('coat')
box_5.remove('basket')
box_5.remove('skirt')

# Replace the needle with the card in Box 1
box_1.remove('needle')
box_1.append('card')

# Move the glasses and the mask and the tree from Box 3 to Box 4
box_3.remove('mask')
box_3.remove('glasses')
box_3.remove('tree')
box_4.extend(['mask', 'glasses', 'tree'])

# Move the grass from Box 5 to Box 1
box_5.remove('grass')
box_1.append('grass')

# Swap the tree in Box 4 with the doll in Box 6
box_4.remove('tree')
box_6.remove('doll')
box_4.append('doll')
box_6.append('tree')

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