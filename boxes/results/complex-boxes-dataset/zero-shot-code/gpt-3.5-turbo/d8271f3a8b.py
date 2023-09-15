box_0 = ['cup', 'train']
box_1 = ['comb', 'toothpaste', 'pen']
box_2 = ['wig', 'necklace']
box_3 = ['fridge']
box_4 = ['puzzle', 'lock', 'sock', 'paint', 'ring']
box_5 = ['needle', 'crown', 'cat']
box_6 = ['elephant', 'camera', 'lamp', 'clock']
box_7 = ['scissors', 'skirt']
box_8 = ['blender', 'tiger', 'boat', 'helmet']
box_9 = ['brush', 'headphone']

# Move the cat from Box 5 to Box 4
box_4.append(box_5.pop(box_5.index('cat')))

# Move the comb and the toothpaste and the pen from Box 1 to Box 5
box_5.extend([box_1.pop(box_1.index('comb')), box_1.pop(box_1.index('toothpaste')), box_1.pop(box_1.index('pen'))])

# Swap the crown in Box 5 with the tiger in Box 8
box_5[box_5.index('crown')], box_8[box_8.index('tiger')] = box_8[box_8.index('tiger')], box_5[box_5.index('crown')]

# Move the elephant and the camera and the clock from Box 6 to Box 7
box_7.extend([box_6.pop(box_6.index('elephant')), box_6.pop(box_6.index('camera')), box_6.pop(box_6.index('clock'))])

# Remove the cat and the lock and the paint from Box 4
box_4.remove('cat')
box_4.remove('lock')
box_4.remove('paint')

# Move the scissors and the clock and the skirt from Box 7 to Box 6
box_6.extend([box_7.pop(box_7.index('scissors')), box_7.pop(box_7.index('clock')), box_7.pop(box_7.index('skirt'))])

# Put the jungle and the comet into Box 5
box_5.extend(['jungle', 'comet'])

# Swap the fridge in Box 3 with the boat in Box 8
box_3, box_8 = box_8, box_3

# Remove the headphone and the brush from Box 9
box_9.remove('headphone')
box_9.remove('brush')

# Swap the skirt in Box 6 with the wig in Box 2
box_6[box_6.index('skirt')], box_2[box_2.index('wig')] = box_2[box_2.index('wig')], box_6[box_6.index('skirt')]

# Move the boat from Box 3 to Box 4
box_4.append(box_3.pop())

# Remove the helmet and the fridge and the blender from Box 8
box_8.remove('helmet')
box_8.remove('fridge')
box_8.remove('blender')

# Replace the camera and the elephant with the island and the telescope in Box 7
box_7[box_7.index('camera')] = 'island'
box_7[box_7.index('elephant')] = 'telescope'

# Swap the toothpaste in Box 5 with the telescope in Box 7
box_5[box_5.index('toothpaste')], box_7[box_7.index('telescope')] = box_7[box_7.index('telescope')], box_5[box_5.index('toothpaste')]

# Empty Box 0
box_0 = []

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