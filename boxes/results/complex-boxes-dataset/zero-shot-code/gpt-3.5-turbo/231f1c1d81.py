box_0 = ['note', 'glasses', 'wallet', 'butterfly']
box_1 = ['bird', 'island', 'frame']
box_2 = ['helmet', 'jacket', 'necklace', 'pants', 'pen']
box_3 = ['sun', 'snow', 'pillow', 'zipper']
box_4 = ['shorts']
box_5 = ['jungle', 'star', 'hat', 'starfish']
box_6 = ['shark', 'lion', 'pot', 'magnet', 'bracelet']
box_7 = ['umbrella', 'lamp', 'sculpture']
box_8 = ['microscope', 'vase', 'puzzle']

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

# Move the jacket, pen, and necklace from Box 2 to Box 1
box_1.extend([box_2.pop(box_2.index('jacket'))])
box_1.extend([box_2.pop(box_2.index('pen'))])
box_1.extend([box_2.pop(box_2.index('necklace'))])

# Swap the note in Box 0 with the shorts in Box 4
box_0[box_0.index('note')], box_4[box_4.index('shorts')] = box_4[box_4.index('shorts')], box_0[box_0.index('note')]

# Remove the star, hat, and starfish from Box 5
box_5.remove('star')
box_5.remove('hat')
box_5.remove('starfish')

# Swap the sun in Box 3 with the wallet in Box 0
box_0[box_0.index('wallet')], box_3[box_3.index('sun')] = box_3[box_3.index('sun')], box_0[box_0.index('wallet')]

# Move the vase from Box 8 to Box 2
box_2.append(box_8.pop(box_8.index('vase')))

# Replace the microscope with the shoe in Box 8
box_8[box_8.index('microscope')] = 'shoe'

# Swap the snow in Box 3 with the jungle in Box 5
box_3[box_3.index('snow')], box_5[box_5.index('jungle')] = box_5[box_5.index('jungle')], box_3[box_3.index('snow')]

# Move the shorts, glasses, and sun from Box 0 to Box 6
box_6.extend([box_0.pop(box_0.index('shorts'))])
box_6.extend([box_0.pop(box_0.index('glasses'))])
box_6.extend([box_0.pop(box_0.index('sun'))])

# Move the puzzle and shoe from Box 8 to Box 7
box_7.extend([box_8.pop(box_8.index('puzzle'))])
box_7.extend([box_8.pop(box_8.index('shoe'))])

# Move the butterfly from Box 0 to Box 3
box_3.append(box_0.pop(box_0.index('butterfly')))

# Replace the shoe with the mirror in Box 7
box_7[box_7.index('shoe')] = 'mirror'

# Put the blender, key, and train into Box 3
box_3.extend(['blender', 'key', 'train'])

# Move the sun, shark, and lion from Box 6 to Box 8
box_8.extend([box_6.pop(box_6.index('sun'))])
box_8.extend([box_6.pop(box_6.index('shark'))])
box_8.extend([box_6.pop(box_6.index('lion'))])

# Replace the bracelet with the toy in Box 6
box_6[box_6.index('bracelet')] = 'toy'

# Print the final state of the boxes
print_boxes()