box_0 = ['crown', 'submarine', 'zipper']
box_1 = ['makeup', 'scissors', 'belt', 'fish']
box_2 = ['umbrella', 'book']
box_3 = ['seaweed', 'tiger', 'glasses', 'necklace']
box_4 = ['polish', 'jungle']
box_5 = ['camera', 'puzzle', 'pen']
box_6 = ['leaf', 'clock', 'cloud', 'keyboard']

# Remove clock, cloud, and leaf from Box 6
box_6.remove('clock')
box_6.remove('cloud')
box_6.remove('leaf')

# Move camera, puzzle, and pen from Box 5 to Box 0
box_0.extend(box_5[0:3])
box_5 = []

# Swap pen in Box 0 with book in Box 2
box_0[box_0.index('pen')] = box_2.pop()

# Move glasses from Box 3 to Box 0
box_0.append(box_3.pop(box_3.index('glasses')))

# Replace tiger and seaweed with camera and microscope in Box 3
box_3.remove('tiger')
box_3.remove('seaweed')
box_3.extend(['camera', 'microscope'])

# Replace camera, crown, and zipper with spoon, lipstick, and bear in Box 0
box_0.remove('camera')
box_0.remove('crown')
box_0.remove('zipper')
box_0.extend(['spoon', 'lipstick', 'bear'])

# Remove spoon from Box 0
box_0.remove('spoon')

# Put polish, doll, and button into Box 4
box_4.extend(['polish', 'doll', 'button'])

# Empty Box 6
box_6 = []

# Put shoe and fork into Box 0
box_0.extend(['shoe', 'fork'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)