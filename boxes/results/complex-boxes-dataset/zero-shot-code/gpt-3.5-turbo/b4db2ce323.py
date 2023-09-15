box_0 = ['telescope', 'blanket', 'apple']
box_1 = ['pan', 'earring']
box_2 = ['console']
box_3 = ['elephant']
box_4 = ['bear', 'belt', 'wire', 'forest', 'shark']
box_5 = ['laptop', 'glove', 'bus', 'card']
box_6 = ['boat', 'beach']
box_7 = ['tiger', 'pillow', 'lightning', 'frame', 'puzzle']
box_8 = ['octopus', 'moon', 'toy', 'flute', 'submarine']
box_9 = ['butterfly', 'branch', 'piano', 'shoes']
box_10 = ['lipstick']

# Replace the piano and the shoes with the blanket and the whistle in Box 9
box_9.remove('piano')
box_9.remove('shoes')
box_9.append('blanket')
box_9.append('whistle')

# Put the bell into Box 3
box_3.append('bell')

# Remove the submarine and the moon from Box 8
box_8.remove('submarine')
box_8.remove('moon')

# Swap the toy in Box 8 with the lipstick in Box 10
box_8.remove('toy')
box_10.remove('lipstick')
box_8.append('lipstick')
box_10.append('toy')

# Swap the boat in Box 6 with the lipstick in Box 8
box_6.remove('boat')
box_8.remove('lipstick')
box_6.append('lipstick')
box_8.append('boat')

# Put the island into Box 0
box_0.append('island')

# Swap the lipstick in Box 6 with the console in Box 2
box_6.remove('lipstick')
box_2.remove('console')
box_6.append('console')
box_2.append('lipstick')

# Replace the beach and the console with the cup and the snow in Box 6
box_6.remove('beach')
box_6.remove('console')
box_6.append('cup')
box_6.append('snow')

# Swap the card in Box 5 with the toy in Box 10
box_5.remove('card')
box_10.remove('toy')
box_5.append('toy')
box_10.append('card')

# Move the pan and the earring from Box 1 to Box 0
box_1.remove('pan')
box_1.remove('earring')
box_0.append('pan')
box_0.append('earring')

# Replace the tiger and the lightning and the puzzle with the sun and the camera and the tie in Box 7
box_7.remove('tiger')
box_7.remove('lightning')
box_7.remove('puzzle')
box_7.append('sun')
box_7.append('camera')
box_7.append('tie')

# Swap the bell in Box 3 with the cup in Box 6
box_3.remove('bell')
box_6.remove('cup')
box_3.append('cup')
box_6.append('bell')

# Move the toy and the bus from Box 5 to Box 7
box_5.remove('toy')
box_5.remove('bus')
box_7.append('toy')
box_7.append('bus')

# Put the chair into Box 6
box_6.append('chair')

# Put the rock and the jacket and the candle into Box 0
box_0.append('rock')
box_0.append('jacket')
box_0.append('candle')

# Replace the elephant with the perfume in Box 3
box_3.remove('elephant')
box_3.append('perfume')

# Remove the card from Box 10
box_10.remove('card')

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