box_0 = ['lion', 'wallet', 'violin', 'bell']
box_1 = ['grass', 'tie', 'sun', 'umbrella']
box_2 = ['plane', 'console', 'ship', 'charger', 'desert']
box_3 = ['bowl', 'towel']
box_4 = ['perfume', 'butterfly', 'island', 'book', 'crown']
box_5 = ['submarine', 'clock', 'glasses', 'keyboard']
box_6 = ['river', 'wig', 'pan']
box_7 = ['comet', 'pillow', 'leaf', 'phone', 'cow']

# Swap the glasses in Box 5 with the violin in Box 0
box_0[2], box_5[2] = box_5[2], box_0[2]

# Swap the violin in Box 5 with the desert in Box 2
box_2[4], box_5[2] = box_5[2], box_2[4]

# Replace the sun and the umbrella and the tie with the plate and the ring and the pot in Box 1
box_1[2:4] = ['plate', 'ring', 'pot']

# Swap the bowl in Box 3 with the desert in Box 5
box_3[0], box_5[2] = box_5[2], box_3[0]

# Remove the island from Box 4
box_4.remove('island')

# Replace the crown and the book and the perfume with the shelf and the wallet and the coin in Box 4
box_4[3:6] = ['shelf', 'wallet', 'coin']

# Remove the wig and the river from Box 6
box_6.remove('wig')
box_6.remove('river')

# Replace the violin and the plane with the grinder and the toothpaste in Box 2
box_2[0], box_5[2] = box_5[2], box_2[0]

# Replace the towel with the whistle in Box 3
box_3[1] = 'whistle'

# Put the coat and the candle and the razor into Box 0
box_0.extend(['coat', 'candle', 'razor'])

# Replace the shelf and the coin with the dice and the elephant in Box 4
box_4[3:5] = ['dice', 'elephant']

# Swap the grinder in Box 2 with the grass in Box 1
box_1[0], box_2[0] = box_2[0], box_1[0]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)