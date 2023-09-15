box_0 = ['razor']
box_1 = ['pot', 'console', 'microscope', 'clock']
box_2 = ['fish', 'fridge', 'submarine']
box_3 = ['mask', 'shoe']
box_4 = ['pan', 'earring', 'pen', 'book']
box_5 = ['dice', 'violin', 'toothbrush', 'pants']
box_6 = ['thunder', 'chair', 'ring']
box_7 = []

# Remove the razor from Box 0
box_0.remove('razor')

# Move the pen from Box 4 to Box 6
item = box_4.pop(box_4.index('pen'))
box_6.append(item)

# Put the key and the drum into Box 4
box_4.extend(['key', 'drum'])

# Move the pan and the drum and the key from Box 4 to Box 6
items = [box_4.pop(box_4.index('pan')), box_4.pop(box_4.index('drum')), box_4.pop(box_4.index('key'))]
box_6.extend(items)

# Put the wire and the horn into Box 7
box_7.extend(['wire', 'horn'])

# Swap the toothbrush in Box 5 with the mask in Box 3
toothbrush = box_5.pop(box_5.index('toothbrush'))
mask = box_3.pop(box_3.index('mask'))
box_5.append(mask)
box_3.append(toothbrush)

# Remove the shoe from Box 3
box_3.remove('shoe')

# Put the keyboard and the leaf into Box 6
box_6.extend(['keyboard', 'leaf'])

# Remove the earring and the book from Box 4
box_4.remove('earring')
box_4.remove('book')

# Move the submarine and the fish from Box 2 to Box 3
items = [box_2.pop(box_2.index('submarine')), box_2.pop(box_2.index('fish'))]
box_3.extend(items)

# Replace the mask and the dice and the violin with the lock and the coral and the thunder in Box 5
items = [box_5.pop(box_5.index('mask')), box_5.pop(box_5.index('dice')), box_5.pop(box_5.index('violin'))]
box_5.extend(['lock', 'coral', 'thunder'])

# Swap the toothbrush in Box 3 with the leaf in Box 6
toothbrush = box_3.pop(box_3.index('toothbrush'))
leaf = box_6.pop(box_6.index('leaf'))
box_3.append(leaf)
box_6.append(toothbrush)

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)