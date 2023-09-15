box_0 = ['console', 'belt']
box_1 = ['sandals', 'comb']
box_2 = []
box_3 = ['tree']
box_4 = ['mask', 'desert', 'tie', 'oven']
box_5 = ['skirt']
box_6 = ['lamp', 'speaker']
box_7 = ['magnet', 'note', 'forest', 'lion']
box_8 = ['doll', 'key', 'gloves', 'swimsuit']
box_9 = ['microscope', 'branch', 'mixer', 'flower', 'truck']
box_10 = ['soap', 'rocket']

# Move the lamp from Box 6 to Box 10
box_10.append(box_6.pop(box_6.index('lamp')))

# Swap the lamp in Box 10 with the desert in Box 4
box_10.append(box_4.pop(box_4.index('desert')))
box_4.append(box_10.pop(box_10.index('lamp')))

# Swap the lion in Box 7 with the truck in Box 9
box_7.append(box_9.pop(box_9.index('lion')))
box_9.append(box_7.pop(box_7.index('truck')))

# Move the skirt from Box 5 to Box 3
box_3.append(box_5.pop(box_5.index('skirt')))

# Swap the lamp in Box 4 with the doll in Box 8
box_4.append(box_8.pop(box_8.index('doll')))
box_8.append(box_4.pop(box_4.index('lamp')))

# Put the island and the wallet and the snow into Box 9
box_9.extend(['island', 'wallet', 'snow'])

# Swap the mixer in Box 9 with the doll in Box 4
box_9.append(box_4.pop(box_4.index('mixer')))
box_4.append(box_9.pop(box_9.index('doll')))

# Remove the tie and the oven from Box 4
box_4.remove('tie')
box_4.remove('oven')

# Put the pillow and the bear into Box 0
box_0.extend(['pillow', 'bear'])

# Replace the branch with the thunder in Box 9
box_9.append('thunder')
box_9.remove('branch')

# Replace the mask and the mixer with the makeup and the boat in Box 4
box_4.append('makeup')
box_4.append('boat')
box_4.remove('mask')
box_4.remove('mixer')

# Swap the comb in Box 1 with the gloves in Box 8
box_1.append(box_8.pop(box_8.index('gloves')))
box_8.append(box_1.pop(box_1.index('comb')))

# Swap the soap in Box 10 with the lion in Box 9
box_10.append(box_9.pop(box_9.index('lion')))
box_9.append(box_10.pop(box_10.index('soap')))

# Remove the lion and the desert from Box 10
box_10.remove('lion')
box_10.remove('desert')

# Move the tree and the skirt from Box 3 to Box 2
box_2.append(box_3.pop(box_3.index('tree')))
box_2.append(box_3.pop(box_3.index('skirt')))

# Swap the lamp in Box 8 with the gloves in Box 1
box_8.append(box_1.pop(box_1.index('gloves')))
box_1.append(box_8.pop(box_8.index('lamp')))

# Remove the rocket from Box 10
box_10.remove('rocket')

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
print("Box 9:", box_9)
print("Box 10:", box_10)