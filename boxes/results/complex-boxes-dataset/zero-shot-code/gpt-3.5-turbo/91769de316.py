box_0 = ['rock', 'doll', 'boot']
box_1 = []
box_2 = ['toothbrush', 'pen', 'dice']
box_3 = ['bus']
box_4 = ['usb', 'mountain']
box_5 = ['fork', 'toothpaste']
box_6 = ['gloves', 'comb', 'horse']
box_7 = ['glove']

# Put the shirt into Box 3
box_3.append('shirt')

# Replace the toothpaste and the fork with the wallet and the shelf in Box 5
box_5.remove('toothpaste')
box_5.remove('fork')
box_5.extend(['wallet', 'shelf'])

# Replace the shirt with the pen in Box 3
box_3.remove('shirt')
box_3.append('pen')

# Remove the bus from Box 3
box_3.remove('bus')

# Move the horse and the comb and the gloves from Box 6 to Box 5
box_5.extend(['horse', 'comb', 'gloves'])
box_6.remove('horse')
box_6.remove('comb')
box_6.remove('gloves')

# Move the mountain from Box 4 to Box 2
box_2.append('mountain')
box_4.remove('mountain')

# Replace the toothbrush and the pen and the dice with the usb and the drum and the rocket in Box 2
box_2.remove('toothbrush')
box_2.remove('pen')
box_2.remove('dice')
box_2.extend(['usb', 'drum', 'rocket'])

# Replace the glove with the dress in Box 7
box_7.remove('glove')
box_7.append('dress')

# Put the whistle and the snow into Box 6
box_6.extend(['whistle', 'snow'])

# Remove the snow from Box 6
box_6.remove('snow')

# Remove the whistle from Box 6
box_6.remove('whistle')

# Move the boot and the rock and the doll from Box 0 to Box 5
box_5.extend(['boot', 'rock', 'doll'])
box_0.remove('boot')
box_0.remove('rock')
box_0.remove('doll')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)