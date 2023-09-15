box_0 = ['magnet', 'tiger', 'basket']
box_1 = ['table']
box_2 = ['thunder']
box_3 = []
box_4 = []
box_5 = ['shoes', 'shelf', 'cat']

# Remove the basket from Box 0
box_0.remove('basket')

# Replace the tiger and the magnet with the snow and the motorcycle in Box 0
box_0.remove('magnet')
box_0.remove('tiger')
box_0.append('snow')
box_0.append('motorcycle')

# Swap the table in Box 1 with the shelf in Box 5
box_1.remove('table')
box_5.remove('shelf')
box_1.append('shelf')
box_5.append('table')

# Move the snow and the motorcycle from Box 0 to Box 2
box_0.remove('snow')
box_0.remove('motorcycle')
box_2.append('snow')
box_2.append('motorcycle')

# Replace the shoes and the table and the cat with the note and the necklace and the grass in Box 5
box_5.remove('shoes')
box_5.remove('table')
box_5.remove('cat')
box_5.append('note')
box_5.append('necklace')
box_5.append('grass')

# Remove the thunder and the snow and the motorcycle from Box 2
box_2.remove('thunder')
box_2.remove('snow')
box_2.remove('motorcycle')

# Replace the shelf with the makeup in Box 1
box_1.remove('shelf')
box_1.append('makeup')

# Replace the makeup with the elephant in Box 1
box_1.remove('makeup')
box_1.append('elephant')

# Replace the note and the necklace with the shampoo and the ring in Box 5
box_5.remove('note')
box_5.remove('necklace')
box_5.append('shampoo')
box_5.append('ring')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)