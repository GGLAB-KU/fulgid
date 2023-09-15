box_0 = ['ring', 'shoe']
box_1 = ['tape']
box_2 = []
box_3 = []
box_4 = ['pot', 'submarine', 'rock', 'laptop']
box_5 = ['wig', 'usb', 'bus', 'toothpaste']
box_6 = []
box_7 = ['skirt', 'cat', 'razor', 'freezer', 'mirror']
box_8 = ['hat', 'telescope', 'sock', 'bird', 'speaker']

# Replace the submarine and the pot with the harmonica and the horse in Box 4
box_4.remove('submarine')
box_4.remove('pot')
box_4.extend(['harmonica', 'horse'])

# Replace the tape with the seaweed in Box 1
box_1.remove('tape')
box_1.append('seaweed')

# Put the usb and the microwave into Box 0
box_0.extend(['usb', 'microwave'])

# Swap the freezer in Box 7 with the ring in Box 0
box_7.remove('freezer')
box_0.remove('ring')
box_7.append('ring')
box_0.append('freezer')

# Put the wire and the truck and the pants into Box 5
box_5.extend(['wire', 'truck', 'pants'])

# Replace the seaweed with the bell in Box 1
box_1.remove('seaweed')
box_1.append('bell')

# Remove the hat and the telescope and the speaker from Box 8
box_8.remove('hat')
box_8.remove('telescope')
box_8.remove('speaker')

# Replace the pants and the truck with the sock and the jungle in Box 5
box_5.remove('pants')
box_5.remove('truck')
box_5.extend(['sock', 'jungle'])

# Empty Box 7
box_7.clear()

# Swap the bird in Box 8 with the usb in Box 5
box_8.remove('bird')
box_5.remove('usb')
box_8.append('usb')
box_5.append('bird')

# Move the bell from Box 1 to Box 8
box_1.remove('bell')
box_8.append('bell')

# Put the ship into Box 1
box_1.append('ship')

# Put the star and the island into Box 5
box_5.extend(['star', 'island'])

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