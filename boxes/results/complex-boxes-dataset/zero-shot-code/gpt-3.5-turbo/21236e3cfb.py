box_0 = ['camera', 'dress', 'plane']
box_1 = ['zipper', 'perfume', 'lightning', 'dice']
box_2 = ['chair', 'makeup', 'button']
box_3 = ['earring']
box_4 = ['fork', 'puzzle']
box_5 = []
box_6 = []
box_7 = []
box_8 = ['controller', 'planet', 'shirt']
box_9 = ['candle']
box_10 = ['starfish', 'toy', 'horse', 'bird']
box_11 = ['bell', 'meteor']

# Move the meteor from Box 11 to Box 0
box_0.append(box_11.pop(box_11.index('meteor')))

# Replace the controller with the mountain in Box 8
box_8[box_8.index('controller')] = 'mountain'

# Replace the button and the chair with the violin and the mixer in Box 2
box_2.remove('button')
box_2.remove('chair')
box_2.extend(['violin', 'mixer'])

# Replace the bell with the branch in Box 11
box_11[box_11.index('bell')] = 'branch'

# Remove the mixer and the violin and the makeup from Box 2
box_2.remove('mixer')
box_2.remove('violin')
box_2.remove('makeup')

# Replace the earring with the shark in Box 3
box_3[box_3.index('earring')] = 'shark'

# Swap the plane in Box 0 with the dice in Box 1
box_0.append(box_1.pop(box_1.index('plane')))
box_1.append(box_0.pop(box_0.index('dice')))

# Remove the candle from Box 9
box_9.remove('candle')

# Swap the branch in Box 11 with the dress in Box 0
box_0.append(box_11.pop(box_11.index('dress')))
box_11.append(box_0.pop(box_0.index('branch')))

# Move the zipper and the perfume and the lightning from Box 1 to Box 3
box_3.extend([box_1.pop(box_1.index('zipper')), box_1.pop(box_1.index('perfume')), box_1.pop(box_1.index('lightning'))])

# Move the plane from Box 1 to Box 7
box_7.append(box_1.pop(box_1.index('plane')))

# Put the belt and the horn into Box 5
box_5.extend(['belt', 'horn'])

# Put the battery into Box 2
box_2.append('battery')

# Put the drum into Box 10
box_10.append('drum')

# Put the bus into Box 4
box_4.append('bus')

# Remove the plane from Box 7
box_7.remove('plane')

# Empty Box 2
box_2.clear()

# Put the toothpaste and the forest into Box 0
box_0.extend(['toothpaste', 'forest'])

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
print("Box 11:", box_11)