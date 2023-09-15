box_0 = ['bell']
box_1 = ['tape', 'sandals', 'branch', 'pan', 'puzzle']
box_2 = ['watch', 'snow', 'lipstick', 'shark']
box_3 = ['coat', 'hat', 'whistle', 'horse']
box_4 = ['perfume', 'table', 'submarine', 'dolphin']
box_5 = ['shoes', 'blender', 'meteor', 'fish', 'grass']
box_6 = ['lamp', 'seaweed', 'glasses', 'console']
box_7 = ['rocket', 'rain']
box_8 = ['skirt', 'moon', 'dog']
box_9 = ['crown']
box_10 = []
box_11 = ['coin', 'magnet', 'game', 'dress', 'shirt']
box_12 = ['swimsuit', 'tiger']
box_13 = ['spoon', 'violin', 'scissors', 'horn']

# Move the moon and the dog from Box 8 to Box 6
box_6.extend(box_8)
box_8.clear()

# Move the swimsuit and the tiger from Box 12 to Box 9
box_9.extend(box_12)
box_12.clear()

# Swap the skirt in Box 8 with the shark in Box 2
box_8[0], box_2[1] = box_2[1], box_8[0]

# Remove the rocket from Box 7
box_7.remove('rocket')

# Move the tiger and the crown from Box 9 to Box 4
box_4.extend(box_9)
box_9.clear()

# Swap the rain in Box 7 with the bell in Box 0
box_0[0], box_7[0] = box_7[0], box_0[0]

# Move the rain from Box 0 to Box 8
box_8.append(box_0.pop())

# Replace the dolphin and the table and the perfume with the thunder and the sun and the jacket in Box 4
box_4 = ['thunder', 'sun', 'jacket']

# Swap the sandals in Box 1 with the hat in Box 3
box_1[1], box_3[1] = box_3[1], box_1[1]

# Remove the spoon and the scissors and the violin from Box 13
box_13.clear()

# Move the fish and the blender and the shoes from Box 5 to Box 12
box_12.extend(box_5[3:])
box_5 = box_5[:3]

# Put the skirt and the fish into Box 4
box_4.extend(['skirt', 'fish'])

# Replace the grass with the branch in Box 5
box_5 = ['branch']

# Remove the dog from Box 6
box_6.remove('dog')

# Replace the horn with the storm in Box 13
box_13 = ['storm']

# Put the hat and the toothpaste into Box 10
box_10.extend(['hat', 'toothpaste'])

# Put the leaf and the game into Box 6
box_6.extend(['leaf', 'game'])

# Empty Box 6
box_6.clear()

# Remove the fish and the crown from Box 4
box_4.remove('fish')
box_4.remove('crown')

# Replace the whistle and the coat with the watch and the sun in Box 3
box_3 = ['watch', 'sun']

# Put the doll and the book into Box 4
box_4.extend(['doll', 'book'])

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
print("Box 12:", box_12)
print("Box 13:", box_13)