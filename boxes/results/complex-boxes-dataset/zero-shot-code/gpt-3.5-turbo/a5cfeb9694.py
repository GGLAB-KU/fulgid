box_0 = ['harmonica', 'soap', 'coat', 'clock']
box_1 = []
box_2 = ['drum']
box_3 = ['toothbrush', 'shoes', 'mountain', 'bowl']
box_4 = ['tiger', 'microwave']
box_5 = ['plane', 'umbrella', 'crown', 'jacket']
box_6 = []
box_7 = ['cloud', 'polish', 'controller', 'violin', 'cat']
box_8 = ['thunder', 'flower', 'earring', 'desert', 'candle']
box_9 = ['table']

# Move the shoes from Box 3 to Box 4
box_4.append(box_3.pop(box_3.index('shoes')))

# Put the meteor and the mixer and the thread into Box 5
box_5.extend(['meteor', 'mixer', 'thread'])

# Remove the earring from Box 8
box_8.remove('earring')

# Replace the drum with the freezer in Box 2
box_2[0] = 'freezer'

# Remove the clock and the coat from Box 0
box_0.remove('clock')
box_0.remove('coat')

# Swap the cat in Box 7 with the flower in Box 8
box_7[box_7.index('cat')], box_8[box_8.index('flower')] = box_8[box_8.index('flower')], box_7[box_7.index('cat')]

# Replace the freezer with the ship in Box 2
box_2[0] = 'ship'

# Put the guitar and the oven and the flower into Box 2
box_2.extend(['guitar', 'oven', 'flower'])

# Move the umbrella and the meteor from Box 5 to Box 2
box_2.extend(['umbrella', 'meteor'])
box_5.remove('umbrella')
box_5.remove('meteor')

# Swap the thunder in Box 8 with the controller in Box 7
box_8[box_8.index('thunder')], box_7[box_7.index('controller')] = box_7[box_7.index('controller')], box_8[box_8.index('thunder')]

# Remove the violin and the polish from Box 7
box_7.remove('violin')
box_7.remove('polish')

# Remove the cat from Box 8
box_8.remove('cat')

# Put the needle into Box 5
box_5.append('needle')

# Put the glove and the jacket into Box 4
box_4.extend(['glove', 'jacket'])

# Swap the jacket in Box 5 with the toothbrush in Box 3
box_5[box_5.index('jacket')], box_3[box_3.index('toothbrush')] = box_3[box_3.index('toothbrush')], box_5[box_5.index('jacket')]

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