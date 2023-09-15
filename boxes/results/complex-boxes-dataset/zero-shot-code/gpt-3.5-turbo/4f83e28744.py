box0 = ['snow', 'ring']
box1 = ['bear', 'motorcycle', 'beach', 'game', 'frame']
box2 = []
box3 = ['grass', 'umbrella', 'shark', 'headphone', 'bus']

# Move the ring from Box 0 to Box 2
box2.append(box0.pop(box0.index('ring')))

# Move the snow from Box 0 to Box 2
box2.append(box0.pop(box0.index('snow')))

# Move the shark and the grass and the headphone from Box 3 to Box 1
box1.extend([box3.pop(box3.index('shark')), box3.pop(box3.index('grass')), box3.pop(box3.index('headphone'))])

# Empty Box 2
box2 = []

# Swap the umbrella in Box 3 with the game in Box 1
box3[box3.index('umbrella')], box1[box1.index('game')] = box1[box1.index('game')], box3[box3.index('umbrella')]

# Move the game and the bus from Box 3 to Box 0
box0.extend([box3.pop(box3.index('game')), box3.pop(box3.index('bus'))])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)