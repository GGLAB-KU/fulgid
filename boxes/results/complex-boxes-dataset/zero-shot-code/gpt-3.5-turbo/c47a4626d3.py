box_0 = []
box_1 = ['umbrella', 'fish']
box_2 = ['telescope']
box_3 = ['pillow', 'thread', 'coral', 'camera', 'river', 'rocket', 'paint', 'magnet']
box_4 = []
box_5 = ['perfume', 'shoe', 'cup', 'dolphin', 'key']
box_6 = ['scarf']
box_7 = ['wire', 'submarine']
box_8 = ['mirror', 'pan']
box_9 = ['flower', 'card', 'fish', 'coat', 'polish']
box_10 = []

# Put the umbrella and the fish into Box 1
box_1.extend(['umbrella', 'fish'])

# Swap the scarf in Box 9 with the flower in Box 6
box_6.remove('flower')
box_9.remove('scarf')
box_6.append('scarf')
box_9.append('flower')

# Remove the beach and the umbrella and the basket from Box 1
box_1.remove('umbrella')
box_1.remove('fish')

# Remove the spoon from Box 4
box_4.remove('spoon')

# Remove the wire from Box 7
box_7.remove('wire')

# Put the coral and the camera and the river into Box 3
box_3.extend(['coral', 'camera', 'river'])

# Put the key and the submarine into Box 7
box_7.extend(['key', 'submarine'])

# Move the scarf from Box 6 to Box 4
box_6.remove('scarf')
box_4.append('scarf')

# Put the rocket and the paint and the magnet into Box 3
box_3.extend(['rocket', 'paint', 'magnet'])

# Put the razor into Box 0
box_0.append('razor')

# Remove the submarine from Box 7
box_7.remove('submarine')

# Move the scarf from Box 4 to Box 6
box_4.remove('scarf')
box_6.append('scarf')

# Replace the fish with the ocean in Box 1
box_1.remove('fish')
box_1.append('ocean')

# Swap the telescope in Box 2 with the razor in Box 0
box_0.remove('razor')
box_2.remove('telescope')
box_0.append('telescope')
box_2.append('razor')

# Swap the key in Box 7 with the dolphin in Box 5
box_5.remove('dolphin')
box_7.remove('key')
box_5.append('key')
box_7.append('dolphin')

# Remove the thread from Box 3
box_3.remove('thread')

# Move the ocean from Box 1 to Box 7
box_1.remove('ocean')
box_7.append('ocean')

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