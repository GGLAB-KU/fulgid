box0 = ['pen', 'bell', 'lion', 'river', 'horse']
box1 = ['comet']
box2 = []
box3 = ['freezer', 'headphone', 'key', 'grinder']
box4 = ['beach', 'train', 'card']

# Replace items in Box 4
box4[0] = 'towel'
box4[1] = 'dog'
box4[2] = 'pot'

# Move items from Box 0 to Box 4
box4.extend([box0.pop(0), box0.pop(0), box0.pop(0)])

# Remove item from Box 1
box1.remove('comet')

# Replace item in Box 0
box0[3] = 'button'

# Move towel from Box 4 to Box 0
box0.append(box4.pop(0))

# Put items into Box 2
box2.extend(['charger', 'wig', 'mountain'])

# Remove items from Box 3
box3.remove('headphone')
box3.remove('grinder')
box3.remove('key')

# Print the boxes
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)