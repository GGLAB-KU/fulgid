box0 = ['pants', 'lock', 'river', 'glasses', 'horse']
box1 = ['button', 'puzzle', 'earring', 'dress', 'camera']
box2 = ['paint']
box3 = ['flower', 'necklace', 'toothpaste', 'shelf', 'microscope']

# Move river, lock, and horse from Box 0 to Box 3
box3.extend([box0.pop(box0.index('river')), box0.pop(box0.index('lock')), box0.pop(box0.index('horse'))])

# Swap puzzle in Box 1 with river in Box 3
box1[box1.index('puzzle')], box3[box3.index('river')] = box3[box3.index('river')], box1[box1.index('puzzle')]

# Put hat and makeup into Box 0
box0.extend(['hat', 'makeup'])

# Swap lock in Box 3 with glasses in Box 0
box3[box3.index('lock')], box0[box0.index('glasses')] = box0[box0.index('glasses')], box3[box3.index('lock')]

# Move shelf and flower from Box 3 to Box 1
box1.extend([box3.pop(box3.index('shelf')), box3.pop(box3.index('flower'))])

# Swap paint in Box 2 with glasses in Box 3
box2[box2.index('paint')], box3[box3.index('glasses')] = box3[box3.index('glasses')], box2[box2.index('paint')]

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)