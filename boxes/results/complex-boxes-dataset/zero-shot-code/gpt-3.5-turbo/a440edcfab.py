box_0 = ['helmet']
box_1 = ['umbrella', 'fridge']
box_2 = ['cup', 'skirt', 'keyboard', 'usb', 'cow']
box_3 = ['motorcycle']
box_4 = ['pan']

# Remove the umbrella and the fridge from Box 1
box_1.remove('umbrella')
box_1.remove('fridge')

# Remove the helmet from Box 0
box_0.remove('helmet')

# Empty Box 4
box_4 = []

# Replace the keyboard with the skirt in Box 2
box_2.remove('keyboard')
box_2.append('skirt')

# Put the shirt into Box 3
box_3.append('shirt')

# Remove the skirt from Box 2
box_2.remove('skirt')

# Swap the usb in Box 2 with the motorcycle in Box 3
box_2.remove('usb')
box_3.remove('motorcycle')
box_2.append('motorcycle')
box_3.append('usb')

# Replace the cup and the skirt and the cow with the forest and the necklace and the lipstick in Box 2
box_2.remove('cup')
box_2.remove('skirt')
box_2.remove('cow')
box_2.extend(['forest', 'necklace', 'lipstick'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)