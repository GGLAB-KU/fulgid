box_0 = ['fish', 'toothbrush']
box_1 = ['cloud', 'razor', 'soap']
box_2 = ['scarf', 'lamp']
box_3 = ['grinder', 'tie', 'cow']
box_4 = ['whistle', 'card', 'elephant']
box_5 = ['battery']
box_6 = ['pot', 'blanket', 'shark', 'charger', 'lightning']
box_7 = ['horse', 'candle']
box_8 = ['towel', 'needle', 'jungle', 'blender']
box_9 = []
box_10 = ['toothpaste', 'belt', 'speaker', 'key', 'table']
box_11 = []
box_12 = ['swimsuit']
box_13 = []

# Move the towel and the needle and the blender from Box 8 to Box 7
box_7.extend(box_8[0:3])
box_8 = []

# Swap the lightning in Box 6 with the whistle in Box 4
box_4[0], box_6[4] = box_6[4], box_4[0]

# Put the charger into Box 3
box_3.append(box_6[3])
box_6.remove(box_6[3])

# Swap the jungle in Box 8 with the battery in Box 5
box_5[0], box_8[2] = box_8[2], box_5[0]

# Move the key and the toothpaste and the speaker from Box 10 to Box 8
box_8.extend(box_10[3:6])
box_10 = box_10[0:3]

# Remove the cow from Box 3
box_3.remove('cow')

# Put the cup and the vase and the umbrella into Box 0
box_0.extend(['cup', 'vase', 'umbrella'])

# Move the razor and the soap and the cloud from Box 1 to Box 9
box_9.extend(box_1[0:3])
box_1 = []

# Put the truck into Box 9
box_9.append('truck')

# Replace the fish and the toothbrush with the battery and the car in Box 0
box_0 = ['battery', 'car']

# Move the charger and the shark and the blanket from Box 6 to Box 8
box_8.extend(box_6[3:6])
box_6 = box_6[0:3]

# Swap the table in Box 10 with the grinder in Box 3
box_3[0], box_10[4] = box_10[4], box_3[0]

# Empty Box 6
box_6 = []

# Replace the scarf with the flute in Box 2
box_2[0] = 'flute'

# Remove the towel and the needle from Box 7
box_7 = []

# Replace the blanket with the game in Box 8
box_8[1] = 'game'

# Replace the belt and the grinder with the grass and the wig in Box 10
box_10[1], box_3[0] = 'grass', 'wig'

# Move the horse and the blender and the candle from Box 7 to Box 3
box_3.extend(box_7[0:3])
box_7 = []

# Move the card and the lightning and the elephant from Box 4 to Box 13
box_13.extend(box_4[1:4])
box_4 = box_4[0:1]

# Put the horn into Box 2
box_2.append('horn')

# Replace the lamp and the horn and the flute with the comet and the perfume and the guitar in Box 2
box_2 = ['comet', 'perfume', 'guitar']

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
print("Box 13:", box_13)