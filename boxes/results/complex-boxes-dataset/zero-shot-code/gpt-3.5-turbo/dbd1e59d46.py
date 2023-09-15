box0 = ['car', 'plane', 'sandals', 'microscope']
box1 = []
box2 = ['whistle', 'tree', 'keyboard', 'lipstick']
box3 = ['bag', 'moon', 'razor']

# Move the tree and the whistle from Box 2 to Box 3
box3.append(box2.pop(box2.index('tree')))
box3.append(box2.pop(box2.index('whistle')))

# Move the tree and the bag and the whistle from Box 3 to Box 1
box1.append(box3.pop(box3.index('tree')))
box1.append(box3.pop(box3.index('bag')))
box1.append(box3.pop(box3.index('whistle')))

# Empty Box 1
box1 = []

# Empty Box 3
box3 = []

# Move the keyboard from Box 2 to Box 3
box3.append(box2.pop(box2.index('keyboard')))

# Replace the keyboard with the grinder in Box 3
box3[box3.index('keyboard')] = 'grinder'

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)