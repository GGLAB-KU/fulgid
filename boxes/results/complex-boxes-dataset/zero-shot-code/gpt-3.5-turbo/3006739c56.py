box_0 = ['scarf', 'desert', 'dolphin', 'apple', 'spoon']
box_1 = ['doll', 'star', 'razor']
box_2 = ['glasses', 'rocket']
box_3 = ['glove', 'pan', 'telescope', 'sculpture', 'puzzle']
box_4 = []
box_5 = ['mountain']
box_6 = ['charger', 'shoe', 'makeup', 'battery']

# Put the scarf, shorts, and fork into Box 6
box_6.extend(['scarf', 'shorts', 'fork'])

# Swap the makeup in Box 6 with the glove in Box 3
box_6.remove('makeup')
box_3.remove('glove')
box_6.append('glove')
box_3.append('makeup')

# Remove the charger, fork, and scarf from Box 6
box_6.remove('charger')
box_6.remove('fork')
box_6.remove('scarf')

# Remove the spoon, scarf, and dolphin from Box 0
box_0.remove('spoon')
box_0.remove('scarf')
box_0.remove('dolphin')

# Remove the rocket from Box 2
box_2.remove('rocket')

# Replace the doll with the toothbrush in Box 1
box_1.remove('doll')
box_1.append('toothbrush')

# Remove the desert and apple from Box 0
box_0.remove('desert')
box_0.remove('apple')

# Swap the toothbrush in Box 1 with the mountain in Box 5
box_1.remove('toothbrush')
box_5.remove('mountain')
box_1.append('mountain')
box_5.append('toothbrush')

# Replace the razor and star with the helmet and oven in Box 1
box_1.remove('razor')
box_1.remove('star')
box_1.append('helmet')
box_1.append('oven')

# Remove the toothbrush from Box 5
box_5.remove('toothbrush')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)