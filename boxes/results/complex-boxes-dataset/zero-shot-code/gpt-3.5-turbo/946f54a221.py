box_0 = ['headphone', 'puzzle', 'pen', 'skirt', 'tree']
box_1 = ['harmonica', 'pillow']
box_2 = ['scissors', 'piano', 'phone', 'apple']
box_3 = ['coin', 'snow', 'bus', 'bicycle', 'microwave']
box_4 = []
box_5 = ['hat', 'forest', 'ship', 'bracelet']
box_6 = ['planet', 'shark']
box_7 = ['wallet', 'speaker', 'usb', 'bag']
box_8 = ['boat']
box_9 = []
box_10 = ['shirt', 'sandals', 'toothpaste', 'island']

# Put the shoe and the microscope and the submarine into Box 3
box_3.extend(['shoe', 'microscope', 'submarine'])

# Move the coin and the shoe and the bus from Box 3 to Box 5
box_5.extend([box_3.pop(box_3.index('coin')), box_3.pop(box_3.index('shoe')), box_3.pop(box_3.index('bus'))])

# Swap the shark in Box 6 with the wallet in Box 7
box_6[box_6.index('shark')], box_7[box_7.index('wallet')] = box_7[box_7.index('wallet')], box_6[box_6.index('shark')]

# Swap the speaker in Box 7 with the island in Box 10
box_7[box_7.index('speaker')], box_10[box_10.index('island')] = box_10[box_10.index('island')], box_7[box_7.index('speaker')]

# Replace the boat with the glove in Box 8
box_8[box_8.index('boat')] = 'glove'

# Move the skirt and the headphone from Box 0 to Box 1
box_1.extend([box_0.pop(box_0.index('skirt')), box_0.pop(box_0.index('headphone'))])

# Replace the shoe with the blanket in Box 5
box_5[box_5.index('shoe')] = 'blanket'

# Replace the phone and the apple and the piano with the sculpture and the thunder and the cloud in Box 2
box_2[box_2.index('phone')] = 'sculpture'
box_2[box_2.index('apple')] = 'thunder'
box_2[box_2.index('piano')] = 'cloud'

# Put the scissors and the earring into Box 6
box_6.extend(['scissors', 'earring'])

# Replace the pen and the tree and the puzzle with the cow and the tie and the horse in Box 0
box_0[box_0.index('pen')] = 'cow'
box_0[box_0.index('tree')] = 'tie'
box_0[box_0.index('puzzle')] = 'horse'

# Replace the bracelet and the forest with the ring and the ocean in Box 5
box_5[box_5.index('bracelet')] = 'ring'
box_5[box_5.index('forest')] = 'ocean'

# Remove the headphone from Box 1
box_1.remove('headphone')

# Replace the glove with the game in Box 8
box_8[box_8.index('glove')] = 'game'

# Move the game from Box 8 to Box 10
box_10.append(box_8.pop(box_8.index('game')))

# Swap the toothpaste in Box 10 with the tie in Box 0
box_10[box_10.index('toothpaste')], box_0[box_0.index('tie')] = box_0[box_0.index('tie')], box_10[box_10.index('toothpaste')]

# Remove the cloud and the thunder from Box 2
box_2.remove('cloud')
box_2.remove('thunder')

# Replace the bicycle and the microwave with the helmet and the lightning in Box 3
box_3[box_3.index('bicycle')] = 'helmet'
box_3[box_3.index('microwave')] = 'lightning'

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]):
    print(f"Box {i}: {box}")