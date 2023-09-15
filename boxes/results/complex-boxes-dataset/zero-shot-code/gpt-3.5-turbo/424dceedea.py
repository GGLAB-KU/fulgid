box_0 = ['mask', 'branch', 'desert']
box_1 = ['shorts', 'comb', 'submarine', 'dolphin']
box_2 = ['cat']
box_3 = ['seaweed', 'camera', 'note', 'elephant']
box_4 = ['plate', 'skirt', 'phone', 'blender']
box_5 = ['lightning', 'fish', 'razor']
box_6 = ['moon']
box_7 = ['bus', 'card', 'boat', 'magnet']

# Remove desert and mask from Box 0
box_0.remove('desert')
box_0.remove('mask')

# Swap note in Box 3 with cat in Box 2
note = box_3.pop(box_3.index('note'))
box_2.append(note)

# Put scissors, spoon, and tiger into Box 7
box_7.extend(['scissors', 'spoon', 'tiger'])

# Put rocket and seaweed into Box 3
box_3.append('rocket')
box_3.append('seaweed')

# Remove blender and phone from Box 4
box_4.remove('blender')
box_4.remove('phone')

# Put scarf, bell, and vase into Box 6
box_6.extend(['scarf', 'bell', 'vase'])

# Swap submarine in Box 1 with skirt in Box 4
submarine = box_1.pop(box_1.index('submarine'))
box_4.append(submarine)
skirt = box_4.pop(box_4.index('skirt'))
box_1.append(skirt)

# Put guitar, river, and button into Box 5
box_5.extend(['guitar', 'river', 'button'])

# Move shorts from Box 1 to Box 7
shorts = box_1.pop(box_1.index('shorts'))
box_7.append(shorts)

# Replace comb and dolphin with basket and oven in Box 1
box_1.remove('comb')
box_1.remove('dolphin')
box_1.extend(['basket', 'oven'])

# Remove branch from Box 0
box_0.remove('branch')

# Empty Box 1
box_1 = []

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)