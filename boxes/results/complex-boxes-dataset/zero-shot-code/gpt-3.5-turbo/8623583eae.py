box0 = []
box1 = ['beach', 'wallet', 'bowl']
box2 = ['tree']
box3 = ['earring']
box4 = []

# Put the chair, rock, and watch into Box 1
box1.extend(['chair', 'rock', 'watch'])

# Remove the drum from Box 1
box1.remove('drum')

# Move the tree from Box 2 to Box 4
box4.append(box2.pop())

# Swap the tree in Box 4 with the cup in Box 3
box4[0], box3[1] = box3[1], box4[0]

# Move the cup from Box 4 to Box 1
box1.append(box4.pop())

# Put the ring into Box 4
box4.append('ring')

# Empty Box 4
box4 = []

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)