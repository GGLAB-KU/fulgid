box_0 = ['magnet', 'telescope', 'doll']
box_1 = ['earring', 'rock', 'car']
box_2 = ['brush', 'fish', 'table']
box_3 = ['tiger', 'jungle']
box_4 = ['fridge', 'grass', 'motorcycle', 'drum']

# Move the table from Box 2 to Box 0
box_0.append(box_2.pop(2))

# Remove the doll from Box 0
box_0.remove('doll')

# Swap the earring in Box 1 with the fridge in Box 4
box_1[0], box_4[0] = box_4[0], box_1[0]

# Put the cow into Box 2
box_2.append('cow')

# Put the bear and the game into Box 1
box_1.extend(['bear', 'game'])

# Remove the fish and the cow from Box 2
box_2.remove('fish')
box_2.remove('cow')

# Move the motorcycle and the drum and the earring from Box 4 to Box 2
box_2.extend([box_4.pop(2), box_4.pop(2), box_4.pop(0)])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)