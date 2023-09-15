box_0 = ['jacket', 'lamp']
box_1 = ['scissors', 'magnet', 'forest', 'microscope']
box_2 = ['telescope', 'thunder', 'lipstick']
box_3 = []
box_4 = ['island', 'sandals', 'table', 'bowl', 'beach']
box_5 = ['truck', 'boat']
box_6 = ['bird', 'rain', 'pot']
box_7 = ['pen', 'toaster', 'glove', 'ring', 'guitar']
box_8 = ['flower', 'comb', 'dice', 'grinder', 'towel']

# Remove the island and the table from Box 4
box_4.remove('island')
box_4.remove('table')

# Put the whistle into Box 5
box_5.append('whistle')

# Replace the truck with the flower in Box 5
box_5.remove('truck')
box_5.append('flower')

# Swap the glove in Box 7 with the flower in Box 5
box_7.remove('glove')
box_7.append('flower')

# Remove the toaster from Box 7
box_7.remove('toaster')

# Swap the dice in Box 8 with the whistle in Box 5
box_8.remove('dice')
box_8.append('whistle')

# Put the book into Box 3
box_3.append('book')

# Move the guitar from Box 7 to Box 0
box_0.append('guitar')
box_7.remove('guitar')

# Remove the whistle from Box 8
box_8.remove('whistle')

# Move the beach and the bowl from Box 4 to Box 1
box_1.append('beach')
box_1.append('bowl')
box_4.remove('beach')
box_4.remove('bowl')

# Swap the flower in Box 8 with the thunder in Box 2
box_8.remove('flower')
box_8.append('thunder')
box_2.remove('thunder')
box_2.append('flower')

# Put the book and the razor into Box 2
box_2.append('book')
box_2.append('razor')

# Replace the lipstick with the bear in Box 2
box_2.remove('lipstick')
box_2.append('bear')

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