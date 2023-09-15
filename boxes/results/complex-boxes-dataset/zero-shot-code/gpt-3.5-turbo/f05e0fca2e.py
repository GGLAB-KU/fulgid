box_0 = []
box_1 = ['hat']
box_2 = []
box_3 = ['bus', 'snow', 'bear', 'ship']
box_4 = ['book', 'thunder', 'cup']
box_5 = ['makeup', 'violin', 'console', 'wallet']
box_6 = ['planet', 'helmet']
box_7 = ['usb', 'note', 'shark', 'freezer']
box_8 = ['leaf', 'star', 'plane', 'ocean']
box_9 = ['seaweed', 'mountain', 'needle', 'dolphin', 'lipstick']
box_10 = ['island', 'magnet']

# Swap the hat in Box 1 with the helmet in Box 6
box_1, box_6 = box_6, box_1

# Move the bus from Box 3 to Box 4
box_4.append(box_3.pop(box_3.index('bus')))

# Put the card into Box 4
box_4.append('card')

# Put the doll into Box 2
box_2.append('doll')

# Replace the bear and the snow and the ship with the skirt and the perfume and the shelf in Box 3
box_3 = ['skirt', 'perfume', 'shelf']

# Replace the plane and the ocean with the mask and the boot in Box 8
box_8 = ['mask', 'boot']

# Remove the doll from Box 2
box_2 = []

# Swap the planet in Box 6 with the seaweed in Box 9
box_6, box_9 = box_9, box_6

# Remove the thunder from Box 4
box_4.remove('thunder')

# Swap the note in Box 7 with the mask in Box 8
box_7[box_7.index('note')], box_8[box_8.index('mask')] = box_8[box_8.index('mask')], box_7[box_7.index('note')]

# Move the star from Box 8 to Box 9
box_9.append(box_8.pop(box_8.index('star')))

# Swap the bus in Box 4 with the seaweed in Box 6
box_4[box_4.index('bus')], box_6[box_6.index('seaweed')] = box_6[box_6.index('seaweed')], box_4[box_4.index('bus')]

# Remove the makeup and the console and the violin from Box 5
box_5 = []

# Remove the magnet and the island from Box 10
box_10 = []

# Swap the helmet in Box 1 with the book in Box 4
box_1, box_4 = box_4, box_1

# Move the boot and the leaf from Box 8 to Box 5
box_5.extend([box_8.pop(box_8.index('boot')), box_8.pop(box_8.index('leaf'))])

# Remove the dolphin and the planet from Box 9
box_9.remove('dolphin')
box_9.remove('planet')

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
print("Box 10:", box_10)