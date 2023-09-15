box_0 = ['octopus', 'coat']
box_1 = ['chair', 'horse']
box_2 = ['river', 'mountain', 'rock']
box_3 = ['blanket']
box_4 = ['dice', 'umbrella', 'cloud', 'toothbrush', 'console']
box_5 = []
box_6 = ['toothpaste', 'controller', 'leaf', 'book', 'button']
box_7 = ['spoon', 'bell']
box_8 = ['mixer']
box_9 = ['piano', 'ship', 'dog']
box_10 = ['note', 'island', 'hat']
box_11 = ['headphone']
box_12 = ['shorts', 'shirt']
box_13 = ['freezer']
box_14 = ['cat']

# Put the hat and the phone into Box 10
box_10.extend(['hat', 'phone'])

# Put the meteor and the usb into Box 9
box_9.extend(['meteor', 'usb'])

# Replace the bell and the spoon with the beach and the submarine in Box 7
box_7 = ['beach', 'submarine']

# Swap the blanket in Box 3 with the horse in Box 1
box_3, box_1 = box_1, box_3

# Swap the hat in Box 10 with the blanket in Box 1
box_10, box_1 = box_1, box_10

# Remove the shorts and the shirt from Box 12
box_12 = []

# Move the freezer from Box 13 to Box 12
box_12.append('freezer')
box_13.remove('freezer')

# Replace the controller and the leaf with the pan and the pot in Box 6
box_6 = ['pan', 'pot']

# Replace the headphone with the blender in Box 11
box_11 = ['blender']

# Move the cat from Box 14 to Box 11
box_11.append('cat')
box_14.remove('cat')

# Swap the hat in Box 1 with the shoe in Box 10
box_1, box_10 = box_10, box_1

# Put the grinder into Box 8
box_8.append('grinder')

# Move the freezer from Box 12 to Box 10
box_10.append('freezer')
box_12.remove('freezer')

# Move the usb and the ship and the piano from Box 9 to Box 10
box_10.extend(['usb', 'ship', 'piano'])
box_9 = []

# Remove the submarine and the beach from Box 7
box_7 = []

# Replace the cat with the rock in Box 11
box_11 = ['rock']

# Empty Box 6
box_6 = []

# Move the note from Box 10 to Box 1
box_1.append('note')
box_10.remove('note')

# Replace the horse with the bowl in Box 3
box_3 = ['bowl']

# Swap the meteor in Box 9 with the bowl in Box 3
box_9, box_3 = box_3, box_9

# Remove the coat and the octopus from Box 0
box_0 = []

# Remove the dice and the cloud and the toothbrush from Box 4
box_4 = []

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
print("Box 13:", box_13)
print("Box 14:", box_14)