box_0 = ['rain', 'lightning', 'headphone', 'vase', 'ship']
box_1 = ['seaweed', 'desert', 'coin']
box_2 = ['bag']
box_3 = ['rock', 'cloud', 'jungle']
box_4 = []
box_5 = ['lock', 'book', 'lion', 'sun']
box_6 = ['sandals', 'puzzle', 'violin', 'laptop', 'truck']
box_7 = ['bicycle']
box_8 = ['shirt', 'planet']
box_9 = ['oven', 'paint', 'wig', 'belt', 'dress']
box_10 = ['bell']
box_11 = ['fork', 'console', 'cow', 'thunder', 'mirror']

# Move seaweed, desert, and coin from Box 1 to Box 8
box_8.extend([box_1.pop(box_1.index('seaweed')), box_1.pop(box_1.index('desert')), box_1.pop(box_1.index('coin'))])

# Put starfish and butterfly into Box 6
box_6.extend(['starfish', 'butterfly'])

# Swap bell in Box 10 with bicycle in Box 7
box_10[0], box_7[0] = box_7[0], box_10[0]

# Remove fork, cow, and console from Box 11
box_11.remove('fork')
box_11.remove('cow')
box_11.remove('console')

# Swap truck in Box 6 with desert in Box 8
box_6[box_6.index('truck')], box_8[box_8.index('desert')] = box_8[box_8.index('desert')], box_6[box_6.index('truck')]

# Put tie into Box 10
box_10.append('tie')

# Move thunder and mirror from Box 11 to Box 2
box_2.extend([box_11.pop(box_11.index('thunder')), box_11.pop(box_11.index('mirror'))])

# Move bell from Box 7 to Box 5
box_5.append(box_7.pop(0))

# Put battery and mixer into Box 8
box_8.extend(['battery', 'mixer'])

# Move wig, dress, and belt from Box 9 to Box 1
box_1.extend([box_9.pop(box_9.index('wig')), box_9.pop(box_9.index('dress')), box_9.pop(box_9.index('belt'))])

# Swap dress in Box 1 with desert in Box 6
box_1[box_1.index('dress')], box_6[box_6.index('desert')] = box_6[box_6.index('desert')], box_1[box_1.index('dress')]

# Move sandals and laptop from Box 6 to Box 10
box_10.extend([box_6.pop(box_6.index('sandals')), box_6.pop(box_6.index('laptop'))])

# Move puzzle from Box 6 to Box 11
box_11.append(box_6.pop(box_6.index('puzzle')))

# Remove vase and rain from Box 0
box_0.remove('vase')
box_0.remove('rain')

# Replace wig, belt, and desert with zipper, snow, and tape in Box 1
box_1[box_1.index('wig')] = 'zipper'
box_1[box_1.index('belt')] = 'tape'
box_1[box_1.index('desert')] = 'snow'

# Empty Box 3
box_3.clear()

# Move puzzle from Box 11 to Box 6
box_6.append(box_11.pop(box_11.index('puzzle')))

# Move puzzle, dress, and violin from Box 6 to Box 9
box_9.extend([box_6.pop(box_6.index('puzzle')), box_6.pop(box_6.index('dress')), box_6.pop(box_6.index('violin'))])

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