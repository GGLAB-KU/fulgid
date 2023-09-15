box_0 = []
box_1 = ['star', 'coral']
box_2 = ['scissors']
box_3 = ['laptop', 'hat', 'polish', 'mirror', 'ship']
box_4 = ['ring']
box_5 = []
box_6 = ['game', 'spoon', 'wig', 'bicycle']
box_7 = ['toaster', 'lamp', 'microwave']
box_8 = ['seaweed', 'console']

# Remove spoon, bicycle, and game from Box 6
box_6.remove('spoon')
box_6.remove('bicycle')
box_6.remove('game')

# Move star and coral from Box 1 to Box 3
box_3.extend(box_1)
box_1.clear()

# Replace console and seaweed with branch and swimsuit in Box 8
box_8.remove('seaweed')
box_8.remove('console')
box_8.append('branch')
box_8.append('swimsuit')

# Move scissors from Box 2 to Box 5
box_5.append(box_2.pop())

# Swap wig in Box 6 with ring in Box 4
box_6.remove('wig')
box_4.remove('ring')
box_6.append('ring')
box_4.append('wig')

# Replace wig with train in Box 4
box_4.remove('wig')
box_4.append('train')

# Put starfish, flute, and wig into Box 7
box_7.extend(['starfish', 'flute', 'wig'])

# Swap scissors in Box 5 with train in Box 4
box_5.append(box_4.pop())
box_4.append(box_5.pop())

# Empty Box 3
box_3.clear()

# Swap swimsuit in Box 8 with scissors in Box 4
box_8.append(box_4.pop())
box_4.append(box_8.pop())

# Empty Box 6
box_6.clear()

# Swap train in Box 5 with starfish in Box 7
box_5.append(box_7.pop())
box_7.append(box_5.pop())

# Put jungle and glasses into Box 7
box_7.extend(['jungle', 'glasses'])

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