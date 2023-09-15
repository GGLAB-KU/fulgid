box_0 = ['earring']
box_1 = []
box_2 = ['card', 'snow']
box_3 = []
box_4 = ['lightning', 'wire']
box_5 = ['mixer']
box_6 = ['fish', 'mountain', 'motorcycle', 'towel']

# Remove the mixer from Box 5
box_5.remove('mixer')

# Move the card from Box 2 to Box 5
box_5.append(box_2.pop(box_2.index('card')))

# Move the snow from Box 2 to Box 1
box_1.append(box_2.pop(box_2.index('snow')))

# Put the spoon into Box 5
box_5.append('spoon')

# Remove the lightning and the wire from Box 4
box_4.remove('lightning')
box_4.remove('wire')

# Move the card from Box 5 to Box 1
box_1.append(box_5.pop(box_5.index('card')))

# Move the towel and the fish and the motorcycle from Box 6 to Box 0
box_0.extend([box_6.pop(box_6.index('towel')), box_6.pop(box_6.index('fish')), box_6.pop(box_6.index('motorcycle'))])

# Swap the snow in Box 1 with the mountain in Box 6
box_1.append(box_6.pop(box_6.index('mountain')))
box_6.append(box_1.pop(box_1.index('snow')))

# Replace the spoon with the truck in Box 5
box_5.append('truck')
box_5.remove('spoon')

# Swap the truck in Box 5 with the card in Box 1
box_5.append(box_1.pop(box_1.index('card')))
box_1.append('truck')

# Move the towel from Box 0 to Box 1
box_1.append(box_0.pop(box_0.index('towel')))

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)