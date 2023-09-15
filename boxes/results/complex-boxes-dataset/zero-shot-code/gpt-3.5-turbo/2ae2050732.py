box_0 = []
box_1 = ['harmonica', 'mountain', 'brush', 'fridge', 'shirt']
box_2 = ['telescope', 'desert']
box_3 = ['chair', 'zipper']
box_4 = ['car', 'mask', 'bell']
box_5 = ['ring', 'thread', 'bird', 'lock', 'submarine']

# Replace the car with the microwave in Box 4
box_4[0] = 'microwave'

# Replace the telescope and the desert with the microwave and the cup in Box 2
box_2 = ['microwave', 'cup']

# Remove the zipper from Box 3
box_3.remove('zipper')

# Swap the lock in Box 5 with the chair in Box 3
box_5[3], box_3[0] = box_3[0], box_5[3]

# Put the shoe into Box 5
box_5.append('shoe')

# Remove the microwave and the cup from Box 2
box_2 = []

# Move the brush and the shirt from Box 1 to Box 3
box_3.extend(['brush', 'shirt'])
box_1.remove('brush')
box_1.remove('shirt')

# Put the table into Box 4
box_4.append('table')

# Move the mountain and the fridge and the harmonica from Box 1 to Box 4
box_4.extend(['mountain', 'fridge', 'harmonica'])
box_1.remove('mountain')
box_1.remove('fridge')
box_1.remove('harmonica')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)