box_0 = ['brush', 'ocean', 'grass', 'razor']
box_1 = ['spoon', 'glasses']
box_2 = ['guitar']
box_3 = ['bus', 'doll']

# Put the wallet and the wire into Box 1
box_1.extend(['wallet', 'wire'])

# Swap the guitar in Box 2 with the brush in Box 0
box_0.remove('brush')
box_2.append('brush')

# Move the grass and the razor and the guitar from Box 0 to Box 2
box_2.extend(['grass', 'razor', 'guitar'])
box_0.remove('grass')
box_0.remove('razor')
box_0.remove('guitar')

# Put the rain and the tiger and the oven into Box 0
box_0.extend(['rain', 'tiger', 'oven'])

# Replace the spoon with the swimsuit in Box 1
box_1.remove('spoon')
box_1.append('swimsuit')

# Put the watch into Box 2
box_2.append('watch')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)