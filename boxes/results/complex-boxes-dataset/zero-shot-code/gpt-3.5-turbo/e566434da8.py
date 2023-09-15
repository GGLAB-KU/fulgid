box_0 = ['flower']
box_1 = ['crown', 'charger', 'cloud', 'table', 'plate']
box_2 = ['car', 'button']
box_3 = ['watch', 'sandals']
box_4 = []
box_5 = ['blender', 'comet', 'tree']
box_6 = ['dolphin']
box_7 = ['boot', 'perfume', 'bell', 'mirror', 'moon']
box_8 = ['zipper', 'pants', 'dress', 'battery']
box_9 = ['grass', 'swimsuit']

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

# Move the charger and the cloud from Box 1 to Box 5
box_5.extend([box_1.pop(box_1.index('charger')), box_1.pop(box_1.index('cloud'))])

# Swap the dolphin in Box 6 with the bell in Box 7
box_6[0], box_7[box_7.index('bell')] = box_7[box_7.index('bell')], box_6[0]

# Put the charger into Box 5
box_5.append('charger')

# Replace the flower with the cloud in Box 0
box_0[0] = 'cloud'

# Move the crown and the plate and the table from Box 1 to Box 5
box_5.extend([box_1.pop(box_1.index('crown')), box_1.pop(box_1.index('plate')), box_1.pop(box_1.index('table'))])

# Move the dolphin and the perfume and the moon from Box 7 to Box 4
box_4.extend([box_7.pop(box_7.index('dolphin')), box_7.pop(box_7.index('perfume')), box_7.pop(box_7.index('moon'))])

# Put the earring into Box 8
box_8.append('earring')

# Empty Box 5
box_5.clear()

# Put the dress and the watch and the game into Box 0
box_0.extend([box_8.pop(box_8.index('dress')), box_3.pop(box_3.index('watch')), 'game'])

# Move the boot and the mirror from Box 7 to Box 4
box_4.extend([box_7.pop(box_7.index('boot')), box_7.pop(box_7.index('mirror'))])

# Move the grass from Box 9 to Box 2
box_2.append(box_9.pop(box_9.index('grass')))

# Swap the watch in Box 3 with the boot in Box 4
box_3[0], box_4[box_4.index('boot')] = box_4[box_4.index('boot')], box_3[0]

# Move the bell from Box 6 to Box 7
box_7.append(box_6.pop())

# Swap the mirror in Box 4 with the earring in Box 8
box_4[box_4.index('mirror')], box_8[box_8.index('earring')] = box_8[box_8.index('earring')], box_4[box_4.index('mirror')]

# Move the sandals and the boot from Box 3 to Box 5
box_5.extend([box_3.pop(box_3.index('sandals')), box_3.pop(box_3.index('boot'))])

# Print the final state of the boxes
print_boxes()