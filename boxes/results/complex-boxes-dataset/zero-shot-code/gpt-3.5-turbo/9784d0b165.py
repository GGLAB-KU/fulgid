box_0 = ['polish', 'key', 'game']
box_1 = ['gloves', 'mountain']
box_2 = ['starfish', 'piano', 'cat', 'horse']
box_3 = ['hat']
box_4 = ['toy']
box_5 = ['desert', 'leaf', 'apple']
box_6 = ['spoon', 'console', 'pen', 'lightning']

# Move the mountain from Box 1 to Box 6
box_6.append(box_1.pop(box_1.index('mountain')))

# Replace the toy with the tape in Box 4
box_4[0] = 'tape'

# Move the hat from Box 3 to Box 5
box_5.append(box_3.pop())

# Swap the gloves in Box 1 with the hat in Box 5
box_1[0], box_5[box_5.index('hat')] = box_5[box_5.index('hat')], box_1[0]

# Move the mountain from Box 6 to Box 0
box_0.append(box_6.pop(box_6.index('mountain')))

# Remove the mountain and the game from Box 0
box_0.remove('mountain')
box_0.remove('game')

# Put the cat and the console and the sun into Box 5
box_5.extend(['cat', 'console', 'sun'])

# Put the bell into Box 3
box_3.append('bell')

# Put the oven and the planet into Box 3
box_3.extend(['oven', 'planet'])

# Remove the hat from Box 1
box_1.remove('hat')

# Replace the starfish and the cat with the vase and the rocket in Box 2
box_2[box_2.index('starfish')] = 'vase'
box_2[box_2.index('cat')] = 'rocket'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)