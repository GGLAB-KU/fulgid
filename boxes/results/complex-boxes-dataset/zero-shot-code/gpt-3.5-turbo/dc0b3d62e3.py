box_0 = ['rock', 'flute', 'scissors', 'storm', 'telescope']
box_1 = []
box_2 = ['book', 'elephant', 'tie']
box_3 = ['table', 'cloud', 'cup', 'brush', 'note']
box_4 = []
box_5 = ['game']
box_6 = ['bracelet', 'laptop', 'oven', 'speaker']

# Swap the note in Box 3 with the oven in Box 6
box_3.remove('note')
box_6.remove('oven')
box_3.append('oven')
box_6.append('note')

# Replace the note and the laptop and the bracelet with the pillow and the gloves and the watch in Box 6
box_6.remove('note')
box_6.remove('laptop')
box_6.remove('bracelet')
box_6.append('pillow')
box_6.append('gloves')
box_6.append('watch')

# Swap the game in Box 5 with the brush in Box 3
box_5.remove('game')
box_3.remove('brush')
box_5.append('brush')
box_3.append('game')

# Replace the tie and the elephant with the ship and the phone in Box 2
box_2.remove('tie')
box_2.remove('elephant')
box_2.append('ship')
box_2.append('phone')

# Put the lipstick and the drum into Box 2
box_2.append('lipstick')
box_2.append('drum')

# Swap the drum in Box 2 with the cloud in Box 3
box_2.remove('drum')
box_3.remove('cloud')
box_2.append('cloud')
box_3.append('drum')

# Move the gloves and the watch from Box 6 to Box 5
box_6.remove('gloves')
box_6.remove('watch')
box_5.append('gloves')
box_5.append('watch')

# Replace the phone with the pot in Box 2
box_2.remove('phone')
box_2.append('pot')

# Put the telescope into Box 6
box_6.append('telescope')

# Put the horn and the mask and the tie into Box 0
box_0.append('horn')
box_0.append('mask')
box_0.append('tie')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)