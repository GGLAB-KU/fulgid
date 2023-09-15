box_0 = ['microscope']
box_1 = []
box_2 = ['fork', 'car']
box_3 = ['whistle', 'watch']
box_4 = ['jacket']

# Remove the car from Box 2
box_2.remove('car')

# Replace the fork with the butterfly in Box 2
box_2.remove('fork')
box_2.append('butterfly')

# Move the jacket from Box 4 to Box 1
box_1.append(box_4.pop())

# Put the blender and the dog and the crown into Box 3
box_3.extend(['blender', 'dog', 'crown'])

# Put the rain and the thunder into Box 4
box_4.extend(['rain', 'thunder'])

# Move the jacket from Box 1 to Box 2
box_2.append(box_1.pop())

# Move the rain and the thunder from Box 4 to Box 0
box_0.extend(box_4)
box_4.clear()

# Put the flute and the skirt and the scarf into Box 4
box_4.extend(['flute', 'skirt', 'scarf'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)