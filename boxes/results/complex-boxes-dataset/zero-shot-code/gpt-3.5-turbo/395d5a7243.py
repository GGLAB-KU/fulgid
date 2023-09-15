box_0 = ['keyboard']
box_1 = []
box_2 = ['mirror', 'shark', 'watch']
box_3 = ['sun', 'scissors', 'needle']
box_4 = ['ocean', 'pants', 'fork', 'bag']
box_5 = ['towel', 'island', 'fridge', 'lion', 'mountain']
box_6 = ['bird', 'cloud', 'perfume']
box_7 = ['grinder']
box_8 = ['tiger', 'toothbrush', 'controller']
box_9 = ['swimsuit', 'tape', 'comet', 'lock', 'note']
box_10 = ['game']

# Move items from Box 4 to Box 3
box_3.extend([box_4.pop(box_4.index('fork'))])
box_3.extend([box_4.pop(box_4.index('ocean'))])
box_3.extend([box_4.pop(box_4.index('bag'))])

# Remove items from Box 6
box_6.remove('bird')
box_6.remove('cloud')
box_6.remove('perfume')

# Remove items from Box 8
box_8.remove('toothbrush')
box_8.remove('tiger')

# Put basket into Box 6
box_6.append('basket')

# Replace keyboard with rain in Box 0
box_0.remove('keyboard')
box_0.append('rain')

# Remove items from Box 3
box_3.remove('needle')
box_3.remove('ocean')

# Swap grinder in Box 7 with scissors in Box 3
box_7_index = box_7.index('grinder')
box_3_index = box_3.index('scissors')
box_7[box_7_index], box_3[box_3_index] = box_3[box_3_index], box_7[box_7_index]

# Put elephant and bicycle into Box 7
box_7.append('elephant')
box_7.append('bicycle')

# Put skirt, towel, and magnet into Box 0
box_0.append('skirt')
box_0.append('towel')
box_0.append('magnet')

# Move swimsuit, note, and comet from Box 9 to Box 4
box_4.extend([box_9.pop(box_9.index('swimsuit'))])
box_4.extend([box_9.pop(box_9.index('note'))])
box_4.extend([box_9.pop(box_9.index('comet'))])

# Swap sun in Box 3 with elephant in Box 7
box_3_index = box_3.index('sun')
box_7_index = box_7.index('elephant')
box_3[box_3_index], box_7[box_7_index] = box_7[box_7_index], box_3[box_3_index]

# Swap scissors in Box 7 with island in Box 5
box_7_index = box_7.index('scissors')
box_5_index = box_5.index('island')
box_7[box_7_index], box_5[box_5_index] = box_5[box_5_index], box_7[box_7_index]

# Move island and bicycle from Box 7 to Box 4
box_4.extend([box_7.pop(box_7.index('island'))])
box_4.extend([box_7.pop(box_7.index('bicycle'))])

# Put coin into Box 2
box_2.append('coin')

# Move controller from Box 8 to Box 1
box_1.append(box_8.pop(box_8.index('controller')))

# Put grass into Box 0
box_0.append('grass')

# Move bag from Box 3 to Box 10
box_10.append(box_3.pop(box_3.index('bag')))

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