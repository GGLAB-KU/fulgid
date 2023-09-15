box_0 = ['microwave']
box_1 = []
box_2 = ['brush', 'pants', 'rock']
box_3 = ['flute', 'moon', 'polish']
box_4 = ['speaker', 'motorcycle', 'island']
box_5 = ['lamp', 'jacket', 'scissors', 'console', 'soap']
box_6 = []
box_7 = ['tape']
box_8 = ['clock', 'crown', 'pen', 'blender', 'glasses']
box_9 = []
box_10 = ['mirror', 'paint', 'shelf', 'bird', 'sock']

# Replace the flute and the polish and the moon with the card and the charger and the bracelet in Box 3
box_3 = ['card', 'charger', 'bracelet']

# Swap the pants in Box 2 with the card in Box 3
box_2.remove('pants')
box_3.append('pants')

# Swap the bracelet in Box 3 with the mirror in Box 10
box_3.remove('bracelet')
box_10.remove('mirror')
box_3.append('mirror')
box_10.append('bracelet')

# Move the tape from Box 7 to Box 2
box_7.remove('tape')
box_2.append('tape')

# Swap the island in Box 4 with the jacket in Box 5
box_4.remove('island')
box_5.remove('jacket')
box_4.append('jacket')
box_5.append('island')

# Move the tape from Box 2 to Box 6
box_2.remove('tape')
box_6.append('tape')

# Replace the speaker and the motorcycle with the phone and the coin in Box 4
box_4.remove('speaker')
box_4.remove('motorcycle')
box_4.append('phone')
box_4.append('coin')

# Replace the microwave with the blanket in Box 0
box_0.remove('microwave')
box_0.append('blanket')

# Put the cloud and the swimsuit and the speaker into Box 5
box_5.extend(['cloud', 'swimsuit', 'speaker'])

# Swap the crown in Box 8 with the card in Box 2
box_8.remove('crown')
box_2.remove('card')
box_8.append('card')
box_2.append('crown')

# Swap the jacket in Box 4 with the charger in Box 3
box_4.remove('jacket')
box_3.remove('charger')
box_4.append('charger')
box_3.append('jacket')

# Move the shelf and the bracelet from Box 10 to Box 4
box_10.remove('shelf')
box_10.remove('bracelet')
box_4.append('shelf')
box_4.append('bracelet')

# Swap the jacket in Box 3 with the bracelet in Box 2
box_3.remove('jacket')
box_2.remove('bracelet')
box_3.append('bracelet')
box_2.append('jacket')

# Swap the pants in Box 3 with the charger in Box 4
box_3.remove('pants')
box_4.remove('charger')
box_3.append('charger')
box_4.append('pants')

# Remove the sock from Box 10
box_10.remove('sock')

# Remove the rock and the brush and the crown from Box 2
box_2.remove('rock')
box_2.remove('brush')
box_2.remove('crown')

# Replace the cloud and the lamp and the speaker with the thread and the train and the mountain in Box 5
box_5.remove('cloud')
box_5.remove('lamp')
box_5.remove('speaker')
box_5.append('thread')
box_5.append('train')
box_5.append('mountain')

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