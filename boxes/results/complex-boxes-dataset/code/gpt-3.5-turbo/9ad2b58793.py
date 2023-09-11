# Initial state of boxes
boxes = {
    0: ['leaf', 'blanket'],
    1: ['telescope', 'guitar', 'meteor', 'comb', 'toothpaste'],
    2: ['gloves', 'thread', 'bell', 'spoon', 'ship'],
    3: ['boat', 'game', 'desert', 'planet'],
    4: [],
    5: ['glove', 'car', 'umbrella', 'candle', 'tiger'],
    6: ['motorcycle', 'pan', 'island'],
    7: ['mixer', 'horse', 'bowl', 'fridge', 'star'],
    8: [],
    9: ['violin', 'wire', 'bird', 'clock'],
    10: ['thunder', 'submarine', 'shorts', 'chair']
}

# Move the thread and the bell from Box 2 to Box 5.
boxes[2].remove('thread')
boxes[2].remove('bell')
boxes[5].append('thread')
boxes[5].append('bell')

# Put the bracelet and the speaker and the headphone into Box 10.
boxes[10].append('bracelet')
boxes[10].append('speaker')
boxes[10].append('headphone')

# Put the flute into Box 10.
boxes[10].append('flute')

# Empty Box 0.
boxes[0] = []

# Put the key and the gloves and the wallet into Box 2.
boxes[2].append('key')
boxes[2].append('gloves')
boxes[2].append('wallet')

# Swap the island in Box 6 with the gloves in Box 2.
boxes[6].remove('island')
boxes[2].remove('gloves')
boxes[6].append('gloves')
boxes[2].append('island')

# Put the mixer into Box 0.
boxes[0].append('mixer')

# Move the telescope and the comb from Box 1 to Box 5.
boxes[1].remove('telescope')
boxes[1].remove('comb')
boxes[5].append('telescope')
boxes[5].append('comb')

# Replace the meteor with the wallet in Box 1.
boxes[1].remove('meteor')
boxes[1].append('wallet')

# Remove the ship and the paint and the island from Box 2.
boxes[2].remove('ship')
boxes[2].remove('paint')
boxes[2].remove('island')

# Put the grinder and the ship into Box 8.
boxes[8].append('grinder')
boxes[8].append('ship')

# Replace the telescope and the comb with the tie and the starfish in Box 5.
boxes[5].remove('telescope')
boxes[5].remove('comb')
boxes[5].append('tie')
boxes[5].append('starfish')

# Move the fridge from Box 7 to Box 3.
boxes[7].remove('fridge')
boxes[3].append('fridge')

# Put the lipstick and the wallet and the thunder into Box 1.
boxes[1].append('lipstick')
boxes[1].append('wallet')
boxes[1].append('thunder')

# Move the key and the wallet and the spoon from Box 2 to Box 1.
boxes[2].remove('key')
boxes[2].remove('wallet')
boxes[2].remove('spoon')
boxes[1].append('key')
boxes[1].append('wallet')
boxes[1].append('spoon')

# Replace the pan and the gloves and the motorcycle with the bowl and the piano and the cloud in Box 6.
boxes[6].remove('pan')
boxes[6].remove('gloves')
boxes[6].remove('motorcycle')
boxes[6].append('bowl')
boxes[6].append('piano')
boxes[6].append('cloud')

# Put the car and the pen and the boot into Box 0.
boxes[0].append('car')
boxes[0].append('pen')
boxes[0].append('boot')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")