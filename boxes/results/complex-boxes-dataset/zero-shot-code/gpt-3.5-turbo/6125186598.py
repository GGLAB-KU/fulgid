box0 = ['comet']
box1 = ['lamp', 'lock', 'flower', 'whistle', 'rain']
box2 = ['ship', 'leaf', 'game', 'blender']
box3 = ['plate', 'cup']
box4 = ['cow']

# Move the cow from Box 4 to Box 3
box3.append(box4.pop())

# Swap the cow in Box 3 with the lock in Box 1
box1[box1.index('lock')], box3[box3.index('cow')] = box3[box3.index('cow')], box1[box1.index('lock')]

# Swap the rain in Box 1 with the leaf in Box 2
box1[box1.index('rain')], box2[box2.index('leaf')] = box2[box2.index('leaf')], box1[box1.index('rain')]

# Move the leaf and the whistle and the flower from Box 1 to Box 3
box3.extend([box1.pop(box1.index('leaf')), box1.pop(box1.index('whistle')), box1.pop(box1.index('flower'))])

# Move the comet from Box 0 to Box 4
box4.append(box0.pop())

# Swap the comet in Box 4 with the rain in Box 2
box4[box4.index('comet')], box2[box2.index('rain')] = box2[box2.index('rain')], box4[box4.index('comet')]

# Move the lamp and the cow from Box 1 to Box 3
box3.extend([box1.pop(box1.index('lamp')), box1.pop(box1.index('cow'))])

# Replace the rain with the truck in Box 4
box2[box2.index('rain')] = 'truck'

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)