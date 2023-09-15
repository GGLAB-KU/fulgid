box_0 = ['bag', 'lock', 'bird', 'train', 'speaker']
box_1 = ['brush']
box_2 = ['fish', 'dice', 'beach']
box_3 = ['dog', 'key']
box_4 = ['toothbrush', 'plane', 'puzzle']

# Move the key and the dog from Box 3 to Box 0
box_0.extend(box_3)
box_3.clear()

# Replace the bag and the train with the umbrella and the hat in Box 0
box_0.remove('bag')
box_0.remove('train')
box_0.extend(['umbrella', 'hat'])

# Remove the plane from Box 4
box_4.remove('plane')

# Remove the puzzle and the toothbrush from Box 4
box_4.remove('puzzle')
box_4.remove('toothbrush')

# Remove the brush from Box 1
box_1.clear()

# Move the beach and the dice from Box 2 to Box 3
box_3.extend(box_2[2:])
box_2 = box_2[:2]

# Swap the fish in Box 2 with the dice in Box 3
box_2[0], box_3[1] = box_3[1], box_2[0]

# Move the key and the bird from Box 0 to Box 1
box_1.extend(box_0[2:])
box_0 = box_0[:2]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)