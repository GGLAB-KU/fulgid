box_0 = ['blanket', 'shirt', 'shelf']
box_1 = ['wig', 'shark', 'storm', 'card']
box_2 = ['watch']
box_3 = ['guitar', 'dolphin', 'scarf']
box_4 = ['flower']

# Put the lamp and the mountain and the clock into Box 3
box_3.extend(['lamp', 'mountain', 'clock'])

# Swap the flower in Box 4 with the clock in Box 3
box_3.remove('clock')
box_4.remove('flower')
box_3.append('flower')
box_4.append('clock')

# Move the watch from Box 2 to Box 3
box_2.remove('watch')
box_3.append('watch')

# Remove the clock from Box 4
box_4.remove('clock')

# Remove the dolphin from Box 3
box_3.remove('dolphin')

# Replace the guitar and the watch with the pillow and the plane in Box 3
box_3.remove('guitar')
box_3.remove('watch')
box_3.extend(['pillow', 'plane'])

# Remove the shirt from Box 0
box_0.remove('shirt')

# Print the final contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)