box_0 = ['plane', 'dress']
box_1 = ['frame', 'fork']
box_2 = ['shark', 'wig', 'toy', 'truck', 'storm']
box_3 = ['umbrella', 'train', 'cow', 'brush', 'starfish']
box_4 = ['belt']
box_5 = ['boat', 'perfume', 'cat', 'button']
box_6 = ['horn', 'shirt', 'shelf']
box_7 = ['shoe', 'whistle', 'grass']
box_8 = ['apple']
box_9 = ['headphone']
box_10 = ['flute', 'thunder']
box_11 = []
box_12 = ['island', 'branch', 'polish']
box_13 = ['lamp', 'tiger', 'thread', 'lightning', 'motorcycle']
box_14 = ['comb']

# Swap headphone in Box 9 with flute in Box 10
box_9, box_10 = box_10, box_9

# Swap apple in Box 8 with wig in Box 2
box_8, box_2[1] = box_2[1], box_8

# Remove storm and truck from Box 2
box_2.remove('storm')
box_2.remove('truck')

# Swap umbrella in Box 3 with tiger in Box 13
box_3[0], box_13[1] = box_13[1], box_3[0]

# Put leaf into Box 11
box_11.append('leaf')

# Remove button, perfume, and cat from Box 5
box_5.remove('button')
box_5.remove('perfume')
box_5.remove('cat')

# Replace leaf with ocean in Box 11
box_11.remove('leaf')
box_11.append('ocean')

# Replace wig with frame in Box 8
box_8, box_2[1] = box_2[1], box_8

# Move belt from Box 4 to Box 14
box_4.remove('belt')
box_14.append('belt')

# Replace train with shampoo in Box 3
box_3[1] = 'shampoo'

# Put keyboard into Box 9
box_9.append('keyboard')

# Move shark and apple from Box 2 to Box 7
box_2.remove('shark')
box_2.remove('apple')
box_7.extend(['shark', 'apple'])

# Swap polish in Box 12 with ocean in Box 11
box_12[2], box_11[0] = box_11[0], box_12[2]

# Empty Box 10
box_10 = []

# Replace boat with scissors in Box 5
box_5[0] = 'scissors'

# Replace scissors with rocket in Box 5
box_5[0] = 'rocket'

# Swap horn in Box 6 with flute in Box 9
box_6[0], box_9[1] = box_9[1], box_6[0]

# Replace rocket with glasses in Box 5
box_5[0] = 'glasses'

# Move frame and fork from Box 1 to Box 3
box_1.remove('frame')
box_1.remove('fork')
box_3.extend(['frame', 'fork'])

# Empty Box 8
box_8 = []

# Replace keyboard with paint in Box 9
box_9[1] = 'paint'

# Swap lightning in Box 13 with glasses in Box 5
box_13[3], box_5[0] = box_5[0], box_13[3]

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
print("Box 14:", box_14)