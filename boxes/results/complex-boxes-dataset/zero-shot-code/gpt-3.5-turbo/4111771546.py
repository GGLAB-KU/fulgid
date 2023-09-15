box_0 = []
box_1 = []
box_2 = ['tape', 'frame']
box_3 = ['plate', 'toothpaste']
box_4 = ['river']
box_5 = ['pillow', 'laptop']

# Replace the wig with the car in Box 1
box_1.remove('wig')
box_1.append('car')

# Put the lion and the bus and the mountain into Box 1
box_1.extend(['lion', 'bus', 'mountain'])

# Put the headphone and the bowl and the boat into Box 0
box_0.extend(['headphone', 'bowl', 'boat'])

# Put the watch and the ring into Box 4
box_4.extend(['watch', 'ring'])

# Put the pen and the desert into Box 3
box_3.extend(['pen', 'desert'])

# Swap the car in Box 1 with the laptop in Box 5
box_1.remove('car')
box_5.remove('laptop')
box_1.append('laptop')
box_5.append('car')

# Remove the headphone from Box 0
box_0.remove('headphone')

# Move the lion and the bus from Box 1 to Box 3
box_1.remove('lion')
box_1.remove('bus')
box_3.extend(['lion', 'bus'])

# Move the lion from Box 3 to Box 4
box_3.remove('lion')
box_4.append('lion')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)