box_0 = ['clock', 'truck', 'glove']
box_1 = ['seaweed']
box_2 = ['butterfly']
box_3 = []
box_4 = []
box_5 = ['toothbrush', 'grinder']
box_6 = ['beach', 'telescope']
box_7 = ['mirror', 'island', 'sun', 'lightning', 'snow']
box_8 = ['helmet', 'frame']

# Put the fish and the truck into Box 7
box_7.extend(['fish', 'truck'])

# Replace the fish and the mirror and the sun with the note and the piano and the controller in Box 7
box_7.remove('fish')
box_7.remove('mirror')
box_7.remove('sun')
box_7.extend(['note', 'piano', 'controller'])

# Move the lightning from Box 7 to Box 6
box_6.append(box_7.pop(box_7.index('lightning')))

# Put the battery and the bell into Box 4
box_4.extend(['battery', 'bell'])

# Put the car and the gloves and the boat into Box 3
box_3.extend(['car', 'gloves', 'boat'])

# Put the jacket and the blender into Box 6
box_6.extend(['jacket', 'blender'])

# Move the car from Box 3 to Box 0
box_0.append(box_3.pop(box_3.index('car')))

# Replace the boat and the gloves with the hat and the microwave in Box 3
box_3.remove('boat')
box_3.remove('gloves')
box_3.extend(['hat', 'microwave'])

# Swap the butterfly in Box 2 with the hat in Box 3
box_2.append(box_3.pop(box_3.index('hat')))
box_3.append(box_2.pop(box_2.index('butterfly')))

# Move the blender and the telescope from Box 6 to Box 2
box_2.extend([box_6.pop(box_6.index('blender')), box_6.pop(box_6.index('telescope'))])

# Move the seaweed from Box 1 to Box 3
box_3.append(box_1.pop(box_1.index('seaweed')))

# Remove the lightning and the beach from Box 6
box_6.remove('lightning')
box_6.remove('beach')

# Replace the jacket with the watch in Box 6
box_6.remove('jacket')
box_6.append('watch')

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