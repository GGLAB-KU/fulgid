box_0 = ['tie', 'magnet', 'plane']
box_1 = ['mixer', 'piano', 'coat', 'bus']
box_2 = ['grinder', 'glasses', 'telescope', 'mask']
box_3 = []
box_4 = ['console', 'bicycle', 'wallet']
box_5 = ['earring']
box_6 = ['brush', 'grass', 'flower', 'book', 'tape']
box_7 = ['sock', 'beach']

# Put the piano and the coat and the bus into Box 1
box_1.extend(['piano', 'coat', 'bus'])

# Remove the perfume from Box 0
box_0.remove('perfume')

# Replace the flower with the thunder in Box 6
box_6[2] = 'thunder'

# Put the cow and the toothpaste and the zipper into Box 6
box_6.extend(['cow', 'toothpaste', 'zipper'])

# Remove the earring from Box 5
box_5.remove('earring')

# Move the bicycle and the console and the wallet from Box 4 to Box 6
box_6.extend(box_4[1:])
box_4 = []

# Put the scissors and the shark and the truck into Box 0
box_0.extend(['scissors', 'shark', 'truck'])

# Move the console and the tape from Box 6 to Box 0
box_0.extend(box_6[4:])
box_6 = box_6[:4]

# Empty Box 2
box_2 = []

# Swap the sock in Box 7 with the piano in Box 1
box_1.remove('piano')
box_7.remove('sock')
box_1.append('sock')
box_7.append('piano')

# Remove the piano from Box 7
box_7.remove('piano')

# Replace the tape with the dice in Box 0
box_0[3] = 'dice'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)