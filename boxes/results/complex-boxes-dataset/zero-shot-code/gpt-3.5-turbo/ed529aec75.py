box_0 = ['telescope', 'forest', 'planet', 'moon', 'crown']
box_1 = ['headphone', 'star', 'card']
box_2 = []
box_3 = ['tie', 'pillow']
box_4 = ['butterfly', 'belt', 'snow', 'coral']

# Move the headphone and the star from Box 1 to Box 3
box_3.extend(box_1[0:2])
box_1 = box_1[2:]

# Remove the butterfly from Box 4 and empty Box 4
box_4.remove('butterfly')
box_4 = []

# Swap the forest in Box 0 with the pillow in Box 3
box_0[1], box_3[1] = box_3[1], box_0[1]

# Replace the planet and the telescope with the doll and the bag in Box 0
box_0[2:4] = ['doll', 'bag']

# Remove the bag from Box 0
box_0.remove('bag')

# Remove the headphone from Box 3
box_3.remove('headphone')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)