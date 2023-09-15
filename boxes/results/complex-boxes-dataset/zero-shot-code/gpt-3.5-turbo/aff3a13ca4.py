box_0 = ['razor', 'camera']
box_1 = ['elephant', 'belt', 'moon']
box_2 = []
box_3 = ['perfume', 'ship', 'ring']
box_4 = ['gloves', 'earring', 'console']
box_5 = ['spoon']
box_6 = ['bowl', 'submarine', 'lock']
box_7 = []
box_8 = []

# Replace the gloves with the desert in Box 4
box_4.remove('gloves')
box_4.append('desert')

# Move the moon from Box 1 to Box 0
box_0.append(box_1.pop(box_1.index('moon')))

# Move the razor and the moon and the camera from Box 0 to Box 2
box_2.extend([box_0.pop(box_0.index('razor')), box_0.pop(box_0.index('moon')), box_0.pop(box_0.index('camera'))])

# Put the makeup and the magnet and the pot into Box 7
box_7.extend(['makeup', 'magnet', 'pot'])

# Move the perfume and the ship from Box 3 to Box 7
box_7.extend([box_3.pop(box_3.index('perfume')), box_3.pop(box_3.index('ship'))])

# Swap the spoon in Box 5 with the camera in Box 2
box_5.remove('spoon')
box_2.remove('camera')
box_5.append('camera')
box_2.append('spoon')

# Empty Box 4
box_4.clear()

# Replace the camera with the harmonica in Box 5
box_5.remove('camera')
box_5.append('harmonica')

# Put the planet into Box 0
box_0.append('planet')

# Move the planet from Box 0 to Box 8
box_8.append(box_0.pop(box_0.index('planet')))

# Remove the spoon and the moon and the razor from Box 2
box_2.remove('spoon')
box_2.remove('moon')
box_2.remove('razor')

# Move the planet from Box 8 to Box 4
box_4.append(box_8.pop(box_8.index('planet')))

# Replace the planet with the motorcycle in Box 4
box_4.remove('planet')
box_4.append('motorcycle')

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