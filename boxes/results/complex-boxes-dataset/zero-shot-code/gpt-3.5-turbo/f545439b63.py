box0 = ['toothpaste', 'vase', 'moon', 'grass', 'helmet']
box1 = []
box2 = ['makeup', 'skirt']
box3 = ['thunder', 'wallet', 'snow', 'violin']
box4 = []

# Move the helmet and the grass from Box 0 to Box 4
box4.append(box0.pop(box0.index('helmet')))
box4.append(box0.pop(box0.index('grass')))

# Empty Box 0
box0 = []

# Put the guitar and the leaf and the gloves into Box 0
box0.extend(['guitar', 'leaf', 'gloves'])

# Swap the makeup in Box 2 with the grass in Box 4
box2[box2.index('makeup')], box4[box4.index('grass')] = box4[box4.index('grass')], box2[box2.index('makeup')]

# Replace the violin with the drum in Box 3
box3[box3.index('violin')] = 'drum'

# Put the makeup into Box 3
box3.append(box2.pop(box2.index('makeup')))

# Move the leaf from Box 0 to Box 4
box4.append(box0.pop(box0.index('leaf')))

# Remove the wallet and the drum from Box 3
box3.remove('wallet')
box3.remove('drum')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)