box_0 = ['polish', 'bracelet', 'dress']
box_1 = ['candle', 'bag', 'shampoo', 'table']
box_2 = ['lock', 'freezer', 'helmet', 'shoe']
box_3 = ['mixer', 'paint', 'charger', 'scarf', 'umbrella']
box_4 = ['zipper', 'glasses']
box_5 = ['octopus', 'island', 'clock', 'comet']
box_6 = ['cloud']
box_7 = ['boat', 'fridge']
box_8 = ['camera', 'bird', 'car', 'razor', 'note']

# Move polish, bracelet, and dress from Box 0 to Box 5
box_5.extend(box_0)
box_0.clear()

# Put the drum into Box 0
box_0.append('drum')

# Swap the scarf in Box 3 with the fridge in Box 7
box_3[box_3.index('scarf')], box_7[box_7.index('fridge')] = box_7[box_7.index('fridge')], box_3[box_3.index('scarf')]

# Move the drum from Box 0 to Box 3
box_3.append(box_0.pop())

# Remove the fridge, paint, and umbrella from Box 3
box_3.remove('fridge')
box_3.remove('paint')
box_3.remove('umbrella')

# Replace the helmet, freezer, and lock with the dice, puzzle, and truck in Box 2
box_2 = ['dice', 'puzzle', 'truck']

# Remove the cloud from Box 6
box_6.clear()

# Remove the shampoo from Box 1
box_1.remove('shampoo')

# Move the dice, puzzle, and shoe from Box 2 to Box 6
box_6.extend(box_2)
box_2.clear()

# Swap the dice in Box 6 with the scarf in Box 7
box_6[box_6.index('dice')], box_7[box_7.index('scarf')] = box_7[box_7.index('scarf')], box_6[box_6.index('dice')]

# Empty Box 2
box_2.clear()

# Empty Box 8
box_8.clear()

# Remove the puzzle and shoe from Box 6
box_6.remove('puzzle')
box_6.remove('shoe')

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