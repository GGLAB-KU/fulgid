box_0 = ['paint', 'polish']
box_1 = ['brush', 'pan', 'soap', 'cloud', 'coin']
box_2 = ['gloves', 'apple', 'motorcycle', 'branch', 'bicycle']
box_3 = ['shark', 'plane']
box_4 = []
box_5 = ['plate', 'shampoo', 'necklace', 'fridge', 'seaweed']
box_6 = ['coral', 'grinder', 'drum', 'headphone']
box_7 = ['key', 'mountain', 'pants']
box_8 = ['shoe', 'harmonica', 'earring', 'comb']
box_9 = ['starfish', 'bell']
box_10 = ['island', 'charger', 'cat', 'fork']
box_11 = []
box_12 = []

# Swap the pan in Box 1 with the pants in Box 7
box_1.remove('pan')
box_7.remove('pants')
box_1.append('pants')
box_7.append('pan')

# Replace the apple and the gloves and the bicycle with the belt and the perfume and the plate in Box 2
box_2.remove('apple')
box_2.remove('gloves')
box_2.remove('bicycle')
box_2.append('belt')
box_2.append('perfume')
box_2.append('plate')

# Move the shampoo from Box 5 to Box 9
box_5.remove('shampoo')
box_9.append('shampoo')

# Put the fish and the elephant and the dice into Box 2
box_2.append('fish')
box_2.append('elephant')
box_2.append('dice')

# Swap the dice in Box 2 with the shampoo in Box 9
box_2.remove('dice')
box_9.remove('shampoo')
box_2.append('shampoo')
box_9.append('dice')

# Replace the branch and the plate and the elephant with the storm and the moon and the tape in Box 2
box_2.remove('branch')
box_2.remove('plate')
box_2.remove('elephant')
box_2.append('storm')
box_2.append('moon')
box_2.append('tape')

# Move the mountain and the pan and the key from Box 7 to Box 0
box_7.remove('mountain')
box_7.remove('pan')
box_7.remove('key')
box_0.append('mountain')
box_0.append('pan')
box_0.append('key')

# Put the lightning into Box 8
box_8.append('lightning')

# Put the lightning and the island and the pants into Box 2
box_2.append('lightning')
box_2.append('island')
box_2.append('pants')

# Replace the fork and the island with the submarine and the shorts in Box 10
box_10.remove('fork')
box_10.remove('island')
box_10.append('submarine')
box_10.append('shorts')

# Replace the polish and the key with the piano and the wire in Box 0
box_0.remove('polish')
box_0.remove('key')
box_0.append('piano')
box_0.append('wire')

# Swap the fridge in Box 5 with the lightning in Box 8
box_5.remove('fridge')
box_8.remove('lightning')
box_5.append('lightning')
box_8.append('fridge')

# Put the moon into Box 12
box_12.append('moon')

# Replace the pants with the dice in Box 1
box_1.remove('pants')
box_1.append('dice')

# Empty Box 8
box_8 = []

# Remove the dice from Box 9
box_9.remove('dice')

# Remove the lightning from Box 2
box_2.remove('lightning')

# Remove the moon from Box 12
box_12.remove('moon')

# Empty Box 2
box_2 = []

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)
print("Box 10:", box_10)
print("Box 11:", box_11)
print("Box 12:", box_12)