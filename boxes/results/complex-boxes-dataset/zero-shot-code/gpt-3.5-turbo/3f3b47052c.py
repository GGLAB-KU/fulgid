box_0 = ['pot', 'shorts', 'key', 'bell', 'toothpaste']
box_1 = ['sandals', 'violin', 'spoon', 'apple']
box_2 = ['cat']
box_3 = ['clock', 'puzzle', 'ring', 'laptop', 'comb']
box_4 = []
box_5 = ['paint']
box_6 = ['camera']

# Remove the cat from Box 2
box_2.remove('cat')

# Swap the bell in Box 0 with the clock in Box 3
box_0.remove('bell')
box_3.remove('clock')
box_0.append('clock')
box_3.append('bell')

# Put the sculpture and the grinder and the bicycle into Box 0
box_0.extend(['sculpture', 'grinder', 'bicycle'])

# Replace the bicycle and the grinder and the key with the lion and the ship and the dolphin in Box 0
box_0.remove('bicycle')
box_0.remove('grinder')
box_0.remove('key')
box_0.extend(['lion', 'ship', 'dolphin'])

# Swap the spoon in Box 1 with the clock in Box 0
box_1.remove('spoon')
box_0.remove('clock')
box_1.append('clock')
box_0.append('spoon')

# Replace the paint with the storm in Box 5
box_5.remove('paint')
box_5.append('storm')

# Replace the camera with the shelf in Box 6
box_6.remove('camera')
box_6.append('shelf')

# Swap the shelf in Box 6 with the apple in Box 1
box_6.remove('shelf')
box_1.remove('apple')
box_6.append('apple')
box_1.append('shelf')

# Move the violin from Box 1 to Box 3
box_1.remove('violin')
box_3.append('violin')

# Put the motorcycle and the sculpture and the planet into Box 1
box_1.extend(['motorcycle', 'sculpture', 'planet'])

# Replace the motorcycle with the shoe in Box 1
box_1.remove('motorcycle')
box_1.append('shoe')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)