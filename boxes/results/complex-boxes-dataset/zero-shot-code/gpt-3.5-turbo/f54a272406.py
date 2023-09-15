box_0 = ['pen', 'whistle', 'scarf', 'speaker']
box_1 = []
box_2 = ['boot', 'crown', 'shark']
box_3 = ['table', 'magnet']
box_4 = ['coin']
box_5 = ['jungle', 'soap']
box_6 = []

# Replace the soap with the charger in Box 5
box_5.remove('soap')
box_5.append('charger')

# Put the boot and the coin and the snow into Box 1
box_1.extend(['boot', 'coin', 'snow'])

# Move the boot and the coin from Box 1 to Box 0
box_0.extend(box_1[:2])
box_1 = box_1[2:]

# Put the phone and the jungle into Box 3
box_3.extend(['phone', 'jungle'])

# Empty Box 4
box_4 = []

# Replace the table and the phone with the coat and the needle in Box 3
box_3.remove('table')
box_3.remove('phone')
box_3.extend(['coat', 'needle'])

# Swap the speaker in Box 0 with the needle in Box 3
box_0.remove('speaker')
box_0.append('needle')

# Move the snow from Box 1 to Box 3
box_3.append('snow')
box_1.remove('snow')

# Swap the crown in Box 2 with the coat in Box 3
box_2.remove('crown')
box_2.append('coat')
box_3.remove('coat')
box_3.append('crown')

# Put the train into Box 4
box_4.append('train')

# Put the river into Box 1
box_1.append('river')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)