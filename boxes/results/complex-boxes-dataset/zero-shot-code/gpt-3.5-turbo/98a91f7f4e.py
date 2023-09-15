box_0 = []
box_1 = []
box_2 = ['glove', 'fish', 'jungle']
box_3 = ['tie', 'seaweed', 'clock', 'ocean']
box_4 = ['fork', 'meteor', 'pen', 'earring', 'vase']
box_5 = ['boat', 'grass', 'freezer']
box_6 = ['skirt', 'wallet', 'card']
box_7 = []
box_8 = ['hat', 'dice', 'brush']
box_9 = ['star', 'mixer', 'storm', 'microwave']
box_10 = ['usb']
box_11 = ['rock', 'scissors', 'bracelet', 'cloud']
box_12 = []

# Move the glove and the fish from Box 2 to Box 0
box_0.extend(box_2.pop(box_2.index('glove')))
box_0.extend(box_2.pop(box_2.index('fish')))

# Remove the pen from Box 4
box_4.remove('pen')

# Replace the boat with the cow in Box 5
box_5[box_5.index('boat')] = 'cow'

# Swap the star in Box 9 with the clock in Box 3
box_9[box_9.index('star')], box_3[box_3.index('clock')] = box_3[box_3.index('clock')], box_9[box_9.index('star')]

# Put the sculpture into Box 6
box_6.append('sculpture')

# Swap the storm in Box 9 with the grass in Box 5
box_9[box_9.index('storm')], box_5[box_5.index('grass')] = box_5[box_5.index('grass')], box_9[box_9.index('storm')]

# Put the branch into Box 5
box_5.append('branch')

# Remove the jungle from Box 2
box_2.remove('jungle')

# Remove the meteor and the earring and the fork from Box 4
box_4.remove('meteor')
box_4.remove('earring')
box_4.remove('fork')

# Empty Box 4
box_4 = []

# Replace the hat with the desert in Box 8
box_8[box_8.index('hat')] = 'desert'

# Remove the star and the tie from Box 3
box_3.remove('star')
box_3.remove('tie')

# Remove the glove from Box 0
box_0.remove('glove')

# Move the clock and the grass and the microwave from Box 9 to Box 5
box_5.extend(box_9.pop(box_9.index('clock')))
box_5.extend(box_9.pop(box_9.index('grass')))
box_5.extend(box_9.pop(box_9.index('microwave')))

# Move the wallet from Box 6 to Box 9
box_9.append(box_6.pop(box_6.index('wallet')))

# Replace the branch with the motorcycle in Box 5
box_5[box_5.index('branch')] = 'motorcycle'

# Remove the usb from Box 10
box_10.remove('usb')

# Replace the wallet with the fish in Box 9
box_9[box_9.index('wallet')] = 'fish'

# Put the hat and the magnet and the rain into Box 7
box_7.extend(['hat', 'magnet', 'rain'])

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