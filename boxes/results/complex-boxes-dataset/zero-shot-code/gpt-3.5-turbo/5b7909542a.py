box_0 = ['blanket']
box_1 = ['paint']
box_2 = ['speaker', 'crown', 'ship', 'wallet', 'harmonica']
box_3 = ['lipstick', 'toothpaste', 'submarine', 'perfume', 'truck']
box_4 = ['table']
box_5 = ['fish', 'controller', 'pants', 'forest', 'motorcycle']
box_6 = ['leaf', 'lightning']
box_7 = ['bell', 'soap', 'necklace', 'jacket', 'plane']
box_8 = ['microwave', 'frame', 'candle', 'thunder']

# Remove the table from Box 4
box_4.remove('table')

# Move the paint from Box 1 to Box 8
item = box_1.pop(0)
box_8.append(item)

# Move the crown and the speaker and the wallet from Box 2 to Box 0
items = box_2[:3]
box_0.extend(items)
box_2 = box_2[3:]

# Swap the microwave in Box 8 with the necklace in Box 7
item_1 = box_8.pop(0)
item_2 = box_7.pop(2)
box_8.append(item_2)
box_7.append(item_1)

# Swap the necklace in Box 8 with the speaker in Box 0
item_1 = box_8.pop(0)
item_2 = box_0.pop(1)
box_8.append(item_2)
box_0.append(item_1)

# Remove the harmonica and the ship from Box 2
box_2.remove('harmonica')
box_2.remove('ship')

# Replace the fish with the sun in Box 5
box_5.remove('fish')
box_5.append('sun')

# Replace the lipstick with the seaweed in Box 3
box_3.remove('lipstick')
box_3.append('seaweed')

# Remove the lightning and the leaf from Box 6
box_6.remove('lightning')
box_6.remove('leaf')

# Replace the seaweed and the submarine and the toothpaste with the hat and the wallet and the zipper in Box 3
box_3.remove('seaweed')
box_3.remove('submarine')
box_3.remove('toothpaste')
box_3.extend(['hat', 'wallet', 'zipper'])

# Move the candle and the paint from Box 8 to Box 7
item_1 = box_8.pop(1)
item_2 = box_8.pop(0)
box_7.extend([item_1, item_2])

# Swap the controller in Box 5 with the microwave in Box 7
item_1 = box_5.pop(1)
item_2 = box_7.pop(0)
box_5.append(item_2)
box_7.append(item_1)

# Swap the frame in Box 8 with the perfume in Box 3
item_1 = box_8.pop(1)
item_2 = box_3.pop(2)
box_8.append(item_2)
box_3.append(item_1)

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