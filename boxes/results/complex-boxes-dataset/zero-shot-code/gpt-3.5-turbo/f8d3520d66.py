box_0 = ['octopus', 'fridge', 'beach', 'glove']
box_1 = ['coin']
box_2 = ['camera', 'laptop', 'submarine', 'speaker', 'pen']
box_3 = []
box_4 = ['toy', 'mixer', 'desert']
box_5 = []
box_6 = ['harmonica']
box_7 = ['lion', 'plate', 'belt', 'lightning']

# Replace the desert, mixer, and toy with the cloud, microwave, and sculpture in Box 4
box_4 = ['cloud', 'microwave', 'sculpture']

# Replace the submarine, pen, and laptop with the toy, car, and lightning in Box 2
box_2 = ['toy', 'car', 'lightning']

# Remove the belt from Box 7
box_7.remove('belt')

# Move the beach and octopus from Box 0 to Box 4
box_4.extend(['beach', 'octopus'])
box_0.remove('beach')
box_0.remove('octopus')

# Replace the coin with the dress in Box 1
box_1 = ['dress']

# Swap the sculpture in Box 4 with the plate in Box 7
box_4.remove('sculpture')
box_7.remove('plate')
box_4.append('plate')
box_7.append('sculpture')

# Empty Box 2
box_2 = []

# Replace the cloud, octopus, and beach with the battery, thread, and umbrella in Box 4
box_4 = ['battery', 'thread', 'umbrella']

# Move the harmonica from Box 6 to Box 4
box_4.append('harmonica')
box_6.remove('harmonica')

# Replace the lion and lightning with the key and card in Box 7
box_7.remove('lion')
box_7.remove('lightning')
box_7.extend(['key', 'card'])

# Replace the key with the forest in Box 7
box_7.remove('key')
box_7.append('forest')

# Remove the forest, card, and sculpture from Box 7
box_7.remove('forest')
box_7.remove('card')
box_7.remove('sculpture')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)