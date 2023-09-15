box_0 = []
box_1 = ['island', 'meteor']
box_2 = []
box_3 = ['comb', 'piano', 'lightning', 'pants', 'fridge']
box_4 = ['glasses', 'fork', 'mixer', 'rock', 'basket']
box_5 = ['microscope', 'bus', 'phone', 'car', 'oven']
box_6 = []
box_7 = ['controller']

# Remove the island from Box 1
box_1.remove('island')

# Swap the phone in Box 5 with the controller in Box 7
box_5.remove('phone')
box_7.remove('controller')
box_5.append('controller')
box_7.append('phone')

# Put the magnet and the helmet and the umbrella into Box 4
box_4.extend(['magnet', 'helmet', 'umbrella'])

# Swap the basket in Box 4 with the phone in Box 7
box_4.remove('basket')
box_7.remove('phone')
box_4.append('phone')
box_7.append('basket')

# Move the basket from Box 7 to Box 6
box_7.remove('basket')
box_6.append('basket')

# Replace the meteor with the fridge in Box 1
box_1.remove('meteor')
box_1.append('fridge')

# Replace the basket with the earring in Box 6
box_6.remove('basket')
box_6.append('earring')

# Put the keyboard and the crown and the hat into Box 0
box_0.extend(['keyboard', 'crown', 'hat'])

# Replace the umbrella and the phone and the helmet with the meteor and the vase and the jacket in Box 4
box_4.remove('umbrella')
box_4.remove('phone')
box_4.remove('helmet')
box_4.extend(['meteor', 'vase', 'jacket'])

# Swap the crown in Box 0 with the piano in Box 3
box_0.remove('crown')
box_3.remove('piano')
box_0.append('piano')
box_3.append('crown')

# Move the piano and the hat from Box 0 to Box 3
box_0.remove('piano')
box_0.remove('hat')
box_3.append('piano')
box_3.append('hat')

# Swap the bus in Box 5 with the hat in Box 3
box_5.remove('bus')
box_3.remove('hat')
box_5.append('hat')
box_3.append('bus')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)