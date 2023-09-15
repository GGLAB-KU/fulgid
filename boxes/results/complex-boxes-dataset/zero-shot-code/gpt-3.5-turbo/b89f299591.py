box_0 = ['bus', 'key']
box_1 = ['elephant', 'button']
box_2 = ['pen', 'laptop', 'shark', 'bag']
box_3 = ['shampoo', 'telescope']
box_4 = ['lion', 'doll', 'card', 'dog', 'toothbrush']
box_5 = ['zipper', 'toy', 'razor']
box_6 = ['game', 'beach', 'table']
box_7 = []
box_8 = ['clock', 'comet']
box_9 = []

# Move the razor from Box 5 to Box 4
box_4.append(box_5.pop(2))

# Remove the laptop and the shark from Box 2
box_2.remove('laptop')
box_2.remove('shark')

# Swap the telescope in Box 3 with the bus in Box 0
box_0[0], box_3[1] = box_3[1], box_0[0]

# Remove the comet from Box 8
box_8.remove('comet')

# Replace the zipper and the toy with the coat and the hat in Box 5
box_5.remove('zipper')
box_5.remove('toy')
box_5.extend(['coat', 'hat'])

# Swap the hat in Box 5 with the elephant in Box 1
box_1[0], box_5[1] = box_5[1], box_1[0]

# Swap the button in Box 1 with the pen in Box 2
box_1[1], box_2[0] = box_2[0], box_1[1]

# Put the shoe and the headphone into Box 8
box_8.extend(['shoe', 'headphone'])

# Remove the key and the telescope from Box 0
box_0.remove('key')
box_0.remove('telescope')

# Empty Box 8
box_8.clear()

# Remove the game from Box 6
box_6.remove('game')

# Put the horn into Box 5
box_5.append('horn')

# Replace the button and the bag with the dice and the phone in Box 2
box_2.remove('button')
box_2.remove('bag')
box_2.extend(['dice', 'phone'])

# Put the tree into Box 6
box_6.append('tree')

# Remove the shampoo from Box 3
box_3.remove('shampoo')

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