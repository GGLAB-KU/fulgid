box_0 = ['shoes']
box_1 = ['scissors', 'wig', 'bell', 'truck', 'meteor']
box_2 = ['belt', 'horn']
box_3 = ['camera', 'usb']
box_4 = ['bus']
box_5 = ['forest', 'flower', 'dice']
box_6 = ['harmonica']
box_7 = ['dress']
box_8 = ['candle', 'spoon', 'skirt', 'toothpaste', 'note']

# Remove the horn from Box 2
box_2.remove('horn')

# Replace the belt with the snow in Box 2
box_2 = ['snow']

# Put the elephant and the grinder into Box 8
box_8.extend(['elephant', 'grinder'])

# Swap the flower in Box 5 with the toothpaste in Box 8
box_5.remove('flower')
box_8.remove('toothpaste')
box_5.append('toothpaste')
box_8.append('flower')

# Replace the bus with the crown in Box 4
box_4 = ['crown']

# Replace the dress with the doll in Box 7
box_7 = ['doll']

# Put the chair and the vase into Box 4
box_4.extend(['chair', 'vase'])

# Move the harmonica from Box 6 to Box 1
box_6.remove('harmonica')
box_1.append('harmonica')

# Remove the spoon from Box 8
box_8.remove('spoon')

# Remove the grinder and the flower and the elephant from Box 8
box_8 = []

# Empty Box 2
box_2 = []

# Put the bracelet and the keyboard and the sock into Box 2
box_2.extend(['bracelet', 'keyboard', 'sock'])

# Replace the crown and the chair with the coat and the shelf in Box 4
box_4 = ['coat', 'shelf']

# Put the leaf and the grass into Box 0
box_0.extend(['leaf', 'grass'])

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