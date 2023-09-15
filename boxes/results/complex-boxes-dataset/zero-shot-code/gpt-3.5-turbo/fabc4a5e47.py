box_0 = []
box_1 = ['mixer', 'coin']
box_2 = ['grinder', 'game']
box_3 = ['thunder', 'lion']
box_4 = ['polish']
box_5 = ['shoe', 'pants', 'blender', 'clock', 'bell']
box_6 = ['dolphin', 'rain', 'fridge', 'piano', 'toothpaste']
box_7 = ['dog', 'mirror', 'spoon', 'sandals', 'bear']
box_8 = []
box_9 = ['microwave']

# Put the toaster and the butterfly into Box 5
box_5.extend(['toaster', 'butterfly'])

# Put the car into Box 4
box_4.append('car')

# Move the clock and the butterfly and the bell from Box 5 to Box 6
box_6.extend([box_5.pop(box_5.index('clock')), box_5.pop(box_5.index('butterfly')), box_5.pop(box_5.index('bell'))])

# Move the fridge from Box 6 to Box 8
box_8.append(box_6.pop(box_6.index('fridge')))

# Empty Box 2
box_2 = []

# Replace the polish with the drum in Box 4
box_4[box_4.index('polish')] = 'drum'

# Remove the toaster and the shoe from Box 5
box_5.remove('toaster')
box_5.remove('shoe')

# Replace the microwave with the shampoo in Box 9
box_9[box_9.index('microwave')] = 'shampoo'

# Put the shoe and the pen and the submarine into Box 8
box_8.extend(['shoe', 'pen', 'submarine'])

# Replace the car with the hat in Box 4
box_4[box_4.index('car')] = 'hat'

# Replace the hat and the drum with the moon and the beach in Box 4
box_4.extend(['moon', 'beach'])
box_4.remove('hat')
box_4.remove('drum')

# Replace the bear with the puzzle in Box 7
box_7[box_7.index('bear')] = 'puzzle'

# Move the lion from Box 3 to Box 8
box_8.append(box_3.pop(box_3.index('lion')))

# Move the lion from Box 8 to Box 5
box_5.append(box_8.pop(box_8.index('lion')))

# Remove the shampoo from Box 9
box_9.remove('shampoo')

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