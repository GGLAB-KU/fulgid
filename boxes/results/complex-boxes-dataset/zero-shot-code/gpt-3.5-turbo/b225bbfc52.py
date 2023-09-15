box_0 = ['toy', 'whistle', 'table']
box_1 = ['watch', 'shorts', 'violin', 'brush', 'sun']
box_2 = ['rain', 'charger', 'coin', 'puzzle']
box_3 = ['dog', 'wire', 'lamp']
box_4 = ['star', 'helmet', 'piano', 'pillow']
box_5 = ['horse', 'hat', 'book']
box_6 = ['scarf', 'thread', 'comb']
box_7 = ['storm', 'river']
box_8 = ['grass', 'cup', 'card', 'flute', 'mixer']
box_9 = []
box_10 = ['blanket', 'polish', 'dice', 'ring']
box_11 = ['butterfly']
box_12 = ['needle']
box_13 = ['glove', 'necklace']

# Swap the needle in Box 12 with the charger in Box 2
box_12.remove('needle')
box_2.remove('charger')
box_12.append('charger')
box_2.append('needle')

# Put the console and the shoe into Box 12
box_12.append('console')
box_12.append('shoe')

# Replace the necklace with the mirror in Box 13
box_13.remove('necklace')
box_13.append('mirror')

# Move the butterfly from Box 11 to Box 12
box_11.remove('butterfly')
box_12.append('butterfly')

# Put the note and the watch and the storm into Box 2
box_2.append('note')
box_2.append('watch')
box_2.append('storm')

# Swap the watch in Box 2 with the shorts in Box 1
box_2.remove('watch')
box_1.remove('shorts')
box_2.append('shorts')
box_1.append('watch')

# Empty Box 13
box_13 = []

# Put the truck into Box 10
box_10.append('truck')

# Replace the shoe and the butterfly with the controller and the thread in Box 12
box_12.remove('shoe')
box_12.remove('butterfly')
box_12.append('controller')
box_12.append('thread')

# Swap the console in Box 12 with the lamp in Box 3
box_12.remove('console')
box_3.remove('lamp')
box_12.append('lamp')
box_3.append('console')

# Put the fish and the dice into Box 6
box_6.append('fish')
box_6.append('dice')

# Replace the needle with the jungle in Box 2
box_2.remove('needle')
box_2.append('jungle')

# Replace the jungle and the rain and the note with the coin and the butterfly and the bicycle in Box 2
box_2.remove('jungle')
box_2.remove('rain')
box_2.remove('note')
box_2.append('coin')
box_2.append('butterfly')
box_2.append('bicycle')

# Move the storm and the river from Box 7 to Box 10
box_7.remove('storm')
box_7.remove('river')
box_10.append('storm')
box_10.append('river')

# Swap the storm in Box 2 with the grass in Box 8
box_2.remove('storm')
box_8.remove('grass')
box_2.append('grass')
box_8.append('storm')

# Swap the hat in Box 5 with the console in Box 3
box_5.remove('hat')
box_3.remove('console')
box_5.append('console')
box_3.append('hat')

# Move the comb and the scarf from Box 6 to Box 12
box_6.remove('comb')
box_6.remove('scarf')
box_12.append('comb')
box_12.append('scarf')

# Replace the controller and the thread and the lamp with the laptop and the shampoo and the car in Box 12
box_12.remove('controller')
box_12.remove('thread')
box_12.remove('lamp')
box_12.append('laptop')
box_12.append('shampoo')
box_12.append('car')

# Replace the helmet with the phone in Box 4
box_4.remove('helmet')
box_4.append('phone')

# Remove the truck and the blanket and the storm from Box 10
box_10.remove('truck')
box_10.remove('blanket')
box_10.remove('storm')

# Put the brush and the elephant into Box 4
box_4.append('brush')
box_4.append('elephant')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13]):
    print(f"Box {i}: {box}")