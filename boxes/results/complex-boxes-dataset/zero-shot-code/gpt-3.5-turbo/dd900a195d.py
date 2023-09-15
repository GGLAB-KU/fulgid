box0 = ['battery', 'fridge']
box1 = ['cup', 'needle']
box2 = ['butterfly']
box3 = ['wire', 'horn', 'clock']

# Replace clock, horn, and wire with hat, dice, and wallet in box3
box3.remove('clock')
box3.remove('horn')
box3.remove('wire')
box3.extend(['hat', 'dice', 'wallet'])

# Empty box0
box0.clear()

# Move butterfly from box2 to box0
box0.append(box2.pop())

# Put doll, storm, and game into box3
box3.extend(['doll', 'storm', 'game'])

# Swap storm in box3 with butterfly in box0
box0[0], box3[box3.index('storm')] = box3[box3.index('storm')], box0[0]

# Put plane, fish, and watch into box3
box3.extend(['plane', 'fish', 'watch'])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)