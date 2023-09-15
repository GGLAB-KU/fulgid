box_0 = ['lamp']
box_1 = ['cup', 'freezer']
box_2 = ['starfish', 'candle', 'horn', 'ring', 'coin']
box_3 = ['battery', 'tie', 'coral', 'pillow']
box_4 = ['lock', 'crown', 'submarine']
box_5 = ['comet']
box_6 = ['truck', 'branch', 'mask']
box_7 = ['magnet', 'shoes', 'flower']
box_8 = ['towel', 'car', 'pen']

# Replace the coral, tie, and pillow with the cow, horn, and glove in Box 3
box_3 = ['battery', 'cow', 'horn', 'glove']

# Move the branch from Box 6 to Box 4
box_4.append(box_6.pop(box_6.index('branch')))

# Replace the mask and the truck with the watch and the microscope in Box 6
box_6 = ['watch', 'microscope']

# Put the tree and the dolphin into Box 4
box_4.extend(['tree', 'dolphin'])

# Move the towel, car, and pen from Box 8 to Box 3
box_3.extend(box_8.pop(0))
box_3.extend(box_8.pop(0))
box_3.extend(box_8.pop(0))

# Empty Box 6
box_6 = []

# Swap the comet in Box 5 with the cup in Box 1
box_5, box_1 = box_1, box_5

# Remove the crown, dolphin, and submarine from Box 4
box_4.remove('crown')
box_4.remove('dolphin')
box_4.remove('submarine')

# Swap the candle in Box 2 with the lock in Box 4
box_2[box_2.index('candle')], box_4[box_4.index('lock')] = box_4[box_4.index('lock')], box_2[box_2.index('candle')]

# Move the cup from Box 5 to Box 8
box_8.append(box_5.pop(0))

# Put the bicycle into Box 3
box_3.append('bicycle')

# Replace the car, cow, and bicycle with the wire, oven, and shoe in Box 3
box_3 = ['battery', 'wire', 'oven', 'shoe']

# Put the controller into Box 8
box_8.append('controller')

# Put the mixer, boot, and cup into Box 6
box_6.extend(['mixer', 'boot', 'cup'])

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