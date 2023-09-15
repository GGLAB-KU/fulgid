box0 = ['jungle', 'frame', 'spoon']
box1 = ['comet']
box2 = ['watch', 'makeup', 'zipper', 'toothbrush']
box3 = ['pot', 'swimsuit', 'hat', 'bell']
box4 = ['shampoo', 'bear']

# Remove the comet from Box 1
box1.remove('comet')

# Move the bear and the shampoo from Box 4 to Box 3
box3.extend([box4.pop(box4.index('bear')), box4.pop(box4.index('shampoo'))])

# Put the keyboard and the submarine into Box 2
box2.extend(['keyboard', 'submarine'])

# Put the rain and the swimsuit and the cat into Box 2
box2.extend(['rain', 'swimsuit', 'cat'])

# Replace the spoon with the sun in Box 0
box0[box0.index('spoon')] = 'sun'

# Put the jungle into Box 4
box4.append('jungle')

# Put the bowl into Box 4
box4.append('bowl')

# Move the jungle and the bowl from Box 4 to Box 3
box3.extend([box4.pop(box4.index('jungle')), box4.pop(box4.index('bowl'))])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)