box_0 = ['camera', 'speaker', 'candle', 'drum']
box_1 = ['forest', 'tape']
box_2 = []
box_3 = ['lightning', 'harmonica']
box_4 = ['polish', 'lion', 'game', 'comb']

# Put the lion into Box 3
box_3.append(box_4.pop(box_4.index('lion')))

# Put the shirt into Box 1
box_1.append('shirt')

# Remove the candle and the camera and the drum from Box 0
box_0.remove('candle')
box_0.remove('camera')
box_0.remove('drum')

# Replace the lion and the harmonica with the console and the tree in Box 3
box_3.remove('lion')
box_3.remove('harmonica')
box_3.extend(['console', 'tree'])

# Move the lion and the game and the polish from Box 4 to Box 1
box_1.extend([box_4.pop(box_4.index('lion')), box_4.pop(box_4.index('game')), box_4.pop(box_4.index('polish'))])

# Put the tie into Box 0
box_0.append('tie')

# Move the tie from Box 0 to Box 4
box_4.append(box_0.pop(box_0.index('tie')))

# Replace the tie and the comb with the coat and the charger in Box 4
box_4.remove('tie')
box_4.remove('comb')
box_4.extend(['coat', 'charger'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)