box_0 = []
box_1 = ['earring', 'pants', 'rocket', 'octopus', 'truck']
box_2 = ['dog', 'jacket', 'charger']
box_3 = ['pan']
box_4 = ['shirt']
box_5 = []
box_6 = ['flute', 'game', 'piano', 'lipstick']
box_7 = ['coat', 'fridge', 'bicycle']
box_8 = ['microwave', 'ship', 'grinder', 'dress']
box_9 = ['tree', 'towel', 'blanket', 'table']

# Remove ship from Box 8
box_8.remove('ship')

# Remove octopus from Box 1
box_1.remove('octopus')

# Remove coat from Box 7
box_7.remove('coat')

# Replace truck, earring, and rocket with phone, dress, and umbrella in Box 1
box_1.remove('truck')
box_1.remove('earring')
box_1.remove('rocket')
box_1.extend(['phone', 'dress', 'umbrella'])

# Move pan from Box 3 to Box 8
box_3.remove('pan')
box_8.append('pan')

# Empty Box 6
box_6.clear()

# Empty Box 8
box_8.clear()

# Remove umbrella from Box 1
box_1.remove('umbrella')

# Remove dog and jacket from Box 2
box_2.remove('dog')
box_2.remove('jacket')

# Replace shirt with skirt in Box 4
box_4.remove('shirt')
box_4.append('skirt')

# Move charger from Box 2 to Box 8
box_2.remove('charger')
box_8.append('charger')

# Swap charger in Box 8 with phone in Box 1
box_1.remove('phone')
box_1.append('charger')
box_8.remove('charger')
box_8.append('phone')

# Put soap into Box 2
box_2.append('soap')

# Swap skirt in Box 4 with towel in Box 9
box_4.remove('skirt')
box_4.append('towel')
box_9.remove('towel')
box_9.append('skirt')

# Replace pants, charger, and dress with sun, elephant, and cat in Box 1
box_1.remove('pants')
box_1.remove('charger')
box_1.remove('dress')
box_1.extend(['sun', 'elephant', 'cat'])

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