box_0 = ['bear', 'fish', 'belt', 'card']
box_1 = []
box_2 = ['usb', 'plate', 'glasses', 'hat']
box_3 = ['guitar']
box_4 = []
box_5 = []

# Replace the belt with the shoes in Box 0
box_0.remove('belt')
box_0.append('shoes')

# Put the battery and the umbrella into Box 4
box_4.extend(['battery', 'umbrella'])

# Empty Box 0
box_0.clear()

# Put the lion and the mirror and the planet into Box 0
box_0.extend(['lion', 'mirror', 'planet'])

# Swap the guitar in Box 3 with the usb in Box 2
box_2.remove('usb')
box_3.remove('guitar')
box_2.append('guitar')
box_3.append('usb')

# Swap the usb in Box 3 with the battery in Box 4
box_3.remove('usb')
box_4.remove('battery')
box_3.append('battery')
box_4.append('usb')

# Put the jungle into Box 2
box_2.append('jungle')

# Empty Box 2
box_2.clear()

# Remove the lion and the mirror and the planet from Box 0
box_0.remove('lion')
box_0.remove('mirror')
box_0.remove('planet')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)