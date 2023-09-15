box0 = ['butterfly', 'scarf', 'freezer']
box1 = ['sculpture', 'boot', 'harmonica', 'pen']
box2 = ['storm', 'desert', 'wallet', 'ring']
box3 = ['oven', 'note', 'lock', 'frame', 'rocket']
box4 = ['microwave', 'grass']

# Swap sculpture in box1 with note in box3
box1[0], box3[1] = box3[1], box1[0]

# Replace microwave and grass with coat and makeup in box4
box4 = ['coat', 'makeup']

# Swap pen in box1 with makeup in box4
box1[3], box4[1] = box4[1], box1[3]

# Remove harmonica and makeup from box1
box1.remove('harmonica')
box1.remove('makeup')

# Put flute and puzzle into box2
box2.extend(['flute', 'puzzle'])

# Move puzzle and desert from box2 to box0
box0.extend([box2.pop(1), box2.pop(1)])

# Remove storm and wallet from box2
box2.remove('storm')
box2.remove('wallet')

# Put shorts, bell, and bicycle into box4
box4.extend(['shorts', 'bell', 'bicycle'])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)