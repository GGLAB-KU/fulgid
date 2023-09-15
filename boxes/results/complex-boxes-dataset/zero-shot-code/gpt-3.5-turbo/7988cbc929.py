box_0 = ['storm']
box_1 = ['cloud']
box_2 = []
box_3 = ['moon']
box_4 = ['mask', 'lightning']
box_5 = ['helmet', 'fish', 'pants', 'desert', 'rain']
box_6 = ['shirt', 'beach', 'perfume', 'clock', 'tape']
box_7 = ['plane', 'microscope', 'magnet']
box_8 = ['usb']
box_9 = ['train', 'towel', 'mountain', 'brush']

# Move the lightning and the mask from Box 4 to Box 3
box_3.extend(box_4)
box_4.clear()

# Replace the usb with the table in Box 8
box_8 = ['table']

# Replace the cloud with the rock in Box 1
box_1 = ['rock']

# Remove the storm from Box 0
box_0.clear()

# Empty Box 9
box_9.clear()

# Move the plane and the magnet from Box 7 to Box 6
box_6.extend(box_7)
box_7.clear()

# Remove the table from Box 8
box_8.clear()

# Replace the rock with the table in Box 1
box_1 = ['table']

# Replace the desert and the helmet and the pants with the flute and the jacket and the fork in Box 5
box_5 = ['flute', 'jacket', 'fork']

# Put the shark and the bell into Box 5
box_5.extend(['shark', 'bell'])

# Remove the tape from Box 6
box_6.remove('tape')

# Remove the lightning from Box 3
box_3.remove('lightning')

# Replace the microscope with the controller in Box 7
box_7 = ['controller']

# Put the grass and the pot into Box 6
box_6.extend(['grass', 'pot'])

# Remove the controller from Box 7
box_7.clear()

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
print("Box 9:", box_9)