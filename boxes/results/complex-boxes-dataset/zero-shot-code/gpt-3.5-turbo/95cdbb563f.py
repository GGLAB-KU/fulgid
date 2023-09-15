box_0 = ['shoe']
box_1 = ['piano']
box_2 = []
box_3 = []
box_4 = ['hat', 'belt', 'needle']
box_5 = ['clock', 'bear', 'laptop']

# Move the laptop from Box 5 to Box 4
box_4.append(box_5.pop(box_5.index('laptop')))

# Put the dress into Box 1
box_1.append('dress')

# Remove the shoe from Box 0
box_0.remove('shoe')

# Replace the piano and the dress with the game and the desert in Box 1
box_1.remove('piano')
box_1.remove('dress')
box_1.append('game')
box_1.append('desert')

# Move the game from Box 1 to Box 3
box_3.append(box_1.pop(box_1.index('game')))

# Replace the hat and the needle with the coral and the seaweed in Box 4
box_4.remove('hat')
box_4.remove('needle')
box_4.append('coral')
box_4.append('seaweed')

# Swap the desert in Box 1 with the belt in Box 4
box_1.remove('desert')
box_4.remove('belt')
box_1.append('belt')
box_4.append('desert')

# Put the bird and the butterfly and the branch into Box 4
box_4.append('bird')
box_4.append('butterfly')
box_4.append('branch')

# Put the leaf and the scissors and the island into Box 1
box_1.append('leaf')
box_1.append('scissors')
box_1.append('island')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)