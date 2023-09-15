box_0 = ['necklace']
box_1 = []
box_2 = ['thunder', 'bell', 'battery', 'umbrella']
box_3 = ['rocket', 'lock', 'pan', 'chair', 'charger']
box_4 = ['mountain']
box_5 = []
box_6 = ['desert', 'shorts', 'card']
box_7 = []
box_8 = ['makeup', 'sun', 'sculpture', 'boat']

# Remove umbrella from Box 2
box_2.remove('umbrella')

# Swap mountain in Box 4 with desert in Box 6
box_4, box_6 = box_6, box_4

# Remove desert from Box 4
box_4.remove('desert')

# Replace necklace with dolphin in Box 0
box_0.remove('necklace')
box_0.append('dolphin')

# Move rocket from Box 3 to Box 7
box_7.append(box_3.pop(box_3.index('rocket')))

# Remove makeup, sun, sculpture, and boat from Box 8
box_8.remove('makeup')
box_8.remove('sun')
box_8.remove('sculpture')
box_8.remove('boat')

# Empty Box 8
box_8 = []

# Swap charger in Box 3 with mountain in Box 6
box_3[box_3.index('charger')], box_6[box_6.index('mountain')] = box_6[box_6.index('mountain')], box_3[box_3.index('charger')]

# Put shampoo, magnet, and frame into Box 1
box_1.extend(['shampoo', 'magnet', 'frame'])

# Replace battery, thunder, and bell with speaker, flute, and hat in Box 2
box_2.remove('battery')
box_2.remove('thunder')
box_2.remove('bell')
box_2.extend(['speaker', 'flute', 'hat'])

# Remove pan from Box 3
box_3.remove('pan')

# Remove dolphin from Box 0
box_0.remove('dolphin')

# Remove lock, mountain, and chair from Box 3
box_3.remove('lock')
box_3.remove('mountain')
box_3.remove('chair')

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