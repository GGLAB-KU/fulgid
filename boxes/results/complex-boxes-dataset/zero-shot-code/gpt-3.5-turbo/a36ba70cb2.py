box_0 = []
box_1 = ['console', 'dice', 'perfume', 'note']
box_2 = ['lightning', 'thunder', 'towel']
box_3 = []
box_4 = ['magnet', 'zipper', 'card', 'controller']
box_5 = ['polish', 'gloves']
box_6 = []
box_7 = []
box_8 = []
box_9 = []

# Put the camera and the meteor into Box 6
box_6.extend(['camera', 'meteor'])

# Swap the comet in Box 2 with the note in Box 1
box_1[box_1.index('note')], box_2[box_2.index('comet')] = box_2[box_2.index('comet')], box_1[box_1.index('note')]

# Remove the camera and the horse from Box 6
box_6.remove('camera')
box_6.remove('horse')

# Replace the snow and the scarf with the bear and the bicycle in Box 6
box_6 = ['bear', 'bicycle']

# Swap the bear in Box 4 with the oven in Box 1
box_1[box_1.index('oven')], box_4[box_4.index('bear')] = box_4[box_4.index('bear')], box_1[box_1.index('oven')]

# Put the fridge into Box 0
box_0.append('fridge')

# Swap the controller in Box 4 with the fridge in Box 0
box_0[0], box_4[box_4.index('controller')] = box_4[box_4.index('controller')], box_0[0]

# Put the toothpaste and the tie and the pot into Box 5
box_5.extend(['toothpaste', 'tie', 'pot'])

# Move the towel and the note and the lightning from Box 2 to Box 9
box_9.extend([box_2.pop(box_2.index('towel')), box_1.pop(box_1.index('note')), box_2.pop(box_2.index('lightning'))])

# Remove the toothpaste and the pot from Box 5
box_5.remove('toothpaste')
box_5.remove('pot')

# Move the note and the lightning from Box 9 to Box 8
box_8.extend([box_9.pop(box_9.index('note')), box_9.pop(box_9.index('lightning'))])

# Swap the gloves in Box 5 with the oven in Box 4
box_5[box_5.index('gloves')], box_4[box_4.index('oven')] = box_4[box_4.index('oven')], box_5[box_5.index('gloves')]

# Put the flower into Box 2
box_2.append('flower')

# Replace the bear with the horse in Box 1
box_1[box_1.index('bear')] = 'horse'

# Replace the comet and the horse and the perfume with the helmet and the spoon and the flute in Box 1
box_1 = ['console', 'dice', 'perfume', 'helmet', 'spoon', 'flute']

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