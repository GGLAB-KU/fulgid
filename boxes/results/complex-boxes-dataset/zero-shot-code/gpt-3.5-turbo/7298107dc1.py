box_0 = ['razor', 'flower']
box_1 = ['leaf', 'necklace', 'guitar']
box_2 = ['glove', 'rocket', 'dice', 'charger', 'seaweed']
box_3 = ['keyboard', 'brush']
box_4 = ['sandals', 'mask', 'mirror', 'storm']
box_5 = ['helmet', 'shoes', 'toothpaste']
box_6 = ['rock', 'wig']
box_7 = ['beach', 'whistle', 'freezer']
box_8 = ['spoon', 'comb', 'lock', 'pillow', 'octopus']
box_9 = ['grinder', 'bowl', 'boat', 'shorts']
box_10 = ['toothbrush', 'umbrella', 'towel', 'bus', 'pot']
box_11 = []

def print_boxes():
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

# Move the toothpaste and the helmet and the shoes from Box 5 to Box 4
box_4.extend([box_5.pop(box_5.index('toothpaste')), box_5.pop(box_5.index('helmet')), box_5.pop(box_5.index('shoes'))])

# Put the plate and the pot into Box 3
box_3.extend([box_10.pop(box_10.index('plate')), box_10.pop(box_10.index('pot'))])

# Move the rock and the wig from Box 6 to Box 10
box_10.extend([box_6.pop(box_6.index('rock')), box_6.pop(box_6.index('wig'))])

# Move the razor from Box 0 to Box 8
box_8.append(box_0.pop(box_0.index('razor')))

# Replace the toothpaste with the puzzle in Box 4
box_4[box_4.index('toothpaste')] = 'puzzle'

# Move the flower from Box 0 to Box 11
box_11.append(box_0.pop(box_0.index('flower')))

# Move the beach and the whistle from Box 7 to Box 8
box_8.extend([box_7.pop(box_7.index('beach')), box_7.pop(box_7.index('whistle'))])

# Empty Box 7
box_7 = []

# Remove the flower from Box 11
box_11.remove('flower')

# Replace the leaf with the toaster in Box 1
box_1[box_1.index('leaf')] = 'toaster'

# Swap the rock in Box 10 with the lock in Box 8
box_10[box_10.index('rock')], box_8[box_8.index('lock')] = box_8[box_8.index('lock')], box_10[box_10.index('rock')]

# Move the boat from Box 9 to Box 3
box_3.append(box_9.pop(box_9.index('boat')))

# Swap the sandals in Box 4 with the plate in Box 3
box_4[box_4.index('sandals')], box_3[box_3.index('plate')] = box_3[box_3.index('plate')], box_4[box_4.index('sandals')]

# Replace the bowl and the grinder with the drum and the glasses in Box 9
box_9[box_9.index('bowl')] = 'drum'
box_9[box_9.index('grinder')] = 'glasses'

# Swap the necklace in Box 1 with the shoes in Box 4
box_1[box_1.index('necklace')], box_4[box_4.index('shoes')] = box_4[box_4.index('shoes')], box_1[box_1.index('necklace')]

# Move the octopus and the beach and the razor from Box 8 to Box 4
box_4.extend([box_8.pop(box_8.index('octopus')), box_8.pop(box_8.index('beach')), box_8.pop(box_8.index('razor'))])

# Remove the pot from Box 10
box_10.remove('pot')

# Move the octopus from Box 4 to Box 11
box_11.append(box_4.pop(box_4.index('octopus')))

# Print the final state of the boxes
print_boxes()