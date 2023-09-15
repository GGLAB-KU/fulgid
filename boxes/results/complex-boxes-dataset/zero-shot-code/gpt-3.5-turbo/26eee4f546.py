box_0 = ['butterfly', 'tie', 'rock', 'crown', 'bicycle']
box_1 = ['zipper', 'battery', 'needle']
box_2 = ['perfume', 'bell', 'octopus']
box_3 = ['mountain', 'watch', 'shoes']
box_4 = ['guitar', 'grinder', 'speaker', 'blender']
box_5 = ['fork', 'grass', 'makeup', 'chair']
box_6 = []

# Put the beach into Box 2
box_2.append('beach')

# Replace the tie with the umbrella in Box 0
box_0[1] = 'umbrella'

# Swap the battery in Box 1 with the grass in Box 5
box_1[1], box_5[1] = box_5[1], box_1[1]

# Move the battery from Box 5 to Box 1
box_1.append(box_5.pop(1))

# Move the umbrella and the bicycle and the butterfly from Box 0 to Box 6
box_6.extend([box_0.pop(1), box_0.pop(1), box_0.pop(0)])

# Swap the blender in Box 4 with the needle in Box 1
box_4[3], box_1[2] = box_1[2], box_4[3]

# Replace the crown with the shirt in Box 0
box_0[2] = 'shirt'

# Put the guitar and the glove and the book into Box 3
box_3.extend(['guitar', 'glove', 'book'])

# Put the lion into Box 6
box_6.append('lion')

# Remove the rock and the shirt from Box 0
box_0.remove('rock')
box_0.remove('shirt')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)