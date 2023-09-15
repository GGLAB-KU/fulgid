box_0 = ['octopus', 'oven']
box_1 = ['game', 'polish']
box_2 = ['forest', 'seaweed']
box_3 = ['branch']

# Remove the polish from Box 1
box_1.remove('polish')

# Swap the octopus in Box 0 with the forest in Box 2
box_0[0], box_2[0] = box_2[0], box_0[0]

# Replace the game with the motorcycle in Box 1
box_1[0] = 'motorcycle'

# Move the branch from Box 3 to Box 1
box_1.append(box_3.pop())

# Put the microwave and the game into Box 0
box_0.extend(['microwave', 'game'])

# Empty Box 2
box_2 = []

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)