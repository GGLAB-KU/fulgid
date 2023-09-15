box_0 = ['coin', 'umbrella']
box_1 = ['storm', 'harmonica', 'puzzle', 'boat', 'shelf']
box_2 = ['rock', 'razor', 'charger', 'shoes', 'skirt']
box_3 = ['scarf', 'sun']

# Replace the sun and the scarf with the flower and the laptop in Box 3
box_3 = ['flower', 'laptop']

# Remove the coin from Box 0
box_0.remove('coin')

# Swap the storm in Box 1 with the flower in Box 3
box_1[0], box_3[0] = box_3[0], box_1[0]

# Put the hat into Box 3
box_3.append('hat')

# Put the car and the tiger and the bicycle into Box 0
box_0.extend(['car', 'tiger', 'bicycle'])

# Move the puzzle and the harmonica and the boat from Box 1 to Box 2
box_2.extend([box_1.pop(2), box_1.pop(1), box_1.pop(0)])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)