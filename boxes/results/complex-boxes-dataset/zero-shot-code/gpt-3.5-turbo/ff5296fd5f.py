box_0 = ['doll', 'dice']
box_1 = ['rain', 'bowl']
box_2 = ['whistle', 'comb', 'oven', 'hat']
box_3 = ['headphone', 'usb', 'tree']
box_4 = ['jungle']
box_5 = []
box_6 = ['crown']
box_7 = ['towel', 'coat']

# Swap comb in Box 2 with towel in Box 7
box_2.remove('comb')
box_7.remove('towel')
box_2.append('towel')
box_7.append('comb')

# Replace comb with headphone in Box 7
box_7.remove('comb')
box_7.append('headphone')

# Put brush, sun, and necklace into Box 0
box_0.extend(['brush', 'sun', 'necklace'])

# Remove usb from Box 3
box_3.remove('usb')

# Swap headphone in Box 3 with hat in Box 2
box_3.remove('headphone')
box_2.remove('hat')
box_3.append('hat')
box_2.append('headphone')

# Remove jungle from Box 4
box_4.remove('jungle')

# Replace dice with mirror in Box 0
box_0.remove('dice')
box_0.append('mirror')

# Empty Box 6
box_6.clear()

# Swap oven in Box 2 with tree in Box 3
box_2.remove('oven')
box_3.remove('tree')
box_2.append('tree')
box_3.append('oven')

# Replace oven with storm in Box 3
box_3.remove('oven')
box_3.append('storm')

# Put boot, swimsuit, and shoes into Box 6
box_6.extend(['boot', 'swimsuit', 'shoes'])

# Remove storm and hat from Box 3
box_3.remove('storm')
box_3.remove('hat')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)