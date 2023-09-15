box_0 = ['cup', 'jacket']
box_1 = ['sandals', 'shorts', 'perfume', 'ring']
box_2 = ['cloud', 'tiger', 'island']
box_3 = ['piano', 'scarf']
box_4 = ['toy', 'violin', 'fish', 'zipper']
box_5 = ['bus', 'train']
box_6 = ['thread', 'blanket', 'plate']

# Remove the blanket and the thread from Box 6
box_6.remove('blanket')
box_6.remove('thread')

# Move the island from Box 2 to Box 0
box_0.append(box_2.pop(box_2.index('island')))

# Put the octopus and the pot into Box 2
box_2.extend(['octopus', 'pot'])

# Swap the toy in Box 4 with the ring in Box 1
box_1[box_1.index('ring')], box_4[box_4.index('toy')] = box_4[box_4.index('toy')], box_1[box_1.index('ring')]

# Remove the octopus and the pot and the tiger from Box 2
box_2.remove('octopus')
box_2.remove('pot')
box_2.remove('tiger')

# Put the bird and the cup and the tree into Box 3
box_3.extend(['bird', 'cup', 'tree'])

# Remove the train from Box 5
box_5.remove('train')

# Replace the cloud with the pants in Box 2
box_2[box_2.index('cloud')] = 'pants'

# Swap the cup in Box 3 with the violin in Box 4
box_3[box_3.index('cup')], box_4[box_4.index('violin')] = box_4[box_4.index('violin')], box_3[box_3.index('cup')]

# Swap the shorts in Box 1 with the plate in Box 6
box_1[box_1.index('shorts')], box_6[box_6.index('plate')] = box_6[box_6.index('plate')], box_1[box_1.index('shorts')]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)