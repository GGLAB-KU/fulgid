box_0 = ['polish', 'phone', 'tape', 'doll', 'toaster']
box_1 = ['cloud', 'butterfly']
box_2 = ['earring']
box_3 = ['keyboard', 'key']
box_4 = ['cow', 'fridge', 'blender']
box_5 = ['helmet', 'star', 'bus', 'basket']
box_6 = ['shorts', 'violin']
box_7 = ['drum', 'thunder', 'meteor', 'fish', 'cup']
box_8 = ['perfume', 'desert', 'boot', 'needle']
box_9 = ['skirt', 'mirror', 'pen', 'charger']
box_10 = ['bag', 'mixer', 'lightning']
box_11 = ['toothpaste', 'makeup', 'coat', 'scissors', 'wire']
box_12 = []
box_13 = ['towel', 'glasses', 'fork', 'flower']

# Move the glasses from Box 13 to Box 12
box_12.append(box_13.pop(box_13.index('glasses')))

# Move the mixer and the lightning and the bag from Box 10 to Box 9
box_9.extend([box_10.pop(box_10.index('mixer')), box_10.pop(box_10.index('lightning')), box_10.pop(box_10.index('bag'))])

# Swap the violin in Box 6 with the thunder in Box 7
box_6[box_6.index('violin')], box_7[box_7.index('thunder')] = box_7[box_7.index('thunder')], box_6[box_6.index('violin')]

# Remove the skirt from Box 9
box_9.remove('skirt')

# Replace the pen and the mixer and the mirror with the tiger and the moon and the comb in Box 9
box_9.extend(['tiger', 'moon', 'comb'])
box_9.remove('pen')
box_9.remove('mixer')
box_9.remove('mirror')

# Remove the lightning and the comb and the moon from Box 9
box_9.remove('lightning')
box_9.remove('comb')
box_9.remove('moon')

# Put the motorcycle and the shark and the boat into Box 9
box_9.extend(['motorcycle', 'shark', 'boat'])

# Remove the shorts and the thunder from Box 6
box_6.remove('shorts')
box_7.remove('thunder')

# Empty Box 2
box_2.clear()

# Move the keyboard and the key from Box 3 to Box 5
box_5.extend([box_3.pop(box_3.index('keyboard')), box_3.pop(box_3.index('key'))])

# Remove the phone and the doll from Box 0
box_0.remove('phone')
box_0.remove('doll')

# Move the tiger from Box 9 to Box 13
box_13.append(box_9.pop(box_9.index('tiger')))

# Put the puzzle into Box 13
box_13.append('puzzle')

# Move the tape and the polish from Box 0 to Box 13
box_13.extend([box_0.pop(box_0.index('tape')), box_0.pop(box_0.index('polish'))])

# Replace the violin and the cup and the fish with the watch and the bear and the key in Box 7
box_7.extend(['watch', 'bear', 'key'])
box_7.remove('violin')
box_7.remove('cup')
box_7.remove('fish')

# Move the tape and the polish from Box 13 to Box 2
box_2.extend([box_13.pop(box_13.index('tape')), box_13.pop(box_13.index('polish'))])

# Replace the wire and the scissors with the octopus and the thread in Box 11
box_11.extend(['octopus', 'thread'])
box_11.remove('wire')
box_11.remove('scissors')

# Swap the cloud in Box 1 with the charger in Box 9
box_1[box_1.index('cloud')], box_9[box_9.index('charger')] = box_9[box_9.index('charger')], box_1[box_1.index('cloud')]

# Swap the blender in Box 4 with the cloud in Box 9
box_4[box_4.index('blender')], box_9[box_9.index('cloud')] = box_9[box_9.index('cloud')], box_4[box_4.index('blender')]

# Replace the desert with the thread in Box 8
box_8[box_8.index('desert')] = 'thread'

# Move the charger and the butterfly from Box 1 to Box 7
box_7.extend([box_1.pop(box_1.index('charger')), box_1.pop(box_1.index('butterfly'))])

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
print("Box 13:", box_13)