box0 = ['bus']
box1 = ['train', 'polish', 'tiger', 'table', 'toothpaste']
box2 = ['bowl', 'microscope', 'game', 'wallet']
box3 = ['dolphin', 'shelf', 'thread', 'toothbrush']
box4 = []

# Swap the bus in Box 0 with the microscope in Box 2
box0[0], box2[1] = box2[1], box0[0]

# Move the microscope from Box 0 to Box 1
box1.append(box0.pop(0))

# Put the keyboard and the button into Box 2
box2.extend(['keyboard', 'button'])

# Move the thread and the dolphin from Box 3 to Box 1
box1.extend([box3.pop(2), box3.pop(1)])

# Swap the keyboard in Box 2 with the toothbrush in Box 3
box2[0], box3[2] = box3[2], box2[0]

# Move the game from Box 2 to Box 4
box4.append(box2.pop(2))

# Replace the button with the jungle in Box 2
box2[1] = 'jungle'

# Remove the microscope and the polish and the tiger from Box 1
box1.remove('microscope')
box1.remove('polish')
box1.remove('tiger')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)