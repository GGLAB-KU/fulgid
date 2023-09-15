box_0 = ['dog', 'fish', 'shelf']
box_1 = ['shark', 'branch', 'sun']
box_2 = ['truck', 'piano', 'chair']
box_3 = []
box_4 = ['bowl']
box_5 = ['island', 'storm', 'basket', 'mirror']
box_6 = ['dice', 'spoon', 'sock']
box_7 = []
box_8 = ['polish']
box_9 = []

# Swap the sock in Box 6 with the piano in Box 2
box_2.remove('piano')
box_6.remove('sock')
box_2.append('sock')
box_6.append('piano')

# Replace the polish with the frame in Box 8
box_8.remove('polish')
box_8.append('frame')

# Replace the bowl with the fork in Box 4
box_4.remove('bowl')
box_4.append('fork')

# Move the sock and the truck from Box 2 to Box 6
box_2.remove('sock')
box_2.remove('truck')
box_6.append('sock')
box_6.append('truck')

# Put the lightning and the coral into Box 6
box_6.append('lightning')
box_6.append('coral')

# Put the cat into Box 4
box_4.append('cat')

# Remove the fish and the shelf from Box 0
box_0.remove('fish')
box_0.remove('shelf')

# Remove the truck and the sock from Box 6
box_6.remove('truck')
box_6.remove('sock')

# Remove the storm and the mirror from Box 5
box_5.remove('storm')
box_5.remove('mirror')

# Replace the dog with the sun in Box 0
box_0.remove('dog')
box_0.append('sun')

# Remove the sun and the shark from Box 1
box_1.remove('sun')
box_1.remove('shark')

# Move the frame from Box 8 to Box 6
box_8.remove('frame')
box_6.append('frame')

# Replace the sun with the umbrella in Box 0
box_0.remove('sun')
box_0.append('umbrella')

# Remove the fork from Box 4
box_4.remove('fork')

# Move the umbrella from Box 0 to Box 3
box_0.remove('umbrella')
box_3.append('umbrella')

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
print("Box 9:", box_9)