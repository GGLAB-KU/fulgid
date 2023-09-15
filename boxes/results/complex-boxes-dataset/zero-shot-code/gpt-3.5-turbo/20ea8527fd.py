box_0 = ['bird', 'bell']
box_1 = ['wire', 'river', 'comet', 'camera', 'sock']
box_2 = ['dog', 'table', 'sandals']
box_3 = ['cat', 'pants']
box_4 = ['bicycle', 'magnet', 'scissors', 'whistle', 'soap']

# Put the grinder and the vase into Box 4
box_4.extend(['grinder', 'vase'])

# Put the ship and the ring into Box 1
box_1.extend(['ship', 'ring'])

# Replace the whistle and the magnet and the scissors with the shelf and the butterfly and the plate in Box 4
box_4.remove('whistle')
box_4.remove('magnet')
box_4.remove('scissors')
box_4.extend(['shelf', 'butterfly', 'plate'])

# Put the moon into Box 4
box_4.append('moon')

# Move the wire from Box 1 to Box 2
box_2.append(box_1.pop(box_1.index('wire')))

# Swap the ship in Box 1 with the cat in Box 3
box_1[box_1.index('ship')], box_3[box_3.index('cat')] = box_3[box_3.index('cat')], box_1[box_1.index('ship')]

# Swap the butterfly in Box 4 with the sandals in Box 2
box_4[box_4.index('butterfly')], box_2[box_2.index('sandals')] = box_2[box_2.index('sandals')], box_4[box_4.index('butterfly')]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)