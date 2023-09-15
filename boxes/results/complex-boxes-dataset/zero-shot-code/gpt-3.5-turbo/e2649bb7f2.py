box_0 = ['bicycle', 'book', 'star', 'pants', 'motorcycle']
box_1 = ['freezer', 'belt', 'bracelet', 'thunder', 'thread']
box_2 = ['candle', 'tiger', 'mask', 'bowl']
box_3 = ['wallet', 'coat', 'spoon', 'toaster', 'earring']
box_4 = ['microwave', 'drum', 'ocean']
box_5 = ['umbrella', 'boot', 'sun', 'pot']
box_6 = ['moon']
box_7 = ['jacket']
box_8 = ['rain']
box_9 = ['plate', 'microscope']
box_10 = ['butterfly', 'octopus']

# Swap the pot in Box 5 with the drum in Box 4
box_5[box_5.index('pot')], box_4[box_4.index('drum')] = box_4[box_4.index('drum')], box_5[box_5.index('pot')]

# Remove the toaster from Box 3
box_3.remove('toaster')

# Swap the umbrella in Box 5 with the belt in Box 1
box_5[box_5.index('umbrella')], box_1[box_1.index('belt')] = box_1[box_1.index('belt')], box_5[box_5.index('umbrella')]

# Move the bicycle and the motorcycle from Box 0 to Box 5
box_5.extend([box_0.pop(box_0.index('bicycle')), box_0.pop(box_0.index('motorcycle'))])

# Put the book into Box 9
box_9.append(box_0.pop(box_0.index('book')))

# Move the star from Box 0 to Box 2
box_2.append(box_0.pop(box_0.index('star')))

# Replace the book and the pants with the rocket and the key in Box 0
box_0 = ['rocket', 'key']

# Put the train and the sock into Box 3
box_3.extend(['train', 'sock'])

# Remove the butterfly and the octopus from Box 10
box_10.remove('butterfly')
box_10.remove('octopus')

# Replace the rain with the pot in Box 8
box_8 = ['pot']

# Remove the rocket from Box 0
box_0 = []

# Swap the microscope in Box 9 with the wallet in Box 3
box_9[box_9.index('microscope')], box_3[box_3.index('wallet')] = box_3[box_3.index('wallet')], box_9[box_9.index('microscope')]

# Empty Box 6
box_6 = []

# Remove the bicycle and the boot and the belt from Box 5
box_5.remove('bicycle')
box_5.remove('boot')
box_5.remove('belt')

# Remove the jacket from Box 7
box_7 = []

# Remove the key from Box 0
box_0 = []

# Replace the pot with the meteor in Box 4
box_4[box_4.index('pot')] = 'meteor'

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