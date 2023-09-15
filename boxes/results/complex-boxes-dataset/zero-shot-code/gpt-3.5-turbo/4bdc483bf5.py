box_0 = ['earring', 'pan', 'tiger', 'snow']
box_1 = ['laptop', 'paint', 'needle']
box_2 = ['shoes', 'lipstick']
box_3 = ['shorts', 'lamp']
box_4 = ['shoe', 'key', 'branch', 'puzzle']

# Swap paint in Box 1 with earring in Box 0
box_0[0], box_1[1] = box_1[1], box_0[0]

# Replace pan, tiger, and snow with doll, planet, and ocean in Box 0
box_0 = ['doll', 'planet', 'ocean']

# Remove needle, earring, and laptop from Box 1
box_1.remove('needle')
box_1.remove('earring')
box_1.remove('laptop')

# Replace lamp with spoon in Box 3
box_3[1] = 'spoon'

# Replace puzzle, key, and branch with umbrella, ship, and fish in Box 4
box_4 = ['umbrella', 'ship', 'fish']

# Remove paint from Box 0
box_0.remove('paint')

# Swap spoon in Box 3 with planet in Box 0
box_0[1], box_3[1] = box_3[1], box_0[1]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)