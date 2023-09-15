box_0 = ['dog', 'needle']
box_1 = []
box_2 = ['plate', 'wire']
box_3 = ['truck', 'microwave', 'paint']
box_4 = ['river', 'bicycle']
box_5 = ['pants', 'octopus']

# Swap the dog in Box 0 with the wire in Box 2
box_0[0], box_2[1] = box_2[1], box_0[0]

# Move the paint and the truck from Box 3 to Box 0
box_0.extend(box_3.pop(2))
box_0.extend(box_3.pop(0))

# Replace the bicycle and the river with the frame and the bird in Box 4
box_4[0], box_4[1] = 'frame', 'bird'

# Remove the plate and the dog from Box 2
box_2.remove('plate')
box_2.remove('dog')

# Swap the frame in Box 4 with the pants in Box 5
box_4[0], box_5[0] = box_5[0], box_4[0]

# Put the headphone into Box 3
box_3.append('headphone')

# Replace the octopus with the towel in Box 5
box_5[1] = 'towel'

# Move the bird and the pants from Box 4 to Box 3
box_3.extend(box_4.pop(1))
box_3.extend(box_4.pop(0))

# Replace the needle with the cup in Box 0
box_0[1] = 'cup'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)