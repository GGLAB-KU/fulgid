box_0 = ['hat', 'lamp', 'sock', 'storm']
box_1 = ['zipper', 'desert']
box_2 = ['bowl', 'freezer', 'jungle']
box_3 = ['belt', 'game']
box_4 = ['charger']
box_5 = []
box_6 = ['scissors']
box_7 = ['dog', 'pot', 'grinder']
box_8 = ['lion', 'forest', 'sandals', 'speaker', 'crown']
box_9 = ['razor']
box_10 = []
box_11 = ['clock']
box_12 = []

# Move the dog from Box 7 to Box 10
box_10.append(box_7.pop(0))

# Put the coral into Box 12
box_12.append('coral')

# Move the charger from Box 4 to Box 6
box_6.append(box_4.pop(0))

# Put the plate into Box 5
box_5.append('plate')

# Put the keyboard and the coral and the shirt into Box 0
box_0.extend(['keyboard', 'coral', 'shirt'])

# Move the sandals and the forest from Box 8 to Box 3
box_3.extend([box_8.pop(2), box_8.pop(1)])

# Move the jungle and the freezer and the bowl from Box 2 to Box 9
box_9.extend([box_2.pop(2), box_2.pop(1), box_2.pop(0)])

# Remove the zipper from Box 1
box_1.remove('zipper')

# Put the fish and the phone into Box 10
box_10.extend(['fish', 'phone'])

# Replace the shirt and the storm with the jungle and the island in Box 0
box_0.remove('shirt')
box_0.remove('storm')
box_0.extend(['jungle', 'island'])

# Put the toothbrush and the helmet into Box 7
box_7.extend(['toothbrush', 'helmet'])

# Put the mountain into Box 1
box_1.append('mountain')

# Put the shark and the mountain and the soap into Box 12
box_12.extend(['shark', 'mountain', 'soap'])

# Put the jungle and the tape into Box 4
box_4.extend(['jungle', 'tape'])

# Put the vase and the dice into Box 10
box_10.extend(['vase', 'dice'])

# Swap the game in Box 3 with the jungle in Box 4
box_3.remove('game')
box_4.remove('jungle')
box_3.append('jungle')
box_4.append('game')

# Replace the charger with the keyboard in Box 6
box_6.remove('charger')
box_6.append('keyboard')

# Put the cat into Box 4
box_4.append('cat')

# Put the hat and the rock into Box 1
box_1.extend(['hat', 'rock'])

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
print("Box 11:", box_11)
print("Box 12:", box_12)