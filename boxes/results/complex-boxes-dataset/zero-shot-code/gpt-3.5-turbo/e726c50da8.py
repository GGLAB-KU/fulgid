box_0 = ['console', 'chair', 'sock', 'dice', 'forest']
box_1 = ['towel', 'battery']
box_2 = ['fork', 'shampoo', 'scarf', 'scissors']
box_3 = ['ship']
box_4 = ['necklace', 'fish']
box_5 = ['starfish', 'cloud', 'motorcycle', 'bell']
box_6 = ['toothpaste', 'crown', 'bowl', 'freezer', 'blender']
box_7 = ['pants', 'keyboard', 'needle', 'bus']
box_8 = []

# Remove starfish and cloud from Box 5
box_5.remove('starfish')
box_5.remove('cloud')

# Put controller into Box 7
box_7.append('controller')

# Put flute, cat, and whistle into Box 7
box_7.extend(['flute', 'cat', 'whistle'])

# Remove scarf from Box 2
box_2.remove('scarf')

# Put whistle and tape into Box 3
box_3.extend(['whistle', 'tape'])

# Swap tape in Box 3 with fish in Box 4
box_3.remove('tape')
box_4.remove('fish')
box_3.append('fish')
box_4.append('tape')

# Put tie into Box 3
box_3.append('tie')

# Replace chair and console with car and truck in Box 0
box_0.remove('chair')
box_0.remove('console')
box_0.extend(['car', 'truck'])

# Remove car from Box 0
box_0.remove('car')

# Move ship and whistle from Box 3 to Box 5
box_3.remove('ship')
box_5.extend(['ship', 'whistle'])

# Swap blender in Box 6 with keyboard in Box 7
box_6.remove('blender')
box_7.remove('keyboard')
box_6.append('keyboard')
box_7.append('blender')

# Remove bus, whistle, and pants from Box 7
box_7.remove('bus')
box_7.remove('whistle')
box_7.remove('pants')

# Replace keyboard and toothpaste with rocket and submarine in Box 6
box_6.remove('keyboard')
box_6.remove('toothpaste')
box_6.extend(['rocket', 'submarine'])

# Move needle, flute, and blender from Box 7 to Box 6
box_7.remove('needle')
box_7.remove('flute')
box_7.remove('blender')
box_6.extend(['needle', 'flute', 'blender'])

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