box_0 = ['cloud', 'bicycle', 'umbrella']
box_1 = ['comet', 'chair', 'pillow', 'speaker']
box_2 = ['coat', 'shoes']
box_3 = ['dress', 'storm', 'bag']
box_4 = ['lock', 'sandals', 'note']

# Remove items from Box 0
box_0.remove('umbrella')
box_0.remove('cloud')
box_0.remove('bicycle')

# Swap items between Box 2 and Box 3
box_2.remove('coat')
box_3.remove('bag')
box_2.append('bag')
box_3.append('coat')

# Add items to Box 4
box_4.append('plane')
box_4.append('scarf')

# Move items from Box 4 to Box 3
box_4.remove('scarf')
box_4.remove('lock')
box_3.append('scarf')
box_3.append('lock')

# Replace items in Box 4
box_4.remove('sandals')
box_4.remove('note')
box_4.append('coat')
box_4.append('vase')

# Remove items from Box 4
box_4.remove('vase')
box_4.remove('coat')

# Replace item in Box 4
box_4.remove('plane')
box_4.append('gloves')

# Add items to Box 0
box_0.append('elephant')
box_0.append('game')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)