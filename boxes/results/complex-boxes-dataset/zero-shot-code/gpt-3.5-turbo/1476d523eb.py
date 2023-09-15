box_0 = ['spoon', 'octopus', 'snow', 'fork']
box_1 = ['boat', 'scissors']
box_2 = ['umbrella', 'cow']
box_3 = ['violin', 'button', 'hat']
box_4 = ['seaweed']

# Move the boat from Box 1 to Box 3
box_3.append(box_1.pop(box_1.index('boat')))

# Put the necklace and the motorcycle and the puzzle into Box 0
box_0.extend(['necklace', 'motorcycle', 'puzzle'])

# Put the elephant into Box 4
box_4.append('elephant')

# Replace the elephant with the horn in Box 4
box_4[box_4.index('elephant')] = 'horn'

# Swap the seaweed in Box 4 with the cow in Box 2
box_2[box_2.index('cow')], box_4[box_4.index('seaweed')] = box_4[box_4.index('seaweed')], box_2[box_2.index('cow')]

# Remove the horn and the cow from Box 4
box_4.remove('horn')
box_4.remove('cow')

# Move the violin from Box 3 to Box 1
box_1.append(box_3.pop(box_3.index('violin')))

# Empty Box 3
box_3 = []

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)