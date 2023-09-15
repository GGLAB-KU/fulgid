box_0 = ['planet', 'controller', 'lion', 'coin']
box_1 = ['laptop', 'bell']
box_2 = ['bear', 'boot']
box_3 = ['island', 'tie', 'beach', 'hat']
box_4 = ['comet', 'microscope', 'seaweed', 'cat']
box_5 = ['butterfly']
box_6 = ['toaster']
box_7 = ['flower', 'star', 'console', 'apple', 'telescope']
box_8 = ['train', 'tape', 'mirror', 'drum']
box_9 = ['bicycle', 'meteor', 'submarine', 'puzzle']
box_10 = ['belt']

# Move the butterfly from Box 5 to Box 8
box_8.append(box_5.pop(0))

# Replace the toaster with the comb in Box 6
box_6[0] = 'comb'

# Replace the console with the bird in Box 7
box_7[2] = 'bird'

# Swap the belt in Box 10 with the bell in Box 1
box_1[0], box_10[0] = box_10[0], box_1[0]

# Replace the tie and the island and the hat with the starfish and the mountain and the bus in Box 3
box_3 = ['starfish', 'mountain', 'bus']

# Put the wig and the dolphin and the speaker into Box 5
box_5.extend(['wig', 'dolphin', 'speaker'])

# Remove the bell from Box 10
box_10 = []

# Swap the cat in Box 4 with the controller in Box 0
box_0[1], box_4[3] = box_4[3], box_0[1]

# Move the puzzle from Box 9 to Box 4
box_4.append(box_9.pop(3))

# Move the comb from Box 6 to Box 1
box_1.append(box_6.pop(0))

# Put the spoon into Box 9
box_9.append('spoon')

# Move the laptop and the comb and the belt from Box 1 to Box 4
box_4.extend([box_1.pop(0), box_1.pop(0), box_1.pop(0)])

# Replace the star and the flower and the apple with the planet and the cow and the towel in Box 7
box_7 = ['planet', 'cow', 'towel']

# Replace the beach and the mountain and the starfish with the coin and the tree and the mask in Box 3
box_3 = ['coin', 'tree', 'mask']

# Remove the planet and the coin from Box 0
box_0 = []

# Put the seaweed and the horn into Box 6
box_6.extend(['seaweed', 'horn'])

# Replace the microscope and the puzzle with the fork and the truck in Box 4
box_4 = ['comet', 'fork', 'truck']

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