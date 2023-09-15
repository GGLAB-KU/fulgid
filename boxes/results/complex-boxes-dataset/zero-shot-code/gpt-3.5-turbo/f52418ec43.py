box_0 = ['toy', 'forest', 'coat']
box_1 = ['bag', 'bicycle', 'storm', 'piano', 'cloud']
box_2 = ['toothpaste', 'lamp', 'hat', 'octopus']
box_3 = ['laptop', 'bell', 'pot']
box_4 = ['pen', 'lion', 'brush']
box_5 = ['crown', 'needle', 'watch', 'necklace']
box_6 = []
box_7 = ['bus', 'cup', 'branch']
box_8 = ['bird', 'console', 'sock', 'fish', 'telescope']
box_9 = []
box_10 = ['sculpture', 'belt', 'tree', 'speaker', 'thunder']
box_11 = ['truck', 'sun', 'plane']
box_12 = ['train', 'book']

# Replace the bird and the telescope with the tree and the microscope in Box 8
box_8.remove('bird')
box_8.remove('telescope')
box_8.append('tree')
box_8.append('microscope')

# Replace the coat and the forest and the toy with the bird and the ocean and the toothbrush in Box 0
box_0.remove('toy')
box_0.remove('forest')
box_0.remove('coat')
box_0.append('bird')
box_0.append('ocean')
box_0.append('toothbrush')

# Remove the sculpture and the speaker and the tree from Box 10
box_10.remove('sculpture')
box_10.remove('speaker')
box_10.remove('tree')

# Put the ring and the towel and the game into Box 0
box_0.append('ring')
box_0.append('towel')
box_0.append('game')

# Move the pen and the lion and the brush from Box 4 to Box 7
box_4.remove('pen')
box_4.remove('lion')
box_4.remove('brush')
box_7.append('pen')
box_7.append('lion')
box_7.append('brush')

# Move the toothpaste and the hat from Box 2 to Box 8
box_2.remove('toothpaste')
box_2.remove('hat')
box_8.append('toothpaste')
box_8.append('hat')

# Swap the book in Box 12 with the ocean in Box 0
box_12.remove('book')
box_0.remove('ocean')
box_12.append('ocean')
box_0.append('book')

# Move the thunder and the belt from Box 10 to Box 9
box_10.remove('thunder')
box_10.remove('belt')
box_9.append('thunder')
box_9.append('belt')

# Move the lamp and the octopus from Box 2 to Box 7
box_2.remove('lamp')
box_2.remove('octopus')
box_7.append('lamp')
box_7.append('octopus')

# Move the sun and the plane from Box 11 to Box 9
box_11.remove('sun')
box_11.remove('plane')
box_9.append('sun')
box_9.append('plane')

# Replace the bicycle with the camera in Box 1
box_1.remove('bicycle')
box_1.append('camera')

# Put the flute into Box 4
box_4.append('flute')

# Remove the toothpaste and the microscope from Box 8
box_8.remove('toothpaste')
box_8.remove('microscope')

# Move the storm and the piano and the bag from Box 1 to Box 5
box_1.remove('storm')
box_1.remove('piano')
box_1.remove('bag')
box_5.append('storm')
box_5.append('piano')
box_5.append('bag')

# Remove the toothbrush and the book from Box 0
box_0.remove('toothbrush')
box_0.remove('book')

# Move the flute from Box 4 to Box 11
box_4.remove('flute')
box_11.append('flute')

# Move the towel from Box 0 to Box 2
box_0.remove('towel')
box_2.append('towel')

# Move the bag and the piano and the watch from Box 5 to Box 3
box_5.remove('bag')
box_5.remove('piano')
box_5.remove('watch')
box_3.append('bag')
box_3.append('piano')
box_3.append('watch')

# Replace the pot and the bag and the piano with the seaweed and the fish and the toaster in Box 3
box_3.remove('pot')
box_3.remove('bag')
box_3.remove('piano')
box_3.append('seaweed')
box_3.append('fish')
box_3.append('toaster')

# Remove the bus and the lion from Box 7
box_7.remove('bus')
box_7.remove('lion')

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
print("Box 10:", box_10)
print("Box 11:", box_11)
print("Box 12:", box_12)