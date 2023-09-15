box_0 = ['comb', 'key', 'rock', 'shampoo', 'towel']
box_1 = ['storm', 'dice', 'rocket', 'sandals']
box_2 = ['bear', 'shorts', 'belt']
box_3 = []
box_4 = []
box_5 = ['oven', 'pan', 'game', 'bicycle']
box_6 = ['coat', 'branch', 'bracelet', 'blanket']

# Remove items from Box 1
box_1.remove('storm')
box_1.remove('rocket')
box_1.remove('sandals')

# Swap items between Box 0 and Box 5
box_0.remove('shampoo')
box_5.remove('game')
box_0.append('game')
box_5.append('shampoo')

# Empty Box 6
box_6 = []

# Move items from Box 2 to Box 0
box_0.extend(box_2)
box_2 = []

# Remove items from Box 0
box_0.remove('towel')
box_0.remove('shorts')

# Put items into Box 2
box_2.extend(['fish', 'whistle'])

# Remove item from Box 0
box_0.remove('comb')

# Swap items between Box 2 and Box 1
box_2.remove('whistle')
box_1.remove('dice')
box_2.append('dice')
box_1.append('whistle')

# Put items into Box 1
box_1.extend(['rain', 'bell', 'mountain'])

# Remove item from Box 2
box_2.remove('fish')

# Print the final state of the boxes
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)