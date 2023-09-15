box_0 = ['lipstick']
box_1 = ['laptop', 'hat', 'puzzle', 'microwave', 'dress']
box_2 = ['bracelet', 'desert']
box_3 = ['sock', 'crown', 'piano']
box_4 = ['toothpaste']
box_5 = ['leaf', 'river', 'earring']
box_6 = ['fridge', 'chair', 'storm', 'watch']

# Replace the desert and the bracelet with the grinder and the vase in Box 2
box_2.remove('desert')
box_2.remove('bracelet')
box_2.extend(['grinder', 'vase'])

# Move the storm from Box 6 to Box 3
box_6.remove('storm')
box_3.append('storm')

# Put the key and the mask into Box 2
box_2.extend(['key', 'mask'])

# Put the butterfly and the glove and the desert into Box 2
box_2.extend(['butterfly', 'glove', 'desert'])

# Replace the earring and the river and the leaf with the jacket and the comb and the octopus in Box 5
box_5.remove('earring')
box_5.remove('river')
box_5.remove('leaf')
box_5.extend(['jacket', 'comb', 'octopus'])

# Swap the chair in Box 6 with the toothpaste in Box 4
box_6.remove('chair')
box_4.remove('toothpaste')
box_6.append('toothpaste')
box_4.append('chair')

# Empty Box 2
box_2 = []

# Remove the chair from Box 4
box_4.remove('chair')

# Replace the laptop and the microwave and the dress with the grinder and the thunder and the pen in Box 1
box_1.remove('laptop')
box_1.remove('microwave')
box_1.remove('dress')
box_1.extend(['grinder', 'thunder', 'pen'])

# Empty Box 5
box_5 = []

# Move the fridge and the toothpaste and the watch from Box 6 to Box 1
box_6.remove('fridge')
box_6.remove('toothpaste')
box_6.remove('watch')
box_1.extend(['fridge', 'toothpaste', 'watch'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)