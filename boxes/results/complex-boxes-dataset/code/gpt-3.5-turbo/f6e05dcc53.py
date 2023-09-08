# Initial state of boxes
boxes = {
    0: ['doll', 'shirt', 'meteor', 'snow'],
    1: ['toy', 'wig', 'coin', 'river'],
    2: [],
    3: ['key', 'lion', 'frame', 'flower'],
    4: ['rocket', 'ring', 'camera', 'bell', 'shelf'],
    5: ['cow', 'soap', 'flute'],
    6: ['speaker', 'grinder', 'toothbrush', 'guitar'],
    7: [],
    8: ['tree'],
    9: []
}

# Remove the doll and the shirt from Box 0.
boxes[0].remove('doll')
boxes[0].remove('shirt')

# Remove the flower and the key from Box 3.
boxes[3].remove('flower')
boxes[3].remove('key')

# Move the snow and the meteor from Box 0 to Box 9.
boxes[0].remove('snow')
boxes[0].remove('meteor')
boxes[9].append('snow')
boxes[9].append('meteor')

# Replace the guitar and the speaker and the grinder with the rain and the fish and the shark in Box 6.
boxes[6].remove('guitar')
boxes[6].remove('speaker')
boxes[6].remove('grinder')
boxes[6].append('rain')
boxes[6].append('fish')
boxes[6].append('shark')

# Remove the lion and the frame from Box 3.
boxes[3].remove('lion')
boxes[3].remove('frame')

# Put the wallet and the skirt and the planet into Box 6.
boxes[6].append('wallet')
boxes[6].append('skirt')
boxes[6].append('planet')

# Swap the flute in Box 5 with the tree in Box 8.
boxes[5].remove('flute')
boxes[8].remove('tree')
boxes[5].append('tree')
boxes[8].append('flute')

# Swap the skirt in Box 6 with the wig in Box 1.
boxes[6].remove('skirt')
boxes[1].remove('wig')
boxes[6].append('wig')
boxes[1].append('skirt')

# Replace the skirt with the key in Box 1.
boxes[1].remove('skirt')
boxes[1].append('key')

# Swap the flute in Box 8 with the river in Box 1.
boxes[8].remove('flute')
boxes[1].remove('river')
boxes[8].append('river')
boxes[1].append('flute')

# Move the river from Box 8 to Box 7.
boxes[8].remove('river')
boxes[7].append('river')

# Empty Box 4.
boxes[4] = []

# Replace the meteor with the harmonica in Box 9.
boxes[9].remove('meteor')
boxes[9].append('harmonica')

# Put the candle into Box 2.
boxes[2].append('candle')

# Put the pants into Box 2.
boxes[2].append('pants')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")