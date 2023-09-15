box_0 = []
box_1 = ['speaker']
box_2 = ['toothpaste', 'bear', 'coin', 'ocean']
box_3 = []
box_4 = []
box_5 = ['pot', 'battery', 'magnet', 'shelf', 'sock']
box_6 = []
box_7 = []

# Replace the butterfly with the speaker in Box 1
box_1.remove('speaker')

# Move the dolphin from Box 6 to Box 0
box_0.append('dolphin')
box_6.remove('dolphin')

# Swap the shelf in Box 5 with the plane in Box 3
box_3.append('shelf')
box_5.remove('shelf')
box_5.remove('plane')
box_3.remove('shelf')

# Replace the ocean and the coin with the cow and the moon in Box 2
box_2.remove('ocean')
box_2.remove('coin')
box_2.extend(['cow', 'moon'])

# Replace the boat with the glove in Box 3
box_3.append('glove')
box_3.remove('boat')

# Put the chair and the telescope into Box 1
box_1.extend(['chair', 'telescope'])

# Put the coral and the tree into Box 3
box_3.extend(['coral', 'tree'])

# Move the dolphin from Box 0 to Box 2
box_2.append('dolphin')
box_0.remove('dolphin')

# Replace the magnet and the battery with the grass and the coat in Box 5
box_5.remove('magnet')
box_5.remove('battery')
box_5.extend(['grass', 'coat'])

# Empty Box 3
box_3 = []

# Swap the grass in Box 5 with the chair in Box 1
box_1.remove('chair')
box_5.remove('grass')
box_1.append('grass')
box_5.append('chair')

# Remove the plane and the chair and the sock from Box 5
box_5.remove('plane')
box_5.remove('chair')
box_5.remove('sock')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)