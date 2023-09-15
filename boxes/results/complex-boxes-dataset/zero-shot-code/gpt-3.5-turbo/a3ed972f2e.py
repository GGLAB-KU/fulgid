box0 = ['wallet', 'lock', 'dice', 'rocket', 'forest']
box1 = ['earring']
box2 = ['speaker']
box3 = ['pan', 'console']
box4 = []
box5 = ['spoon', 'horse']
box6 = ['belt', 'necklace', 'mountain', 'rock']
box7 = ['dress', 'glasses', 'phone', 'beach', 'clock']

# Move phone, dress, and glasses from Box 7 to Box 1
box1.extend([box7.pop(box7.index('phone')), box7.pop(box7.index('dress')), box7.pop(box7.index('glasses'))])

# Replace console with soap in Box 3
box3[box3.index('console')] = 'soap'

# Empty Box 2
box2.clear()

# Put fridge and makeup into Box 3
box3.extend(['fridge', 'makeup'])

# Swap horse in Box 5 with rock in Box 6
box5[box5.index('horse')], box6[box6.index('rock')] = box6[box6.index('rock')], box5[box5.index('horse')]

# Remove forest from Box 0
box0.remove('forest')

# Remove spoon and rock from Box 5
box5.remove('spoon')
box5.remove('rock')

# Put drum, toaster, and note into Box 7
box7.extend(['drum', 'toaster', 'note'])

# Remove belt, mountain, and necklace from Box 6
box6.remove('belt')
box6.remove('mountain')
box6.remove('necklace')

# Put phone, jungle, and tie into Box 3
box3.extend(['phone', 'jungle', 'tie'])

# Move fridge and makeup from Box 3 to Box 7
box7.extend([box3.pop(box3.index('fridge')), box3.pop(box3.index('makeup'))])

# Remove horse from Box 6
box6.remove('horse')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)
print("Box 7:", box7)