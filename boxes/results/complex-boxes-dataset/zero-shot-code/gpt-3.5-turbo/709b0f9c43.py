box_0 = ['pot', 'headphone', 'mask', 'coat']
box_1 = ['keyboard', 'desert', 'watch', 'paint']
box_2 = []
box_3 = ['shoe', 'fridge', 'mixer', 'chair']
box_4 = ['rocket', 'whistle', 'tree', 'drum']
box_5 = ['table', 'glasses', 'tiger']
box_6 = ['pan', 'vase', 'microwave', 'towel', 'tie']

# Move the glasses, table, and tiger from Box 5 to Box 4
box_4.extend([box_5.pop(box_5.index('glasses'))])
box_4.extend([box_5.pop(box_5.index('table'))])
box_4.extend([box_5.pop(box_5.index('tiger'))])

# Put the rain into Box 0
box_0.append('rain')

# Move the pot and headphone from Box 0 to Box 5
box_5.extend([box_0.pop(box_0.index('pot'))])
box_5.extend([box_0.pop(box_0.index('headphone'))])

# Move the shoe from Box 3 to Box 4
box_4.append(box_3.pop(box_3.index('shoe')))

# Remove the chair and mixer from Box 3
box_3.remove('chair')
box_3.remove('mixer')

# Remove the tie from Box 6
box_6.remove('tie')

# Remove the fridge from Box 3
box_3.remove('fridge')

# Remove the whistle from Box 4
box_4.remove('whistle')

# Replace the microwave, pan, and vase with the planet, card, and bus in Box 6
box_6.remove('microwave')
box_6.remove('pan')
box_6.remove('vase')
box_6.extend(['planet', 'card', 'bus'])

# Swap the rain in Box 0 with the drum in Box 4
box_0.append(box_4.pop(box_4.index('drum')))

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)