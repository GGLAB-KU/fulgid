box_0 = ['jungle', 'violin']
box_1 = ['flute', 'oven']
box_2 = ['telescope']
box_3 = ['key', 'tape', 'plate', 'laptop']
box_4 = ['lamp', 'star', 'apple']
box_5 = ['butterfly', 'boot', 'comb', 'island']
box_6 = ['river', 'freezer', 'magnet', 'bowl']

# Swap comb in Box 5 with oven in Box 1
box_1.append(box_5.pop(box_5.index('oven')))
box_5.append('comb')

# Swap bowl in Box 6 with jungle in Box 0
box_0.append(box_6.pop(box_6.index('jungle')))
box_6.append('bowl')

# Put car into Box 4
box_4.append('car')

# Replace violin and bowl with star and frame in Box 0
box_0.remove('violin')
box_0.remove('bowl')
box_0.extend(['star', 'frame'])

# Swap star in Box 0 with freezer in Box 6
box_0.append(box_6.pop(box_6.index('freezer')))
box_6.append('star')

# Empty Box 0
box_0 = []

# Move jungle and star from Box 6 to Box 4
box_4.extend(['jungle', 'star'])
box_6.remove('jungle')
box_6.remove('star')

# Move plate, tape, and laptop from Box 3 to Box 4
box_4.extend(['plate', 'tape', 'laptop'])
box_3.remove('plate')
box_3.remove('tape')
box_3.remove('laptop')

# Move key from Box 3 to Box 6
box_6.append(box_3.pop(box_3.index('key')))

# Move car from Box 4 to Box 1
box_1.append(box_4.pop(box_4.index('car')))

# Move star, jungle, and star from Box 4 to Box 6
box_6.extend(['star', 'jungle', 'star'])
box_4.remove('star')
box_4.remove('jungle')
box_4.remove('star')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)