box_0 = ['hat', 'lightning', 'needle', 'boat', 'sandals']
box_1 = ['desert', 'comet', 'chair', 'table']
box_2 = []
box_3 = []
box_4 = ['bracelet', 'frame', 'helmet', 'shoe', 'sun']

# Replace the helmet and the frame with the car and the planet in Box 4
box_4[box_4.index('helmet')] = 'car'
box_4[box_4.index('frame')] = 'planet'

# Swap the desert in Box 1 with the needle in Box 0
box_0[box_0.index('needle')], box_1[box_1.index('desert')] = box_1[box_1.index('desert')], box_0[box_0.index('needle')]

# Put the perfume and the shelf into Box 1
box_1.extend(['perfume', 'shelf'])

# Move the sandals and the hat and the desert from Box 0 to Box 2
box_2.extend([box_0.pop(box_0.index('sandals')), box_0.pop(box_0.index('hat')), box_0.pop(box_0.index('desert'))])

# Remove the perfume and the table from Box 1
box_1.remove('perfume')
box_1.remove('table')

# Remove the lightning and the boat from Box 0
box_0.remove('lightning')
box_0.remove('boat')

# Remove the sun and the bracelet from Box 4
box_4.remove('sun')
box_4.remove('bracelet')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)