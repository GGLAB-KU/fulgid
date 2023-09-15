box_0 = ['vase', 'flute']
box_1 = ['polish', 'camera', 'plate', 'starfish', 'coin']
box_2 = ['console', 'branch', 'jacket', 'doll', 'glove']
box_3 = ['lock', 'headphone', 'coral']
box_4 = ['toy', 'freezer', 'zipper']
box_5 = ['leaf', 'grinder', 'puzzle', 'whistle', 'keyboard']
box_6 = ['bell', 'candle', 'belt', 'fridge', 'ship']
box_7 = ['tie', 'perfume', 'shampoo', 'oven']

# Replace the necklace and the table with the vase and the flute in Box 0
box_0 = ['vase', 'flute']

# Swap the flute in Box 0 with the puzzle in Box 5
box_0, box_5 = box_5, box_0

# Remove the leaf from Box 5
box_5.remove('leaf')

# Remove the zipper and the toy from Box 4
box_4.remove('zipper')
box_4.remove('toy')

# Replace the shampoo with the lamp in Box 7
box_7[2] = 'lamp'

# Swap the coin in Box 1 with the belt in Box 6
box_1[4], box_6[2] = box_6[2], box_1[4]

# Put the book into Box 4
box_4.append('book')

# Replace the grinder and the flute with the seaweed and the magnet in Box 5
box_5[1] = 'seaweed'
box_5[2] = 'magnet'

# Move the headphone and the coral from Box 3 to Box 0
box_0.extend(box_3[1:])
box_3 = []

# Put the belt into Box 5
box_5.append('belt')

# Move the starfish and the plate and the camera from Box 1 to Box 3
box_3.extend(box_1[3:])
box_1 = box_1[:3]

# Put the microwave into Box 5
box_5.append('microwave')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)