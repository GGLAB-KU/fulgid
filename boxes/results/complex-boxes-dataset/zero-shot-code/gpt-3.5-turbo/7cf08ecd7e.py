box_0 = ['motorcycle']
box_1 = ['fish', 'thread', 'mirror']
box_2 = ['phone', 'towel', 'shorts', 'fridge']
box_3 = []
box_4 = ['blanket']
box_5 = ['apple', 'note']
box_6 = ['violin', 'bag', 'horn']

# Replace items in Box 6
box_6 = ['starfish', 'speaker', 'wig']

# Swap items in Box 0 and Box 4
box_0, box_4 = box_4, box_0

# Empty Box 2
box_2 = []

# Swap items in Box 1 and Box 5
box_1, box_5 = box_5, box_1

# Put the coat into Box 1
box_1.append('coat')

# Move the motorcycle from Box 4 to Box 2
box_2.append(box_4.pop(0))

# Replace items in Box 1
box_1 = ['gloves', 'flower', 'magnet']

# Replace the blanket with the horse in Box 0
box_0 = ['horse']

# Move the flower and the magnet from Box 1 to Box 3
box_3.extend(box_1[1:])

# Put the ocean and the cloud into Box 2
box_2.extend(['ocean', 'cloud'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)