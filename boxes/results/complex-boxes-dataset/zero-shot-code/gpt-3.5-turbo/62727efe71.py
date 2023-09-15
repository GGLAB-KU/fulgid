box_0 = ['branch', 'chair', 'speaker']
box_1 = ['wallet', 'horn', 'train', 'magnet', 'comb']
box_2 = ['mixer', 'shirt', 'pen']
box_3 = ['flute', 'dress', 'submarine']
box_4 = ['oven', 'telescope', 'seaweed']
box_5 = ['charger', 'apple', 'coat', 'star', 'spoon']
box_6 = ['horse', 'lion', 'table', 'ocean']
box_7 = ['thunder', 'basket', 'boot', 'gloves']
box_8 = ['dog', 'rock', 'motorcycle', 'glove']
box_9 = ['planet', 'coral', 'grinder']
box_10 = []

# Move the star and the charger from Box 5 to Box 6
box_6.extend([box_5.pop(box_5.index('star')), box_5.pop(box_5.index('charger'))])

# Put the mirror and the clock into Box 10
box_10.extend(['mirror', 'clock'])

# Put the flower into Box 10
box_10.append('flower')

# Replace the gloves and the boot with the crown and the violin in Box 7
box_7[box_7.index('gloves')] = 'crown'
box_7[box_7.index('boot')] = 'violin'

# Remove the coral and the planet from Box 9
box_9.remove('coral')
box_9.remove('planet')

# Remove the rock and the dog and the motorcycle from Box 8
box_8.remove('rock')
box_8.remove('dog')
box_8.remove('motorcycle')

# Swap the clock in Box 10 with the grinder in Box 9
box_10[box_10.index('clock')] = box_9.pop(box_9.index('grinder'))

# Replace the basket and the thunder with the necklace and the polish in Box 7
box_7[box_7.index('basket')] = 'necklace'
box_7[box_7.index('thunder')] = 'polish'

# Replace the seaweed and the telescope with the comb and the mixer in Box 4
box_4[box_4.index('seaweed')] = 'comb'
box_4[box_4.index('telescope')] = 'mixer'

# Put the card into Box 8
box_8.append('card')

# Move the ocean from Box 6 to Box 10
box_10.append(box_6.pop(box_6.index('ocean')))

# Remove the mixer from Box 2
box_2.remove('mixer')

# Put the wig and the doll and the mask into Box 7
box_7.extend(['wig', 'doll', 'mask'])

# Replace the oven and the comb and the mixer with the horn and the controller and the coral in Box 4
box_4[box_4.index('oven')] = 'horn'
box_4[box_4.index('comb')] = 'controller'
box_4[box_4.index('mixer')] = 'coral'

# Swap the horn in Box 4 with the submarine in Box 3
box_4[box_4.index('horn')] = box_3.pop(box_3.index('submarine'))

# Swap the wallet in Box 1 with the glove in Box 8
box_1[box_1.index('wallet')] = box_8.pop(box_8.index('glove'))

# Remove the branch and the speaker from Box 0
box_0.remove('branch')
box_0.remove('speaker')

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