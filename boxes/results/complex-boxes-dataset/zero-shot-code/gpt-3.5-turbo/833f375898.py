box_0 = ['scarf', 'clock']
box_1 = ['bus', 'rain', 'sculpture', 'fish']
box_2 = ['mask', 'piano', 'bicycle', 'shampoo', 'star']
box_3 = ['gloves', 'flute', 'umbrella', 'submarine']
box_4 = ['helmet', 'comb', 'speaker', 'sandals', 'telescope']
box_5 = ['laptop', 'watch', 'lipstick']
box_6 = []
box_7 = ['pot', 'fork', 'table', 'polish', 'blanket']
box_8 = ['toy', 'wig', 'starfish', 'truck']

# Remove the clock from Box 0
box_0.remove('clock')

# Put the rocket and the beach and the ship into Box 4
box_4.extend(['rocket', 'beach', 'ship'])

# Swap the watch in Box 5 with the scarf in Box 0
box_0[0], box_5[1] = box_5[1], box_0[0]

# Remove the wig and the truck from Box 8
box_8.remove('wig')
box_8.remove('truck')

# Replace the submarine and the gloves and the umbrella with the glasses and the camera and the charger in Box 3
box_3.remove('submarine')
box_3.remove('gloves')
box_3.remove('umbrella')
box_3.extend(['glasses', 'camera', 'charger'])

# Swap the lipstick in Box 5 with the bus in Box 1
box_1[0], box_5[2] = box_5[2], box_1[0]

# Swap the sandals in Box 4 with the bus in Box 5
box_4[3], box_5[0] = box_5[0], box_4[3]

# Move the fish and the sculpture from Box 1 to Box 7
box_7.extend([box_1.pop(3), box_1.pop(2)])

# Move the comb and the telescope from Box 4 to Box 8
box_8.extend([box_4.pop(1), box_4.pop(3)])

# Remove the scarf and the sandals from Box 5
box_5.remove('scarf')
box_5.remove('sandals')

# Swap the piano in Box 2 with the blanket in Box 7
box_2[1], box_7[3] = box_7[3], box_2[1]

# Move the fish and the table and the fork from Box 7 to Box 8
box_8.extend([box_7.pop(2), box_7.pop(2), box_7.pop(2)])

# Move the watch from Box 0 to Box 4
box_4.append(box_0.pop(0))

# Replace the camera and the flute with the fork and the table in Box 3
box_3.remove('camera')
box_3.remove('flute')
box_3.extend(['fork', 'table'])

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