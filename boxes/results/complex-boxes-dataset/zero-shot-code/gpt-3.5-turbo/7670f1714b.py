box_0 = ['shelf', 'blanket', 'controller', 'drum']
box_1 = ['coral', 'tape', 'star']
box_2 = ['oven', 'coin', 'polish', 'boat', 'thread']
box_3 = []
box_4 = []
box_5 = ['bag']

# Swap thread in Box 2 with drum in Box 0
box_0[box_0.index('drum')], box_2[box_2.index('thread')] = box_2[box_2.index('thread')], box_0[box_0.index('drum')]

# Move polish and oven from Box 2 to Box 5
box_5.extend([box_2.pop(box_2.index('polish')), box_2.pop(box_2.index('oven'))])

# Remove thread and shelf from Box 0
box_0.remove('thread')
box_0.remove('shelf')

# Replace drum, boat, and coin with scissors, train, and cat in Box 2
box_2[box_2.index('drum')] = 'scissors'
box_2[box_2.index('boat')] = 'train'
box_2[box_2.index('coin')] = 'cat'

# Swap polish in Box 5 with blanket in Box 0
box_0[box_0.index('blanket')], box_5[box_5.index('polish')] = box_5[box_5.index('polish')], box_0[box_0.index('blanket')]

# Put car and paint into Box 4
box_4.extend(['car', 'paint'])

# Move paint and car from Box 4 to Box 2
box_2.extend([box_4.pop(box_4.index('paint')), box_4.pop(box_4.index('car'))])

# Replace cat with shoes in Box 2
box_2[box_2.index('cat')] = 'shoes'

# Move coral, star, and tape from Box 1 to Box 2
box_2.extend([box_1.pop(box_1.index('coral')), box_1.pop(box_1.index('star')), box_1.pop(box_1.index('tape'))])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)