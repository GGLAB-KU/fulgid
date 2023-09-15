box_0 = ['elephant', 'bear', 'magnet', 'star', 'battery']
box_1 = ['snow', 'wallet']
box_2 = ['headphone', 'ring', 'perfume', 'wig', 'ship']
box_3 = ['game']
box_4 = ['submarine', 'pen', 'charger']
box_5 = ['basket', 'octopus', 'lamp', 'horn']
box_6 = ['speaker', 'cat']
box_7 = []

# Remove the speaker from Box 6
box_6.remove('speaker')

# Swap the ship in Box 2 with the magnet in Box 0
box_0.remove('magnet')
box_2.remove('ship')
box_0.append('ship')
box_2.append('magnet')

# Replace the horn and the basket and the octopus with the comet and the apple and the toy in Box 5
box_5.remove('horn')
box_5.remove('basket')
box_5.remove('octopus')
box_5.append('comet')
box_5.append('apple')
box_5.append('toy')

# Swap the game in Box 3 with the wallet in Box 1
box_1.remove('wallet')
box_3.remove('game')
box_1.append('game')
box_3.append('wallet')

# Empty Box 1
box_1 = []

# Move the wallet from Box 3 to Box 0
box_3.remove('wallet')
box_0.append('wallet')

# Replace the pen and the submarine and the charger with the lamp and the truck and the fork in Box 4
box_4.remove('pen')
box_4.remove('submarine')
box_4.remove('charger')
box_4.append('lamp')
box_4.append('truck')
box_4.append('fork')

# Remove the apple from Box 5
box_5.remove('apple')

# Swap the cat in Box 6 with the toy in Box 5
box_5.remove('toy')
box_6.remove('cat')
box_5.append('cat')
box_6.append('toy')

# Move the cat and the comet from Box 5 to Box 1
box_5.remove('cat')
box_5.remove('comet')
box_1.append('cat')
box_1.append('comet')

# Replace the lamp with the train in Box 5
box_5.remove('lamp')
box_5.append('train')

# Move the wallet from Box 0 to Box 1
box_0.remove('wallet')
box_1.append('wallet')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)