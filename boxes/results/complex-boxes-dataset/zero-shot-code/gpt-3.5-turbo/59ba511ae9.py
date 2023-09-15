box_0 = ['cow']
box_1 = ['violin', 'zipper', 'meteor']
box_2 = ['key', 'dress', 'needle', 'starfish']
box_3 = ['grass', 'rain', 'phone']
box_4 = ['card', 'butterfly']
box_5 = ['pants', 'ship']
box_6 = ['leaf', 'towel', 'toaster']
box_7 = ['puzzle', 'harmonica']
box_8 = ['helmet', 'keyboard', 'frame', 'shoes']
box_9 = ['bird', 'necklace', 'bag', 'skirt']
box_10 = ['tree', 'scarf', 'coral', 'dog', 'swimsuit']

# Move items from Box 8 to Box 1
box_1.extend([box_8.pop(box_8.index('keyboard')), box_8.pop(box_8.index('frame')), box_8.pop(box_8.index('helmet'))])

# Move harmonica from Box 7 to Box 2
box_2.append(box_7.pop(box_7.index('harmonica')))

# Put piano and brush into Box 8
box_8.extend(['piano', 'brush'])

# Move necklace from Box 9 to Box 2
box_2.append(box_9.pop(box_9.index('necklace')))

# Swap scarf in Box 10 with rain in Box 3
box_10[box_10.index('scarf')], box_3[box_3.index('rain')] = box_3[box_3.index('rain')], box_10[box_10.index('scarf')]

# Remove leaf and towel from Box 6
box_6.remove('leaf')
box_6.remove('towel')

# Put forest into Box 1
box_1.append('forest')

# Move puzzle from Box 7 to Box 2
box_2.append(box_7.pop(box_7.index('puzzle')))

# Put meteor, doll, and seaweed into Box 0
box_0.extend(['meteor', 'doll', 'seaweed'])

# Replace scarf, phone, and grass with earring, coin, and lamp in Box 3
box_3[box_3.index('scarf')] = 'earring'
box_3[box_3.index('phone')] = 'coin'
box_3[box_3.index('grass')] = 'lamp'

# Replace skirt with shoe in Box 9
box_9[box_9.index('skirt')] = 'shoe'

# Replace bird, bag, and shoe with watch, wire, and magnet in Box 9
box_9[box_9.index('bird')] = 'watch'
box_9[box_9.index('bag')] = 'wire'
box_9[box_9.index('shoe')] = 'magnet'

# Replace toaster with umbrella in Box 6
box_6[box_6.index('toaster')] = 'umbrella'

# Remove piano from Box 8
box_8.remove('piano')

# Move lamp and earring from Box 3 to Box 6
box_6.extend([box_3.pop(box_3.index('lamp')), box_3.pop(box_3.index('earring'))])

# Remove card from Box 4
box_4.remove('card')

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