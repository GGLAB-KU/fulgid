box0 = ['seaweed', 'oven', 'scarf']
box1 = []
box2 = ['coin', 'tape', 'glove', 'thread', 'moon']
box3 = ['motorcycle', 'wallet', 'storm', 'rock', 'mixer']

# Swap the moon in Box 2 with the rock in Box 3
box2.remove('moon')
box3.remove('rock')
box2.append('rock')
box3.append('moon')

# Put the truck and the coral and the whistle into Box 3
box3.extend(['truck', 'coral', 'whistle'])

# Remove the glove from Box 2
box2.remove('glove')

# Remove the mixer from Box 3
box3.remove('mixer')

# Move the seaweed and the scarf and the oven from Box 0 to Box 1
box1.extend(box0)
box0.clear()

# Move the oven from Box 1 to Box 0
box0.append(box1.pop(box1.index('oven')))

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)