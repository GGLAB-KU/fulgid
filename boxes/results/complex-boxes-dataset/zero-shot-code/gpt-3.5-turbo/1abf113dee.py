box_0 = ['ocean', 'spoon', 'rock', 'pot']
box_1 = ['ship', 'belt', 'skirt', 'boat', 'soap']
box_2 = []
box_3 = ['dolphin', 'watch', 'button']
box_4 = []
box_5 = ['thunder', 'shampoo', 'rain', 'wire', 'crown']
box_6 = ['moon', 'card', 'tape']
box_7 = []
box_8 = ['horse', 'coral', 'cloud', 'laptop']
box_9 = ['cup', 'leaf', 'basket', 'camera']
box_10 = ['charger', 'piano']

# Swap the cloud in Box 8 with the rock in Box 0
box_0[box_0.index('rock')], box_8[box_8.index('cloud')] = box_8[box_8.index('cloud')], box_0[box_0.index('rock')]

# Swap the tape in Box 6 with the piano in Box 10
box_6[box_6.index('tape')], box_10[box_10.index('piano')] = box_10[box_10.index('piano')], box_6[box_6.index('tape')]

# Put the clock and the puzzle into Box 7
box_7.extend(['clock', 'puzzle'])

# Move the clock from Box 7 to Box 10
box_10.append(box_7.pop(box_7.index('clock')))

# Swap the spoon in Box 0 with the puzzle in Box 7
box_0[box_0.index('spoon')], box_7[box_7.index('puzzle')] = box_7[box_7.index('puzzle')], box_0[box_0.index('spoon')]

# Move the thunder from Box 5 to Box 7
box_7.append(box_5.pop(box_5.index('thunder')))

# Swap the card in Box 6 with the spoon in Box 7
box_6[box_6.index('card')], box_7[box_7.index('spoon')] = box_7[box_7.index('spoon')], box_6[box_6.index('card')]

# Move the horse from Box 8 to Box 2
box_2.append(box_8.pop(box_8.index('horse')))

# Swap the card in Box 7 with the horse in Box 2
box_7[box_7.index('card')], box_2[box_2.index('horse')] = box_2[box_2.index('horse')], box_7[box_7.index('card')]

# Remove the spoon and the piano from Box 6
box_6.remove('spoon')
box_6.remove('piano')

# Move the cup and the camera and the basket from Box 9 to Box 1
box_1.extend([box_9.pop(box_9.index('cup')), box_9.pop(box_9.index('camera')), box_9.pop(box_9.index('basket'))])

# Put the bag and the wire and the phone into Box 6
box_6.extend(['bag', 'wire', 'phone'])

# Replace the ocean and the pot and the puzzle with the microwave and the forest and the mirror in Box 0
box_0 = ['microwave', 'forest', 'mirror']

# Replace the dolphin and the watch with the cow and the bicycle in Box 3
box_3 = ['cow', 'bicycle']

# Replace the soap and the camera and the boat with the glasses and the thunder and the apple in Box 1
box_1 = ['glasses', 'thunder', 'apple']

# Move the charger and the tape from Box 10 to Box 7
box_7.extend([box_10.pop(box_10.index('charger')), box_10.pop(box_10.index('tape'))])

# Empty Box 5
box_5 = []

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