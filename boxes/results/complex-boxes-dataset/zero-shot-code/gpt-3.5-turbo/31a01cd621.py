box0 = ['boat']
box1 = ['brush']
box2 = ['button', 'motorcycle']
box3 = ['octopus', 'plane', 'ocean', 'pillow', 'puzzle']
box4 = ['magnet', 'spoon', 'blender', 'dress', 'leaf']
box5 = []
box6 = ['microwave']
box7 = ['charger', 'belt', 'hat', 'shelf', 'perfume']

# Move the ocean and the puzzle from Box 3 to Box 1
box1.extend(['ocean', 'puzzle'])
box3.remove('ocean')
box3.remove('puzzle')

# Swap the boat in Box 0 with the puzzle in Box 1
box0[0], box1[box1.index('puzzle')] = box1[box1.index('puzzle')], box0[0]

# Replace the puzzle with the river in Box 0
box0[0] = 'river'

# Put the submarine and the mixer into Box 2
box2.extend(['submarine', 'mixer'])

# Remove the boat and the ocean and the brush from Box 1
box1.remove('boat')
box1.remove('ocean')
box1.remove('brush')

# Swap the blender in Box 4 with the microwave in Box 6
box4[box4.index('blender')], box6[0] = box6[0], box4[box4.index('blender')]

# Put the ocean and the watch into Box 0
box0.extend(['ocean', 'watch'])

# Remove the river from Box 0
box0.remove('river')

# Put the guitar and the freezer and the bear into Box 2
box2.extend(['guitar', 'freezer', 'bear'])

# Replace the perfume with the keyboard in Box 7
box7[box7.index('perfume')] = 'keyboard'

# Move the shelf from Box 7 to Box 5
box5.append(box7.pop(box7.index('shelf')))

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)
print("Box 7:", box7)