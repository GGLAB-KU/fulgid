box0 = []
box1 = ['snow', 'bowl', 'rocket']
box2 = ['bus']
box3 = ['cat', 'flute']

# Put the cloud into Box 3
box3.append('cloud')

# Put the shelf and the fish into Box 3
box3.extend(['shelf', 'fish'])

# Move the shelf and the cat from Box 3 to Box 2
box2.extend([box3.pop(box3.index('shelf')), box3.pop(box3.index('cat'))])

# Swap the cat in Box 2 with the rocket in Box 1
box2[box2.index('cat')], box1[box1.index('rocket')] = box1[box1.index('rocket')], box2[box2.index('cat')]

# Replace the fish with the scarf in Box 3
box3[box3.index('fish')] = 'scarf'

# Swap the rocket in Box 2 with the bowl in Box 1
box2[box2.index('rocket')], box1[box1.index('bowl')] = box1[box1.index('bowl')], box2[box2.index('rocket')]

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)