box0 = ['lion', 'bicycle']
box1 = ['oven', 'forest', 'dice', 'pants']
box2 = ['vase', 'watch', 'leaf', 'key', 'glasses']
box3 = []

# Move items from Box 2 to Box 3
box3.extend([box2.pop(box2.index('vase'))])
box3.extend([box2.pop(box2.index('watch'))])
box3.extend([box2.pop(box2.index('glasses'))])

# Swap lion in Box 0 with forest in Box 1
box0[box0.index('lion')], box1[box1.index('forest')] = box1[box1.index('forest')], box0[box0.index('lion')]

# Remove dice and oven from Box 1
box1.remove('dice')
box1.remove('oven')

# Move pants and lion from Box 1 to Box 2
box2.extend([box1.pop(box1.index('pants'))])
box2.extend([box1.pop(box1.index('lion'))])

# Remove key and lion from Box 2
box2.remove('key')
box2.remove('lion')

# Replace forest and bicycle with rocket and shelf in Box 0
box0[box0.index('forest')] = 'rocket'
box0[box0.index('bicycle')] = 'shelf'

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)