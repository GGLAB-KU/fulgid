box_0 = ['fish', 'wire', 'jungle', 'scarf']
box_1 = ['table', 'needle', 'boot', 'tie']
box_2 = ['sandals', 'pen', 'magnet', 'spoon']
box_3 = ['freezer', 'motorcycle', 'submarine', 'perfume', 'bracelet']
box_4 = ['pan', 'coat']
box_5 = ['horse', 'cloud', 'storm']
box_6 = ['rocket']
box_7 = []
box_8 = ['elephant', 'cup', 'shark']
box_9 = []
box_10 = []
box_11 = ['lion', 'mountain', 'thread', 'snow', 'oven']

# Remove the cloud from Box 5
box_5.remove('cloud')

# Move the coat and the pan from Box 4 to Box 8
box_8.extend(box_4)
box_4.clear()

# Put the bracelet into Box 11
box_11.append('bracelet')

# Replace the coat and the elephant and the cup with the charger and the thunder and the bell in Box 8
box_8 = ['charger', 'thunder', 'bell']

# Remove the pan and the thunder from Box 8
box_8.remove('pan')
box_8.remove('thunder')

# Replace the storm with the microwave in Box 5
box_5 = ['horse', 'microwave']

# Replace the motorcycle with the tape in Box 3
box_3[1] = 'tape'

# Replace the rocket with the clock in Box 6
box_6[0] = 'clock'

# Swap the charger in Box 8 with the horse in Box 5
box_5[0], box_8[0] = box_8[0], box_5[0]

# Move the thread and the lion and the bracelet from Box 11 to Box 2
box_2.extend([box_11.pop(2), box_11.pop(1), box_11.pop(0)])

# Remove the table and the boot from Box 1
box_1.remove('table')
box_1.remove('boot')

# Remove the oven and the mountain and the snow from Box 11
box_11.remove('oven')
box_11.remove('mountain')
box_11.remove('snow')

# Swap the sandals in Box 2 with the charger in Box 5
box_2[0], box_5[1] = box_5[1], box_2[0]

# Swap the pen in Box 2 with the tape in Box 3
box_2[1], box_3[1] = box_3[1], box_2[1]

# Replace the tie and the needle with the bus and the mask in Box 1
box_1 = ['bus', 'mask']

# Replace the bracelet and the perfume and the submarine with the cup and the whistle and the skirt in Box 3
box_3 = ['cup', 'whistle', 'skirt']

# Swap the mask in Box 1 with the skirt in Box 3
box_1[1], box_3[2] = box_3[2], box_1[1]

# Move the shark and the bell from Box 8 to Box 10
box_10.extend([box_8.pop(2), box_8.pop(1)])

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