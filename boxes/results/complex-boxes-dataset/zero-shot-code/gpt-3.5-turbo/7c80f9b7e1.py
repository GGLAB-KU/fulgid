box_0 = ['mountain', 'elephant']
box_1 = ['swimsuit', 'microwave', 'lipstick', 'tree']
box_2 = ['river', 'microscope']
box_3 = ['dress', 'lion', 'clock']
box_4 = []
box_5 = ['table', 'umbrella', 'headphone', 'console']
box_6 = []

# Remove the headphone from Box 5
box_5.remove('headphone')

# Move the clock and the lion and the dress from Box 3 to Box 2
box_2.extend(box_3)
box_3.clear()

# Remove the mountain and the elephant from Box 0
box_0.clear()

# Replace the tree and the swimsuit and the microwave with the shelf and the shoe and the puzzle in Box 1
box_1 = ['shelf', 'shoe', 'puzzle']

# Remove the console from Box 5
box_5.remove('console')

# Replace the dress and the microscope with the ocean and the desert in Box 2
box_2 = ['ocean', 'desert']

# Swap the lion in Box 2 with the shoe in Box 1
box_1[box_1.index('shoe')], box_2[box_2.index('lion')] = box_2[box_2.index('lion')], box_1[box_1.index('shoe')]

# Put the controller and the polish and the tie into Box 4
box_4.extend(['controller', 'polish', 'tie'])

# Put the book and the microscope and the mask into Box 0
box_0.extend(['book', 'microscope', 'mask'])

# Remove the controller from Box 4
box_4.remove('controller')

# Replace the book and the microscope with the river and the dog in Box 0
box_0 = ['river', 'dog']

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)