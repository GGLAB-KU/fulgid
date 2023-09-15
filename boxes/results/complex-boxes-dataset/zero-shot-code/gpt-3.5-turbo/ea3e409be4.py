box_0 = ['bird']
box_1 = ['toothbrush', 'ship', 'butterfly']
box_2 = ['rock', 'helmet']
box_3 = ['towel', 'wig', 'bag']
box_4 = ['horn', 'glove', 'submarine', 'glasses']

# Replace items in Box 1
box_1.remove('toothbrush')
box_1.remove('ship')
box_1.remove('butterfly')
box_1.extend(['polish', 'skirt', 'razor'])

# Replace items in Box 4
box_4.remove('horn')
box_4.remove('glasses')
box_4.remove('submarine')
box_4.extend(['necklace', 'jungle', 'toaster'])

# Remove rock from Box 2
box_2.remove('rock')

# Move bird from Box 0 to Box 3
box_3.append(box_0.pop())

# Put scarf, note, and desert into Box 2
box_2.extend(['scarf', 'note', 'desert'])

# Remove items from Box 1
box_1.remove('polish')
box_1.remove('skirt')
box_1.remove('razor')

# Remove helmet from Box 2
box_2.remove('helmet')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)