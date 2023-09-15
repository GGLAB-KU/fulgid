box_0 = ['towel', 'oven', 'battery']
box_1 = ['magnet', 'table', 'polish', 'wig', 'butterfly']
box_2 = ['card', 'glasses', 'game', 'dress']
box_3 = ['bus', 'zipper', 'makeup', 'comb', 'branch']
box_4 = ['desert']
box_5 = []
box_6 = ['pot', 'lipstick']
box_7 = []
box_8 = ['toothpaste', 'brush', 'shorts']

print("Initial State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)

# Move the table and the wig and the magnet from Box 1 to Box 2
box_2.extend([box_1.pop(box_1.index('table')), box_1.pop(box_1.index('wig')), box_1.pop(box_1.index('magnet'))])

# Move the branch from Box 3 to Box 1
box_1.append(box_3.pop(box_3.index('branch')))

# Move the polish and the branch and the butterfly from Box 1 to Box 4
box_4.extend([box_1.pop(box_1.index('polish')), box_1.pop(box_1.index('branch')), box_1.pop(box_1.index('butterfly'))])

# Swap the toothpaste in Box 8 with the lipstick in Box 6
box_8[box_8.index('toothpaste')], box_6[box_6.index('lipstick')] = box_6[box_6.index('lipstick')], box_8[box_8.index('toothpaste')]

# Move the battery from Box 0 to Box 4
box_4.append(box_0.pop(box_0.index('battery')))

# Remove the lipstick and the brush and the shorts from Box 8
box_8.remove('lipstick')
box_8.remove('brush')
box_8.remove('shorts')

# Empty Box 6
box_6.clear()

# Remove the towel from Box 0
box_0.remove('towel')

# Remove the zipper and the bus and the makeup from Box 3
box_3.remove('zipper')
box_3.remove('bus')
box_3.remove('makeup')

# Replace the table and the glasses with the magnet and the tree in Box 2
box_2[box_2.index('table')] = 'magnet'
box_2[box_2.index('glasses')] = 'tree'

# Move the comb from Box 3 to Box 7
box_7.append(box_3.pop(box_3.index('comb')))

# Move the comb from Box 7 to Box 4
box_4.append(box_7.pop(box_7.index('comb')))

# Remove the polish and the battery from Box 4
box_4.remove('polish')
box_4.remove('battery')

print("\nFinal State:")
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)