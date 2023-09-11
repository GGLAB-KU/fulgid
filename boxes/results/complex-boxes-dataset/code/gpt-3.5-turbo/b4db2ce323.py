# Initial state of boxes
boxes = {
    0: ['telescope', 'blanket', 'apple'],
    1: ['pan', 'earring'],
    2: ['console'],
    3: ['elephant'],
    4: ['bear', 'belt', 'wire', 'forest', 'shark'],
    5: ['laptop', 'glove', 'bus', 'card'],
    6: ['boat', 'beach'],
    7: ['tiger', 'pillow', 'lightning', 'frame', 'puzzle'],
    8: ['octopus', 'moon', 'toy', 'flute', 'submarine'],
    9: ['butterfly', 'branch', 'piano', 'shoes'],
    10: ['lipstick']
}

# Replace the piano and the shoes with the blanket and the whistle in Box 9.
boxes[9].remove('piano')
boxes[9].remove('shoes')
boxes[9].append('blanket')
boxes[9].append('whistle')

# Put the bell into Box 3.
boxes[3].append('bell')

# Remove the submarine and the moon from Box 8.
boxes[8].remove('submarine')
boxes[8].remove('moon')

# Swap the toy in Box 8 with the lipstick in Box 10.
boxes[8].remove('toy')
boxes[10].remove('lipstick')
boxes[8].append('lipstick')
boxes[10].append('toy')

# Swap the boat in Box 6 with the lipstick in Box 8.
boxes[6].remove('boat')
boxes[8].remove('lipstick')
boxes[6].append('lipstick')
boxes[8].append('boat')

# Put the island into Box 0.
boxes[0].append('island')

# Swap the lipstick in Box 6 with the console in Box 2.
boxes[6].remove('lipstick')
boxes[2].remove('console')
boxes[6].append('console')
boxes[2].append('lipstick')

# Replace the beach and the console with the cup and the snow in Box 6.
boxes[6].remove('beach')
boxes[6].remove('console')
boxes[6].append('cup')
boxes[6].append('snow')

# Swap the card in Box 5 with the toy in Box 10.
boxes[5].remove('card')
boxes[10].remove('toy')
boxes[5].append('toy')
boxes[10].append('card')

# Move the pan and the earring from Box 1 to Box 0.
boxes[1].remove('pan')
boxes[1].remove('earring')
boxes[0].append('pan')
boxes[0].append('earring')

# Replace the tiger and the lightning and the puzzle with the sun and the camera and the tie in Box 7.
boxes[7].remove('tiger')
boxes[7].remove('lightning')
boxes[7].remove('puzzle')
boxes[7].append('sun')
boxes[7].append('camera')
boxes[7].append('tie')

# Swap the bell in Box 3 with the cup in Box 6.
boxes[3].remove('bell')
boxes[6].remove('cup')
boxes[3].append('cup')
boxes[6].append('bell')

# Move the toy and the bus from Box 5 to Box 7.
boxes[5].remove('toy')
boxes[5].remove('bus')
boxes[7].append('toy')
boxes[7].append('bus')

# Put the chair into Box 6.
boxes[6].append('chair')

# Put the rock and the jacket and the candle into Box 0.
boxes[0].append('rock')
boxes[0].append('jacket')
boxes[0].append('candle')

# Replace the elephant with the perfume in Box 3.
boxes[3].remove('elephant')
boxes[3].append('perfume')

# Remove the card from Box 10.
boxes[10].remove('card')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")