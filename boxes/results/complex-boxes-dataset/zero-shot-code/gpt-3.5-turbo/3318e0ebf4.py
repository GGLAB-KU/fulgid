box_0 = []
box_1 = ['usb', 'blender', 'ring']
box_2 = ['coin', 'meteor', 'grinder']
box_3 = ['pot', 'cup']
box_4 = []
box_5 = ['desert']
box_6 = []

# Remove the ring, usb, and blender from Box 1
box_1.remove('ring')
box_1.remove('usb')
box_1.remove('blender')

# Replace the razor with the desert in Box 5
box_5.remove('desert')
box_5.append('razor')

# Put the spoon and the butterfly into Box 0
box_0.append('spoon')
box_0.append('butterfly')

# Swap the butterfly in Box 0 with the coin in Box 2
box_0.remove('butterfly')
box_2.remove('coin')
box_0.append('coin')
box_2.append('butterfly')

# Move the pot and the cup from Box 3 to Box 0
box_0.append('pot')
box_0.append('cup')
box_3.remove('pot')
box_3.remove('cup')

# Move the coin and the spoon from Box 0 to Box 4
box_4.append('coin')
box_4.append('spoon')
box_0.remove('coin')
box_0.remove('spoon')

# Put the table into Box 2
box_2.append('table')

# Put the microscope and the boat into Box 2
box_2.append('microscope')
box_2.append('boat')

# Swap the microscope in Box 2 with the pot in Box 0
box_2.remove('microscope')
box_0.remove('pot')
box_2.append('pot')
box_0.append('microscope')

# Move the microscope and the cup from Box 0 to Box 3
box_3.append('microscope')
box_3.append('cup')
box_0.remove('microscope')
box_0.remove('cup')

# Put the mirror, moon, and earring into Box 6
box_6.append('mirror')
box_6.append('moon')
box_6.append('earring')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)