box_0 = ['coat', 'candle']
box_1 = ['oven']
box_2 = []
box_3 = ['meteor', 'jungle']
box_4 = ['lion', 'necklace']

# Swap the candle in Box 0 with the meteor in Box 3
box_0[1], box_3[0] = box_3[0], box_0[1]

# Remove the meteor from Box 0
box_0.remove('meteor')

# Replace the candle with the note in Box 3
box_3[1] = 'note'

# Put the apple and the mirror into Box 3
box_3.extend(['apple', 'mirror'])

# Put the sculpture into Box 1
box_1.append('sculpture')

# Move the oven from Box 1 to Box 2
box_2.append(box_1.pop(0))

# Move the jungle and the apple from Box 3 to Box 4
box_4.extend([box_3.pop(1), box_3.pop(1)])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)