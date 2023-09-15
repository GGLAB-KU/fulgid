box_0 = ['jungle', 'gloves']
box_1 = ['pen']
box_2 = ['mixer']
box_3 = ['fridge', 'telescope', 'river', 'lion', 'shirt']
box_4 = ['mountain', 'doll', 'beach', 'shampoo']
box_5 = ['chair', 'hat', 'vase']
box_6 = ['clock']
box_7 = ['perfume', 'grinder', 'laptop']

# Put the drum into Box 6
box_6.append('drum')

# Put the shorts and the speaker and the bracelet into Box 7
box_7.extend(['shorts', 'speaker', 'bracelet'])

# Remove the mixer from Box 2
box_2.remove('mixer')

# Put the boot and the rocket and the spoon into Box 5
box_5.extend(['boot', 'rocket', 'spoon'])

# Put the perfume into Box 5
box_5.append('perfume')

# Remove the pen from Box 1
box_1.remove('pen')

# Remove the hat from Box 5
box_5.remove('hat')

# Swap the gloves in Box 0 with the mountain in Box 4
box_0.remove('gloves')
box_4.remove('mountain')
box_0.append('mountain')
box_4.append('gloves')

# Replace the shirt and the telescope with the tiger and the blanket in Box 3
box_3.remove('shirt')
box_3.remove('telescope')
box_3.extend(['tiger', 'blanket'])

# Put the fork into Box 0
box_0.append('fork')

# Move the fork and the mountain and the jungle from Box 0 to Box 2
box_0.remove('fork')
box_2.extend(['fork', 'mountain', 'jungle'])

# Move the vase and the spoon from Box 5 to Box 4
box_5.remove('vase')
box_5.remove('spoon')
box_4.extend(['vase', 'spoon'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)