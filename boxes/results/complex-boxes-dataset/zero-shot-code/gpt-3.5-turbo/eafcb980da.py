box_0 = ['horn', 'branch', 'needle', 'basket']
box_1 = ['wire', 'coat', 'starfish']
box_2 = ['pot', 'usb', 'planet', 'thunder', 'spoon']
box_3 = ['swimsuit', 'earring', 'console']

# Remove wire and starfish from Box 1
box_1.remove('wire')
box_1.remove('starfish')

# Remove coat from Box 1
box_1.remove('coat')

# Replace swimsuit and console with coral and blanket in Box 3
box_3.remove('swimsuit')
box_3.remove('console')
box_3.extend(['coral', 'blanket'])

# Remove coral and blanket from Box 3
box_3.remove('coral')
box_3.remove('blanket')

# Replace horn and branch with keyboard and seaweed in Box 0
box_0.remove('horn')
box_0.remove('branch')
box_0.extend(['keyboard', 'seaweed'])

# Move seaweed from Box 0 to Box 2
seaweed = box_0.pop(box_0.index('seaweed'))
box_2.append(seaweed)

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)