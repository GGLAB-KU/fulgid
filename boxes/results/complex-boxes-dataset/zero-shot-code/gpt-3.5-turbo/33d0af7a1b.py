box_0 = ['camera', 'dolphin', 'jungle']
box_1 = ['wallet', 'bird', 'toaster', 'boat']
box_2 = ['whistle']
box_3 = ['seaweed', 'telescope', 'cat', 'drum', 'lightning']
box_4 = []
box_5 = ['piano', 'fish', 'mask', 'sculpture', 'table']
box_6 = ['pot']
box_7 = ['zipper', 'tree', 'sun']
box_8 = ['island', 'mountain']
box_9 = ['game', 'usb', 'lion', 'shoe']
box_10 = []

# Remove the mask, sculpture, and table from Box 5
box_5.remove('mask')
box_5.remove('sculpture')
box_5.remove('table')

# Move the tree and sun from Box 7 to Box 0
box_0.append(box_7.pop(box_7.index('tree')))
box_0.append(box_7.pop(box_7.index('sun')))

# Replace the game and usb with the octopus and seaweed in Box 9
box_9.remove('game')
box_9.remove('usb')
box_9.append('octopus')
box_9.append('seaweed')

# Swap the boat in Box 1 with the mountain in Box 8
box_1.remove('boat')
box_8.remove('mountain')
box_1.append('mountain')
box_8.append('boat')

# Replace the whistle with the pan in Box 2
box_2.remove('whistle')
box_2.append('pan')

# Swap the lion in Box 9 with the cat in Box 3
box_9.remove('lion')
box_3.remove('cat')
box_9.append('cat')
box_3.append('lion')

# Remove the pot from Box 6
box_6.remove('pot')

# Move the cat, seaweed, and shoe from Box 9 to Box 1
box_1.append(box_9.pop(box_9.index('cat')))
box_1.append(box_9.pop(box_9.index('seaweed')))
box_1.append(box_9.pop(box_9.index('shoe')))

# Remove the octopus from Box 9
box_9.remove('octopus')

# Move the boat from Box 8 to Box 0
box_0.append(box_8.pop(box_8.index('boat')))

# Swap the zipper in Box 7 with the island in Box 8
box_7.remove('zipper')
box_8.remove('island')
box_7.append('island')
box_8.append('zipper')

# Swap the zipper in Box 8 with the shoe in Box 1
box_8.remove('zipper')
box_1.remove('shoe')
box_8.append('shoe')
box_1.append('zipper')

# Replace the boat, tree, and sun with the lamp, moon, and bird in Box 0
box_0.remove('boat')
box_0.remove('tree')
box_0.remove('sun')
box_0.append('lamp')
box_0.append('moon')
box_0.append('bird')

# Replace the lamp and moon with the dice and ocean in Box 0
box_0.remove('lamp')
box_0.remove('moon')
box_0.append('dice')
box_0.append('ocean')

# Put the shirt into Box 6
box_6.append('shirt')

# Remove the island from Box 7
box_7.remove('island')

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