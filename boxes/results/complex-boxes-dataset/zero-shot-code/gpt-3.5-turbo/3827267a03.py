box_0 = ['shoes', 'drum']
box_1 = ['magnet', 'oven', 'mask', 'button', 'branch']
box_2 = ['mountain', 'thread', 'tie', 'desert', 'bird']
box_3 = []
box_4 = ['toothbrush', 'umbrella', 'card', 'doll', 'moon']
box_5 = []
box_6 = ['scissors', 'controller', 'coin']
box_7 = []
box_8 = ['bicycle']

def print_boxes():
    print("Box 0:", box_0)
    print("Box 1:", box_1)
    print("Box 2:", box_2)
    print("Box 3:", box_3)
    print("Box 4:", box_4)
    print("Box 5:", box_5)
    print("Box 6:", box_6)
    print("Box 7:", box_7)
    print("Box 8:", box_8)

# Remove the coin from Box 6
box_6.remove('coin')

# Put the mask into Box 3
box_3.append('mask')

# Replace the thread and the tie with the jungle and the earring in Box 2
box_2.remove('thread')
box_2.remove('tie')
box_2.extend(['jungle', 'earring'])

# Swap the mask in Box 3 with the doll in Box 4
box_3[0], box_4[3] = box_4[3], box_3[0]

# Swap the card in Box 4 with the bicycle in Box 8
box_4[2], box_8[0] = box_8[0], box_4[2]

# Remove the branch and the magnet from Box 1
box_1.remove('branch')
box_1.remove('magnet')

# Empty Box 2
box_2.clear()

# Put the table and the skirt into Box 6
box_6.extend(['table', 'skirt'])

# Empty Box 1
box_1.clear()

# Swap the card in Box 8 with the doll in Box 3
box_8[0], box_3[0] = box_3[0], box_8[0]

# Put the dice and the wallet into Box 2
box_2.extend(['dice', 'wallet'])

# Replace the skirt and the table and the scissors with the tree and the puzzle and the tiger in Box 6
box_6 = ['tree', 'puzzle', 'tiger']

# Remove the toothbrush from Box 4
box_4.remove('toothbrush')

# Swap the moon in Box 4 with the shoes in Box 0
box_4[3], box_0[0] = box_0[0], box_4[3]

# Print the final state of the boxes
print_boxes()