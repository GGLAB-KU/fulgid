box_0 = ['tiger', 'button', 'octopus', 'mountain', 'fridge']
box_1 = ['towel', 'card', 'console', 'lion', 'bear']
box_2 = ['train', 'horn', 'wire']
box_3 = ['bag']
box_4 = ['spoon', 'basket', 'drum', 'helmet']
box_5 = ['ring', 'fish', 'forest', 'butterfly', 'bicycle']
box_6 = ['mask']
box_7 = ['island']

# Move the horn and the wire and the train from Box 2 to Box 6
box_6.extend(box_2)
box_2.clear()

# Remove the horn from Box 6
box_6.remove('horn')

# Replace the spoon and the helmet and the drum with the soap and the jacket and the bird in Box 4
box_4.remove('spoon')
box_4.remove('helmet')
box_4.remove('drum')
box_4.extend(['soap', 'jacket', 'bird'])

# Replace the wire with the shampoo in Box 6
box_6.remove('wire')
box_6.append('shampoo')

# Swap the bear in Box 1 with the bag in Box 3
box_1.remove('bear')
box_3.remove('bag')
box_1.append('bag')
box_3.append('bear')

# Swap the forest in Box 5 with the mask in Box 6
box_5.remove('forest')
box_6.remove('mask')
box_5.append('mask')
box_6.append('forest')

# Remove the island from Box 7
box_7.clear()

# Replace the bear with the cow in Box 3
box_3.remove('bear')
box_3.append('cow')

# Move the button and the octopus from Box 0 to Box 1
box_1.extend(['button', 'octopus'])
box_0.remove('button')
box_0.remove('octopus')

# Move the mountain from Box 0 to Box 1
box_1.append('mountain')
box_0.remove('mountain')

# Empty Box 0
box_0.clear()

# Replace the button and the mountain with the sock and the camera in Box 1
box_1.remove('button')
box_1.remove('mountain')
box_1.extend(['sock', 'camera'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)