box_0 = ['basket', 'sculpture']
box_1 = ['laptop']
box_2 = ['button', 'piano', 'jungle', 'shoe', 'butterfly']
box_3 = ['shark', 'motorcycle']
box_4 = ['apple', 'sun']
box_5 = ['lamp', 'mixer', 'ship', 'speaker', 'bird']
box_6 = []
box_7 = ['lion', 'flute']

# Swap the shoe in Box 2 with the lion in Box 7
box_2[3], box_7[0] = box_7[0], box_2[3]

# Remove the sun from Box 4
box_4.remove('sun')

# Swap the shark in Box 3 with the shoe in Box 7
box_3[0], box_7[0] = box_7[0], box_3[0]

# Replace the butterfly and the lion with the keyboard and the plane in Box 2
box_2[4] = 'keyboard'
box_2.append('plane')

# Put the violin and the sculpture into Box 4
box_4.extend(['violin', 'sculpture'])

# Move the plane and the piano and the jungle from Box 2 to Box 6
box_6.extend([box_2.pop(4), box_2.pop(2), box_2.pop(2)])

# Remove the apple from Box 4
box_4.remove('apple')

# Remove the sculpture and the violin from Box 4
box_4.remove('sculpture')
box_4.remove('violin')

# Remove the basket and the sculpture from Box 0
box_0.remove('basket')
box_0.remove('sculpture')

# Move the shoe and the motorcycle from Box 3 to Box 4
box_4.extend([box_3.pop(1), box_3.pop(0)])

# Remove the keyboard and the button from Box 2
box_2.remove('keyboard')
box_2.remove('button')

# Remove the laptop from Box 1
box_1.remove('laptop')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)