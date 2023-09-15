box_0 = ['keyboard', 'mountain', 'hat']
box_1 = ['beach', 'oven', 'makeup']
box_2 = ['shoes', 'river', 'lion', 'whistle']
box_3 = ['harmonica', 'boot']
box_4 = ['glasses', 'sun', 'sculpture']

# Replace keyboard with helmet in Box 0
box_0[0] = 'helmet'

# Move glasses from Box 4 to Box 2
box_2.append(box_4.pop(0))

# Put harmonica, drum, and microwave into Box 1
box_1.extend(['harmonica', 'drum', 'microwave'])

# Remove mountain and helmet from Box 0
box_0.remove('mountain')
box_0.remove('helmet')

# Put needle into Box 1
box_1.append('needle')

# Empty Box 0
box_0 = []

# Put skirt, soap, and pants into Box 0
box_0.extend(['skirt', 'soap', 'pants'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)