box_0 = ['scissors', 'sock', 'motorcycle', 'submarine', 'snow']
box_1 = ['seaweed', 'wig', 'swimsuit', 'makeup', 'coat']
box_2 = ['speaker', 'keyboard', 'blanket']
box_3 = ['shoe', 'shelf']
box_4 = ['island', 'toaster']
box_5 = ['river']
box_6 = ['storm', 'lightning', 'desert', 'needle', 'rocket']
box_7 = ['sandals']
box_8 = ['leaf', 'telescope']
box_9 = ['horse', 'grinder', 'toy', 'note', 'soap']
box_10 = []

def print_box(box_index, box_items):
    if len(box_items) == 0:
        print(f"Box {box_index}: []")
    else:
        print(f"Box {box_index}: {box_items}")

# Initial state
print_box(0, box_0)
print_box(1, box_1)
print_box(2, box_2)
print_box(3, box_3)
print_box(4, box_4)
print_box(5, box_5)
print_box(6, box_6)
print_box(7, box_7)
print_box(8, box_8)
print_box(9, box_9)
print_box(10, box_10)

# Put the battery and the charger and the cup into Box 9
box_9.extend(['battery', 'charger', 'cup'])
print_box(9, box_9)

# Swap the shelf in Box 3 with the blanket in Box 2
box_3[1], box_2[2] = box_2[2], box_3[1]
print_box(2, box_2)
print_box(3, box_3)

# Swap the river in Box 5 with the swimsuit in Box 1
box_5[0], box_1[2] = box_1[2], box_5[0]
print_box(1, box_1)
print_box(5, box_5)

# Swap the cup in Box 9 with the keyboard in Box 2
box_9[2], box_2[1] = box_2[1], box_9[2]
print_box(2, box_2)
print_box(9, box_9)

# Replace the speaker with the dolphin in Box 2
box_2[0] = 'dolphin'
print_box(2, box_2)

# Remove the storm and the rocket and the desert from Box 6
box_6.remove('storm')
box_6.remove('rocket')
box_6.remove('desert')
print_box(6, box_6)

# Empty Box 5
box_5.clear()
print_box(5, box_5)

# Remove the dolphin and the shelf from Box 2
box_2.remove('dolphin')
box_2.remove('shelf')
print_box(2, box_2)

# Put the microscope and the watch and the planet into Box 3
box_3.extend(['microscope', 'watch', 'planet'])
print_box(3, box_3)

# Move the blanket and the watch from Box 3 to Box 0
box_0.extend([box_3.pop(2), box_3.pop(1)])
print_box(0, box_0)
print_box(3, box_3)

# Put the ocean and the bowl into Box 8
box_8.extend(['ocean', 'bowl'])
print_box(8, box_8)

# Swap the lightning in Box 6 with the island in Box 4
box_6[1], box_4[0] = box_4[0], box_6[1]
print_box(4, box_4)
print_box(6, box_6)

# Put the hat and the mask and the island into Box 3
box_3.extend(['hat', 'mask', box_4.pop(0)])
print_box(3, box_3)
print_box(4, box_4)

# Move the island from Box 6 to Box 7
box_7.append(box_6.pop(1))
print_box(6, box_6)
print_box(7, box_7)

# Replace the snow and the sock with the pants and the book in Box 0
box_0[1] = 'pants'
box_0[4] = 'book'
print_box(0, box_0)

# Swap the keyboard in Box 9 with the toaster in Box 4
box_9[1], box_4[1] = box_4[1], box_9[1]
print_box(4, box_4)
print_box(9, box_9)