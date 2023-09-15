box_0 = ['note', 'mirror', 'belt']
box_1 = ['grass']
box_2 = ['scarf', 'usb', 'sculpture']
box_3 = ['fish', 'microwave', 'wallet', 'needle']
box_4 = []
box_5 = ['shirt', 'swimsuit', 'bicycle']
box_6 = ['mixer', 'flute']
box_7 = ['sandals', 'grinder']
box_8 = ['rocket', 'pot']
box_9 = []
box_10 = ['pan', 'shorts', 'telescope', 'glasses', 'laptop']
box_11 = ['branch', 'charger']
box_12 = []

# Move the charger from Box 11 to Box 8
box_8.append(box_11.pop(box_11.index('charger')))

# Remove the rocket, charger, and pot from Box 8
box_8.remove('rocket')
box_8.remove('charger')
box_8.remove('pot')

# Put the lock into Box 1
box_1.append('lock')

# Swap the grass in Box 1 with the branch in Box 11
box_1[0], box_11[0] = box_11[0], box_1[0]

# Remove the flute and mixer from Box 6
box_6.remove('flute')
box_6.remove('mixer')

# Swap the grass in Box 11 with the wallet in Box 3
box_11[0], box_3[2] = box_3[2], box_11[0]

# Replace the note, belt, and mirror with the plane, sandals, and thunder in Box 0
box_0 = ['plane', 'sandals', 'thunder']

# Put the sandals into Box 5
box_5.append(box_0.pop(box_0.index('sandals')))

# Swap the glasses in Box 10 with the scarf in Box 2
box_10[3], box_2[0] = box_2[0], box_10[3]

# Put the flute, camera, and note into Box 0
box_0.extend(['flute', 'camera', 'note'])

# Remove the laptop and telescope from Box 10
box_10.remove('laptop')
box_10.remove('telescope')

# Replace the wallet with the coat in Box 11
box_11[1] = 'coat'

# Move the grinder and sandals from Box 7 to Box 4
box_4.append(box_7.pop(box_7.index('grinder')))
box_4.append(box_7.pop(box_7.index('sandals')))

# Move the shirt and bicycle from Box 5 to Box 7
box_7.append(box_5.pop(box_5.index('shirt')))
box_7.append(box_5.pop(box_5.index('bicycle')))

# Remove the sandals and grinder from Box 4
box_4.remove('sandals')
box_4.remove('grinder')

# Swap the needle in Box 3 with the shirt in Box 7
box_3[3], box_7[0] = box_7[0], box_3[3]

# Remove the shirt and microwave from Box 3
box_3.remove('shirt')
box_3.remove('microwave')

# Remove the fish from Box 3
box_3.remove('fish')

# Remove the plane from Box 0
box_0.remove('plane')

# Remove the bicycle and needle from Box 7
box_7.remove('bicycle')
box_7.remove('needle')

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