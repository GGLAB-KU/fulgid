box_0 = ['headphone']
box_1 = []
box_2 = ['microwave', 'octopus', 'table', 'lamp', 'plate']
box_3 = []
box_4 = ['pants', 'train']

# Remove the table from Box 2
box_2.remove('table')

# Swap the octopus in Box 2 with the headphone in Box 0
box_0.remove('headphone')
box_2.remove('octopus')
box_0.append('octopus')
box_2.append('headphone')

# Put the dress into Box 0
box_0.append('dress')

# Put the plate into Box 4
box_4.append('plate')

# Replace the lamp with the ring in Box 2
box_2.remove('lamp')
box_2.append('ring')

# Put the puzzle and the jungle into Box 3
box_3.append('puzzle')
box_3.append('jungle')

# Replace the octopus with the freezer in Box 0
box_0.remove('octopus')
box_0.append('freezer')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)