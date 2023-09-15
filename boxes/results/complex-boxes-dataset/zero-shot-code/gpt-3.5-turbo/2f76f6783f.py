box0 = ['cat', 'rock', 'submarine', 'scissors', 'hat']
box1 = []
box2 = ['coin', 'shark', 'star', 'elephant', 'charger']
box3 = ['clock', 'button', 'table']

# Swap the coin in Box 2 with the submarine in Box 0
box0[box0.index('submarine')], box2[box2.index('coin')] = box2[box2.index('coin')], box0[box0.index('submarine')]

# Put the helmet and the sock and the fork into Box 1
box1.extend(['helmet', 'sock', 'fork'])

# Put the truck and the thunder into Box 2
box2.extend(['truck', 'thunder'])

# Put the sun into Box 1
box1.append('sun')

# Swap the hat in Box 0 with the sock in Box 1
box0[box0.index('hat')], box1[box1.index('sock')] = box1[box1.index('sock')], box0[box0.index('hat')]

# Remove the coin from Box 0
box0.remove('coin')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)