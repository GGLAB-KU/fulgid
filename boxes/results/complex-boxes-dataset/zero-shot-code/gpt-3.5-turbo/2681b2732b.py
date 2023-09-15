box_0 = ['soap', 'thunder', 'coin']
box_1 = ['dice']
box_2 = ['flute', 'necklace', 'plate', 'comb', 'fork']
box_3 = ['bus', 'train', 'river']
box_4 = ['mountain', 'umbrella', 'forest', 'doll', 'usb']
box_5 = ['charger', 'seaweed', 'wire', 'coral']
box_6 = ['keyboard', 'planet']

# Replace the keyboard with the dice in Box 6
box_6.remove('keyboard')
box_6.append('dice')

# Swap the soap in Box 0 with the comb in Box 2
box_0.remove('soap')
box_2.remove('comb')
box_0.append('comb')
box_2.append('soap')

# Move the mountain from Box 4 to Box 0
box_4.remove('mountain')
box_0.append('mountain')

# Remove the dice from Box 1
box_1.remove('dice')

# Replace the bus and the river and the train with the cat and the toothpaste and the wire in Box 3
box_3.remove('bus')
box_3.remove('train')
box_3.remove('river')
box_3.append('cat')
box_3.append('toothpaste')
box_3.append('wire')

# Move the planet and the dice from Box 6 to Box 4
box_6.remove('planet')
box_4.append('planet')
box_6.remove('dice')
box_4.append('dice')

# Swap the thunder in Box 0 with the necklace in Box 2
box_0.remove('thunder')
box_2.remove('necklace')
box_0.append('necklace')
box_2.append('thunder')

# Move the coral and the wire and the charger from Box 5 to Box 0
box_5.remove('coral')
box_5.remove('wire')
box_5.remove('charger')
box_0.append('coral')
box_0.append('wire')
box_0.append('charger')

# Swap the thunder in Box 2 with the coin in Box 0
box_2.remove('thunder')
box_0.remove('coin')
box_2.append('coin')
box_0.append('thunder')

# Remove the plate from Box 2
box_2.remove('plate')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)