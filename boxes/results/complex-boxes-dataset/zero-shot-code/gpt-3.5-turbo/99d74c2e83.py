box0 = ['polish', 'zipper']
box1 = ['blender', 'rock', 'bowl']
box2 = ['glasses', 'vase', 'pants']
box3 = ['wallet', 'submarine', 'cloud', 'dice', 'phone']
box4 = []

# Swap the dice in Box 3 with the rock in Box 1
box1.remove('rock')
box3.remove('dice')
box1.append('dice')
box3.append('rock')

# Swap the glasses in Box 2 with the wallet in Box 3
box2.remove('glasses')
box3.remove('wallet')
box2.append('wallet')
box3.append('glasses')

# Move the glasses and the cloud and the submarine from Box 3 to Box 0
box0.extend(['glasses', 'cloud', 'submarine'])
box3.remove('glasses')
box3.remove('cloud')
box3.remove('submarine')

# Remove the wallet from Box 2
box2.remove('wallet')

# Replace the glasses and the polish and the submarine with the candle and the glove and the pants in Box 0
box0.remove('glasses')
box0.remove('polish')
box0.remove('submarine')
box0.extend(['candle', 'glove', 'pants'])

# Put the vase and the mask into Box 3
box3.extend(['vase', 'mask'])

# Move the vase from Box 3 to Box 4
box4.append(box3.pop(box3.index('vase')))

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)