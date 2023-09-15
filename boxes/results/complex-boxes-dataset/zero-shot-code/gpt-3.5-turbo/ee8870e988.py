box_0 = []
box_1 = ['usb', 'doll']
box_2 = ['pan']
box_3 = ['shark', 'toy']
box_4 = ['sandals']
box_5 = []

# Swap the pan in Box 2 with the shark in Box 3
box_2, box_3 = box_3, box_2

# Replace the doll with the shorts in Box 1
box_1.remove('doll')
box_1.append('shorts')

# Remove the usb from Box 1
box_1.remove('usb')

# Swap the toy in Box 3 with the sandals in Box 4
box_3, box_4 = box_4, box_3

# Remove the shorts from Box 1
box_1.remove('shorts')

# Remove the toy from Box 4
box_4.remove('toy')

# Remove the shark from Box 2
box_2.remove('shark')

# Move the sandals from Box 3 to Box 4
box_4.extend(box_3)
box_3 = []

# Put the sock into Box 2
box_2.append('sock')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)