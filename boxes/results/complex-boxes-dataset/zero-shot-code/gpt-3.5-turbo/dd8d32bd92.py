box_0 = ['usb', 'tape', 'camera', 'plane']
box_1 = ['wire', 'bus']
box_2 = ['charger', 'spoon', 'shampoo', 'boat', 'butterfly']
box_3 = ['coral', 'scarf']

# Put the dolphin and the pan into Box 0
box_0.extend(['dolphin', 'pan'])

# Remove the wire from Box 1
box_1.remove('wire')

# Swap the butterfly in Box 2 with the bus in Box 1
box_2.remove('butterfly')
box_1.append('butterfly')

# Remove the butterfly from Box 1
box_1.remove('butterfly')

# Replace the pan with the oven in Box 0
box_0.remove('pan')
box_0.append('oven')

# Swap the oven in Box 0 with the scarf in Box 3
box_0.remove('oven')
box_3.remove('scarf')
box_0.append('scarf')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)