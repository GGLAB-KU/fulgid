box_0 = ['razor', 'tree', 'harmonica', 'rocket', 'bell']
box_1 = ['rock', 'candle', 'note', 'charger', 'submarine']
box_2 = ['cow', 'spoon', 'tape']
box_3 = ['cup', 'controller', 'beach']
box_4 = ['basket', 'guitar', 'lock']

# Swap basket in Box 4 with cup in Box 3
box_4.remove('basket')
box_3.remove('cup')
box_4.append('cup')
box_3.append('basket')

# Replace rocket and tree with microscope and lipstick in Box 0
box_0.remove('rocket')
box_0.remove('tree')
box_0.append('microscope')
box_0.append('lipstick')

# Put scissors and magnet into Box 1
box_1.append('scissors')
box_1.append('magnet')

# Swap tape in Box 2 with microscope in Box 0
box_2.remove('tape')
box_0.remove('microscope')
box_2.append('microscope')
box_0.append('tape')

# Replace razor, harmonica, and tape with toy, laptop, and crown in Box 0
box_0.remove('razor')
box_0.remove('harmonica')
box_0.remove('tape')
box_0.append('toy')
box_0.append('laptop')
box_0.append('crown')

# Swap crown in Box 0 with guitar in Box 4
box_0.remove('crown')
box_4.remove('guitar')
box_0.append('guitar')
box_4.append('crown')

# Put coral, dice, and sculpture into Box 3
box_3.append('coral')
box_3.append('dice')
box_3.append('sculpture')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)