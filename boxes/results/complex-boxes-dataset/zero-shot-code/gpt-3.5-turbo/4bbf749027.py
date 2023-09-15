box_0 = ['shirt', 'seaweed', 'thunder']
box_1 = ['charger', 'pants', 'cat', 'bag', 'storm']
box_2 = []
box_3 = ['piano', 'ring', 'bird', 'guitar']
box_4 = ['horse', 'controller', 'table']
box_5 = ['toothbrush']
box_6 = ['boot', 'towel']

# Replace the bird and the guitar with the glove and the puzzle in Box 3
box_3.remove('bird')
box_3.remove('guitar')
box_3.extend(['glove', 'puzzle'])

# Put the glasses into Box 2
box_2.append('glasses')

# Remove the towel and the boot from Box 6
box_6.remove('towel')
box_6.remove('boot')

# Replace the seaweed and the thunder with the elephant and the freezer in Box 0
box_0.remove('seaweed')
box_0.remove('thunder')
box_0.extend(['elephant', 'freezer'])

# Swap the charger in Box 1 with the glasses in Box 2
box_1.remove('charger')
box_2.remove('glasses')
box_1.append('glasses')
box_2.append('charger')

# Remove the charger from Box 2
box_2.remove('charger')

# Move the shirt and the elephant and the freezer from Box 0 to Box 5
box_0.remove('shirt')
box_0.remove('elephant')
box_0.remove('freezer')
box_5.extend(['shirt', 'elephant', 'freezer'])

# Remove the puzzle from Box 3
box_3.remove('puzzle')

# Move the storm and the cat from Box 1 to Box 4
box_1.remove('storm')
box_1.remove('cat')
box_4.extend(['storm', 'cat'])

# Move the toothbrush from Box 5 to Box 2
box_5.remove('toothbrush')
box_2.append('toothbrush')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)