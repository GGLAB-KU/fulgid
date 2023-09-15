box0 = ['crown', 'car']
box1 = ['whistle', 'cup', 'ring']
box2 = ['gloves', 'button', 'fork', 'dice', 'drum']
box3 = ['plate', 'tape', 'tiger']
box4 = ['seaweed']

# Move items from Box 3 to Box 1
box1.extend([box3.pop(box3.index('plate')), box3.pop(box3.index('tape')), box3.pop(box3.index('tiger'))])

# Move items from Box 0 to Box 2
box2.extend([box0.pop(box0.index('car')), box0.pop(box0.index('crown'))])

# Remove items from Box 1
box1.remove('ring')
box1.remove('tape')
box1.remove('tiger')

# Put motorcycle into Box 2
box2.append('motorcycle')

# Put motorcycle and whistle into Box 3
box3.extend(['motorcycle', 'whistle'])

# Move cup from Box 1 to Box 0
box0.append(box1.pop(box1.index('cup')))

# Move seaweed from Box 4 to Box 1
box1.append(box4.pop(box4.index('seaweed')))

# Move cup from Box 0 to Box 3
box3.append(box0.pop(box0.index('cup')))

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)