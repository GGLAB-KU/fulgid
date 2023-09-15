box_0 = ['table', 'earring', 'chair', 'lock', 'shirt']
box_1 = ['comb', 'magnet', 'bag', 'river']
box_2 = ['pot', 'coral', 'tie', 'forest', 'controller']
box_3 = ['shoe']
box_4 = ['basket', 'toaster', 'star', 'toothpaste']
box_5 = ['bear', 'candle', 'whistle', 'polish', 'elephant']
box_6 = ['blanket', 'speaker']
box_7 = ['grass', 'razor', 'wig', 'ring', 'laptop']
box_8 = ['necklace', 'brush', 'octopus', 'keyboard', 'makeup']

# Move the wig from Box 7 to Box 0
box_0.append(box_7.pop(box_7.index('wig')))

# Swap the magnet in Box 1 with the blanket in Box 6
box_1[box_1.index('magnet')], box_6[box_6.index('blanket')] = box_6[box_6.index('blanket')], box_1[box_1.index('magnet')]

# Put the toothpaste and the elephant into Box 4
box_4.extend(['toothpaste', 'elephant'])

# Put the chair and the rain into Box 0
box_0.extend(['chair', 'rain'])

# Remove the elephant and the swimsuit from Box 4
box_4.remove('elephant')

# Put the shampoo and the coral and the dice into Box 8
box_8.extend(['shampoo', 'coral', 'dice'])

# Swap the laptop in Box 7 with the brush in Box 8
box_7[box_7.index('laptop')], box_8[box_8.index('brush')] = box_8[box_8.index('brush')], box_7[box_7.index('laptop')]

# Put the piano and the swimsuit and the lion into Box 5
box_5.extend(['piano', 'swimsuit', 'lion'])

# Remove the blanket and the river and the bag from Box 1
box_1.remove('blanket')
box_1.remove('river')
box_1.remove('bag')

# Replace the swimsuit with the shark in Box 5
box_5[box_5.index('swimsuit')] = 'shark'

# Move the basket from Box 4 to Box 1
box_1.append(box_4.pop(box_4.index('basket')))

# Swap the lock in Box 0 with the grass in Box 7
box_0[box_0.index('lock')], box_7[box_7.index('grass')] = box_7[box_7.index('grass')], box_0[box_0.index('lock')]

# Move the controller and the pot and the tie from Box 2 to Box 3
box_3.extend([box_2.pop(box_2.index('controller')), box_2.pop(box_2.index('pot')), box_2.pop(box_2.index('tie'))])

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