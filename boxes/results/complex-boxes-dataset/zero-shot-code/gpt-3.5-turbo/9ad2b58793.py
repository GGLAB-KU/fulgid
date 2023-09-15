box_0 = ['leaf', 'blanket']
box_1 = ['telescope', 'guitar', 'meteor', 'comb', 'toothpaste']
box_2 = ['gloves', 'thread', 'bell', 'spoon', 'ship']
box_3 = ['boat', 'game', 'desert', 'planet']
box_4 = []
box_5 = ['glove', 'car', 'umbrella', 'candle', 'tiger']
box_6 = ['motorcycle', 'pan', 'island']
box_7 = ['mixer', 'horse', 'bowl', 'fridge', 'star']
box_8 = []
box_9 = ['violin', 'wire', 'bird', 'clock']
box_10 = ['thunder', 'submarine', 'shorts', 'chair']

# Move the thread and the bell from Box 2 to Box 5
box_5.extend([box_2.pop(box_2.index('thread')), box_2.pop(box_2.index('bell'))])

# Put the bracelet and the speaker and the headphone into Box 10
box_10.extend(['bracelet', 'speaker', 'headphone'])

# Put the flute into Box 10
box_10.append('flute')

# Empty Box 0
box_0.clear()

# Put the key and the gloves and the wallet into Box 2
box_2.extend(['key', 'gloves', 'wallet'])

# Swap the island in Box 6 with the gloves in Box 2
box_6[box_6.index('island')], box_2[box_2.index('gloves')] = box_2[box_2.index('gloves')], box_6[box_6.index('island')]

# Put the mixer into Box 0
box_0.append(box_7.pop(box_7.index('mixer')))

# Move the telescope and the comb from Box 1 to Box 5
box_5.extend([box_1.pop(box_1.index('telescope')), box_1.pop(box_1.index('comb'))])

# Replace the meteor with the wallet in Box 1
box_1[box_1.index('meteor')] = box_1.pop(box_1.index('wallet'))

# Remove the ship and the paint and the island from Box 2
box_2.remove('ship')
box_2.remove('paint')
box_2.remove('island')

# Put the grinder and the ship into Box 8
box_8.extend(['grinder', 'ship'])

# Replace the telescope and the comb with the tie and the starfish in Box 5
box_5[box_5.index('telescope')] = 'tie'
box_5[box_5.index('comb')] = 'starfish'

# Move the fridge from Box 7 to Box 3
box_3.append(box_7.pop(box_7.index('fridge')))

# Put the lipstick and the wallet and the thunder into Box 1
box_1.extend(['lipstick', 'wallet', 'thunder'])

# Move the key and the wallet and the spoon from Box 2 to Box 1
box_1.extend([box_2.pop(box_2.index('key')), box_2.pop(box_2.index('wallet')), box_2.pop(box_2.index('spoon'))])

# Replace the pan and the gloves and the motorcycle with the bowl and the piano and the cloud in Box 6
box_6[box_6.index('pan')] = 'bowl'
box_6[box_6.index('gloves')] = 'piano'
box_6[box_6.index('motorcycle')] = 'cloud'

# Put the car and the pen and the boot into Box 0
box_0.extend(['car', 'pen', 'boot'])

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