box_0 = []
box_1 = ['vase', 'phone', 'grinder', 'shoe']
box_2 = ['shark']
box_3 = ['lightning', 'microscope', 'sock', 'polish', 'butterfly']
box_4 = ['scissors', 'cup']
box_5 = ['bus', 'mixer', 'keyboard']
box_6 = ['shirt', 'shoes', 'paint']
box_7 = ['earring', 'branch', 'rain']
box_8 = []
box_9 = ['spoon', 'boat']

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

# Put the keyboard into Box 2
box_2.append('keyboard')

# Empty Box 5
box_5 = []

# Swap the shark in Box 2 with the branch in Box 7
box_2[0], box_7[1] = box_7[1], box_2[0]

# Swap the shark in Box 7 with the vase in Box 1
box_7[0], box_1[0] = box_1[0], box_7[0]

# Put the butterfly and the snow into Box 9
box_9.extend(['butterfly', 'snow'])

# Move the vase and the earring and the rain from Box 7 to Box 4
box_4.extend([box_7[0], box_7[2], box_7[2]])
box_7.remove(box_7[0])
box_7.remove(box_7[1])
box_7.remove(box_7[1])

# Put the puzzle and the leaf into Box 7
box_7.extend(['puzzle', 'leaf'])

# Replace the paint and the shoes with the tiger and the truck in Box 6
box_6.remove('paint')
box_6.remove('shoes')
box_6.extend(['tiger', 'truck'])

# Put the hat and the comb into Box 0
box_0.extend(['hat', 'comb'])

# Move the polish and the microscope from Box 3 to Box 8
box_8.extend([box_3[3], box_3[4]])
box_3.remove(box_3[3])
box_3.remove(box_3[3])

# Move the puzzle from Box 7 to Box 6
box_6.append(box_7[2])
box_7.remove(box_7[2])

# Remove the tiger from Box 6
box_6.remove('tiger')

# Swap the sock in Box 3 with the shirt in Box 6
box_3[2], box_6[1] = box_6[1], box_3[2]

# Swap the phone in Box 1 with the keyboard in Box 2
box_1[1], box_2[1] = box_2[1], box_1[1]

# Replace the polish with the octopus in Box 8
box_8[1] = 'octopus'

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