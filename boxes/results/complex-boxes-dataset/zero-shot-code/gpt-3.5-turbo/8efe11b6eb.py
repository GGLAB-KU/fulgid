box_0 = ['horn', 'lamp']
box_1 = ['usb', 'pillow']
box_2 = ['rocket', 'starfish', 'shelf', 'skirt']
box_3 = ['book', 'bag', 'bus']
box_4 = ['chair', 'planet']
box_5 = ['forest', 'glasses']
box_6 = ['cat']

# Remove the forest from Box 5
box_5.remove('forest')

# Replace the usb with the shorts in Box 1
box_1.remove('usb')
box_1.append('shorts')

# Put the wig and the laptop and the snow into Box 5
box_5.extend(['wig', 'laptop', 'snow'])

# Swap the skirt in Box 2 with the pillow in Box 1
box_2.remove('skirt')
box_1.remove('pillow')
box_2.append('pillow')
box_1.append('skirt')

# Put the butterfly into Box 3
box_3.append('butterfly')

# Move the laptop from Box 5 to Box 3
box_5.remove('laptop')
box_3.append('laptop')

# Swap the lamp in Box 0 with the laptop in Box 3
box_0.remove('lamp')
box_3.remove('laptop')
box_0.append('laptop')
box_3.append('lamp')

# Put the flower into Box 2
box_2.append('flower')

# Replace the shorts and the skirt with the gloves and the microwave in Box 1
box_1.remove('shorts')
box_1.remove('skirt')
box_1.extend(['gloves', 'microwave'])

# Move the cat from Box 6 to Box 5
box_6.remove('cat')
box_5.append('cat')

# Swap the bus in Box 3 with the planet in Box 4
box_3.remove('bus')
box_4.remove('planet')
box_3.append('planet')
box_4.append('bus')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)