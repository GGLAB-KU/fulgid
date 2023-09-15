box_0 = []
box_1 = []
box_2 = ['shirt', 'toothbrush']
box_3 = ['motorcycle', 'grinder', 'leaf', 'blanket']
box_4 = []
box_5 = ['pan', 'microscope', 'usb']
box_6 = []
box_7 = []

# Remove the shirt from Box 2
box_2.remove('shirt')

# Remove the microscope and the pan and the usb from Box 5
box_5.remove('microscope')
box_5.remove('pan')
box_5.remove('usb')

# Move the toothbrush from Box 2 to Box 6
box_6.append(box_2.pop(box_2.index('toothbrush')))

# Put the phone and the jungle into Box 4
box_4.extend(['phone', 'jungle'])

# Replace the jungle and the phone with the battery and the flute in Box 4
box_4.remove('jungle')
box_4.remove('phone')
box_4.extend(['battery', 'flute'])

# Put the scissors and the freezer into Box 5
box_5.extend(['scissors', 'freezer'])

# Replace the grinder and the leaf with the flower and the meteor in Box 3
box_3.remove('grinder')
box_3.remove('leaf')
box_3.extend(['flower', 'meteor'])

# Remove the blanket and the flower from Box 3
box_3.remove('blanket')
box_3.remove('flower')

# Swap the freezer in Box 5 with the meteor in Box 3
box_5.remove('freezer')
box_5.append('meteor')
box_3.remove('meteor')
box_3.append('freezer')

# Move the motorcycle from Box 3 to Box 2
box_2.append(box_3.pop(box_3.index('motorcycle')))

# Replace the freezer with the leaf in Box 3
box_3.remove('freezer')
box_3.append('leaf')

# Move the battery from Box 4 to Box 3
box_3.append(box_4.pop(box_4.index('battery')))

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)