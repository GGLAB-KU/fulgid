box_0 = ['clock', 'mirror', 'fish', 'wire', 'card']
box_1 = []
box_2 = ['lion']
box_3 = []
box_4 = []
box_5 = ['drum']
box_6 = []
box_7 = ['island', 'pan']

# Move the drum from Box 5 to Box 6
box_6.append(box_5.pop(0))

# Remove the lion from Box 2
box_2.pop(0)

# Swap the drum in Box 6 with the wire in Box 0
box_0.append(box_6.pop(0))
box_6.append(box_0.pop(3))

# Swap the island in Box 7 with the wire in Box 6
box_6.append(box_7.pop(0))
box_7.append(box_6.pop(1))

# Move the island from Box 6 to Box 7
box_7.append(box_6.pop(0))

# Put the key and the sun and the forest into Box 3
box_3.extend(['key', 'sun', 'forest'])

# Put the guitar into Box 6
box_6.append('guitar')

# Replace the key with the horn in Box 3
box_3.remove('key')
box_3.append('horn')

# Move the island and the wire and the pan from Box 7 to Box 2
box_2.extend([box_7.pop(0), box_6.pop(0), box_7.pop(0)])

# Remove the mirror from Box 0
box_0.remove('mirror')

# Remove the forest from Box 3
box_3.remove('forest')

# Remove the sun and the horn from Box 3
box_3.remove('sun')
box_3.remove('horn')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)