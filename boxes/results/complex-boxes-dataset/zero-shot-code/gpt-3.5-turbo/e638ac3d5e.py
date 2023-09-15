box_0 = ['bracelet', 'frame', 'horse', 'blanket']
box_1 = ['note', 'coat', 'book', 'sculpture', 'wig']
box_2 = []
box_3 = []
box_4 = ['bag', 'vase', 'bus', 'motorcycle']
box_5 = []
box_6 = ['crown', 'dog']
box_7 = []
box_8 = ['sandals', 'grass', 'pen', 'boat', 'train']

# Put the rock and the coral into Box 0
box_0.extend(['rock', 'coral'])

# Replace the bag with the glove in Box 4
box_4.remove('bag')
box_4.append('glove')

# Remove the vase from Box 4
box_4.remove('vase')

# Move the coral and the bracelet and the blanket from Box 0 to Box 5
box_5.extend(['coral', 'bracelet', 'blanket'])
box_0.remove('coral')
box_0.remove('bracelet')
box_0.remove('blanket')

# Swap the dog in Box 6 with the glove in Box 4
box_6.remove('dog')
box_4.remove('glove')
box_6.append('glove')
box_4.append('dog')

# Put the dice and the motorcycle into Box 0
box_0.extend(['dice', 'motorcycle'])

# Replace the glove with the magnet in Box 6
box_6.remove('glove')
box_6.append('magnet')

# Replace the bus and the motorcycle and the dog with the truck and the toaster and the butterfly in Box 4
box_4.remove('bus')
box_4.remove('motorcycle')
box_4.remove('dog')
box_4.extend(['truck', 'toaster', 'butterfly'])

# Put the frame into Box 3
box_3.append('frame')

# Put the zipper and the magnet and the umbrella into Box 1
box_1.extend(['zipper', 'magnet', 'umbrella'])

# Put the magnet and the necklace into Box 8
box_8.extend(['magnet', 'necklace'])

# Replace the frame with the lock in Box 3
box_3.remove('frame')
box_3.append('lock')

# Put the motorcycle into Box 1
box_1.append('motorcycle')

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