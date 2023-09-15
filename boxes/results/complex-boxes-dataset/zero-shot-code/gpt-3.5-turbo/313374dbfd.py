box_0 = ['helmet', 'controller', 'jacket', 'coral', 'thunder']
box_1 = ['forest', 'cloud', 'lion', 'scissors']
box_2 = ['blanket', 'doll', 'mask', 'bicycle', 'lipstick']
box_3 = ['horn', 'bear', 'desert']
box_4 = ['car', 'candle']
box_5 = ['thread', 'toy', 'bird', 'pen']
box_6 = ['microscope']
box_7 = ['shorts']
box_8 = ['freezer']
box_9 = ['whistle', 'bus', 'jungle', 'sock']
box_10 = ['skirt', 'dress', 'shampoo', 'glasses', 'brush']
box_11 = ['keyboard', 'submarine', 'charger', 'puzzle', 'hat']
box_12 = ['note']

# Put the leaf and the ocean into Box 2
box_2.extend(['leaf', 'ocean'])

# Move the bus and the whistle and the jungle from Box 9 to Box 1
box_1.extend(box_9[1:4])
box_9 = box_9[:1] + box_9[4:]

# Swap the car in Box 4 with the desert in Box 3
box_4[0], box_3[2] = box_3[2], box_4[0]

# Put the truck and the storm into Box 12
box_12.extend(['truck', 'storm'])

# Move the scissors and the cloud and the jungle from Box 1 to Box 8
box_8.extend(box_1[2:5])
box_1 = box_1[:2]

# Replace the thread and the toy with the paint and the charger in Box 5
box_5 = ['paint', 'charger', 'bird', 'pen']

# Put the phone into Box 12
box_12.append('phone')

# Replace the pen and the paint and the charger with the speaker and the tree and the coin in Box 5
box_5 = ['speaker', 'tree', 'coin']

# Swap the keyboard in Box 11 with the storm in Box 12
box_11[0], box_12[1] = box_12[1], box_11[0]

# Move the phone and the keyboard and the truck from Box 12 to Box 1
box_1.extend(box_12[0:3])
box_12 = []

# Put the chair and the piano and the apple into Box 8
box_8.extend(['chair', 'piano', 'apple'])

# Swap the keyboard in Box 1 with the car in Box 3
box_1[0], box_3[0] = box_3[0], box_1[0]

# Replace the lion with the umbrella in Box 1
box_1[2] = 'umbrella'

# Move the keyboard from Box 3 to Box 1
box_1.append(box_3[0])
box_3 = box_3[1:]

# Swap the leaf in Box 2 with the bus in Box 1
box_2[4], box_1[1] = box_1[1], box_2[4]

# Replace the whistle and the forest and the keyboard with the phone and the plane and the sandals in Box 1
box_1 = ['phone', 'plane', 'sandals']

# Put the piano into Box 2
box_2.append('piano')

# Remove the helmet from Box 0
box_0.remove('helmet')

# Remove the shorts from Box 7
box_7 = []

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