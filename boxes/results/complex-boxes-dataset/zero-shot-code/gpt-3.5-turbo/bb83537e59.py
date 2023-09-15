box_0 = ['hat', 'pants', 'earring', 'necklace']
box_1 = ['flower', 'grass', 'blanket']
box_2 = []
box_3 = ['vase', 'moon', 'bowl']
box_4 = ['ring']
box_5 = ['brush', 'tiger', 'cow']
box_6 = ['desert']
box_7 = ['dice', 'key', 'motorcycle', 'shampoo']
box_8 = ['storm']
box_9 = ['bracelet', 'train', 'lipstick', 'card']
box_10 = ['glove', 'lamp', 'piano', 'star', 'shorts']

# Put the flower and the river and the lock into Box 10
box_10.extend(['flower', 'river', 'lock'])

# Replace the card and the bracelet with the cup and the makeup in Box 9
box_9.remove('card')
box_9.remove('bracelet')
box_9.extend(['cup', 'makeup'])

# Remove the ring from Box 4
box_4.remove('ring')

# Put the glasses into Box 5
box_5.append('glasses')

# Replace the hat with the submarine in Box 0
box_0.remove('hat')
box_0.append('submarine')

# Move the storm from Box 8 to Box 1
box_1.append(box_8.pop())

# Swap the submarine in Box 0 with the cow in Box 5
box_0[0], box_5[2] = box_5[2], box_0[0]

# Remove the cow and the earring and the necklace from Box 0
box_0.remove('cow')
box_0.remove('earring')
box_0.remove('necklace')

# Remove the dice and the key and the motorcycle from Box 7
box_7.remove('dice')
box_7.remove('key')
box_7.remove('motorcycle')

# Put the piano into Box 3
box_3.append('piano')

# Swap the bowl in Box 3 with the brush in Box 5
box_3[2], box_5[0] = box_5[0], box_3[2]

# Remove the moon from Box 3
box_3.remove('moon')

# Move the shampoo from Box 7 to Box 10
box_10.append(box_7.pop())

# Replace the lock and the shampoo and the flower with the tree and the frame and the book in Box 10
box_10.remove('lock')
box_10.remove('shampoo')
box_10.remove('flower')
box_10.extend(['tree', 'frame', 'book'])

# Move the bowl and the tiger and the glasses from Box 5 to Box 1
box_1.extend([box_5.pop(0), box_5.pop(0), box_5.pop(0)])

# Put the elephant into Box 5
box_5.append('elephant')

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