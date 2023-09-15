box_0 = ['guitar', 'tie', 'fridge']
box_1 = ['camera', 'pan', 'table', 'mixer']
box_2 = []
box_3 = ['sandals']
box_4 = []
box_5 = ['perfume', 'book', 'hat', 'mountain', 'thunder']
box_6 = ['ship']
box_7 = []
box_8 = ['needle', 'console', 'wig']

# Replace the mountain with the table in Box 5
box_5.remove('mountain')
box_5.append('table')

# Swap the wig in Box 8 with the perfume in Box 5
box_5.remove('perfume')
box_8.remove('wig')
box_5.append('wig')
box_8.append('perfume')

# Move the needle and the perfume and the console from Box 8 to Box 2
box_2.extend(['needle', 'perfume', 'console'])
box_8.remove('needle')
box_8.remove('perfume')
box_8.remove('console')

# Remove the needle from Box 2
box_2.remove('needle')

# Replace the guitar and the tie and the fridge with the flute and the makeup and the shelf in Box 0
box_0.remove('guitar')
box_0.remove('tie')
box_0.remove('fridge')
box_0.extend(['flute', 'makeup', 'shelf'])

# Put the gloves into Box 2
box_2.append('gloves')

# Move the mixer and the camera from Box 1 to Box 8
box_8.extend(['mixer', 'camera'])
box_1.remove('mixer')
box_1.remove('camera')

# Put the perfume into Box 8
box_8.append('perfume')

# Swap the ship in Box 6 with the pan in Box 1
box_1.remove('pan')
box_6.remove('ship')
box_1.append('ship')
box_6.append('pan')

# Swap the ship in Box 1 with the sandals in Box 3
box_1.remove('ship')
box_3.remove('sandals')
box_1.append('sandals')
box_3.append('ship')

# Move the table and the sandals from Box 1 to Box 3
box_3.extend(['table', 'sandals'])
box_1.remove('table')
box_1.remove('sandals')

# Swap the console in Box 2 with the wig in Box 5
box_2.remove('console')
box_5.remove('wig')
box_2.append('wig')
box_5.append('console')

# Move the sandals from Box 3 to Box 0
box_0.append('sandals')
box_3.remove('sandals')

# Swap the wig in Box 2 with the makeup in Box 0
box_0.remove('makeup')
box_2.remove('wig')
box_0.append('wig')
box_2.append('makeup')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)