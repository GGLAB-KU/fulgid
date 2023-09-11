# Initial state of boxes
boxes = {
    0: ['candle', 'bear', 'beach', 'lipstick', 'boat'],
    1: ['phone', 'wire'],
    2: ['oven', 'coat'],
    3: ['card', 'jacket'],
    4: ['toothbrush', 'flute', 'river', 'guitar'],
    5: ['frame', 'coral', 'scarf'],
    6: ['shelf'],
    7: ['microscope'],
    8: ['flower', 'table', 'watch', 'grinder', 'tiger'],
    9: ['planet'],
    10: []
}

# Remove the guitar and the flute and the river from Box 4.
boxes[4].remove('guitar')
boxes[4].remove('flute')
boxes[4].remove('river')

# Empty Box 8.
boxes[8] = []

# Remove the candle and the lipstick from Box 0.
boxes[0].remove('candle')
boxes[0].remove('lipstick')

# Replace the toothbrush with the brush in Box 4.
boxes[4].remove('toothbrush')
boxes[4].append('brush')

# Remove the shelf from Box 6.
boxes[6].remove('shelf')

# Swap the bear in Box 0 with the planet in Box 9.
boxes[0].remove('bear')
boxes[9].remove('planet')
boxes[0].append('planet')
boxes[9].append('bear')

# Move the phone from Box 1 to Box 0.
boxes[1].remove('phone')
boxes[0].append('phone')

# Remove the bear from Box 9.
boxes[9].remove('bear')

# Swap the coral in Box 5 with the wire in Box 1.
boxes[5].remove('coral')
boxes[1].remove('wire')
boxes[5].append('wire')
boxes[1].append('coral')

# Remove the jacket from Box 3.
boxes[3].remove('jacket')

# Remove the card from Box 3.
boxes[3].remove('card')

# Remove the coral from Box 1.
boxes[1].remove('coral')

# Remove the brush from Box 4.
boxes[4].remove('brush')

# Replace the scarf and the frame with the toaster and the comet in Box 5.
boxes[5].remove('scarf')
boxes[5].remove('frame')
boxes[5].append('toaster')
boxes[5].append('comet')

# Remove the boat from Box 0.
boxes[0].remove('boat')

# Move the phone and the beach from Box 0 to Box 2.
boxes[0].remove('phone')
boxes[0].remove('beach')
boxes[2].append('phone')
boxes[2].append('beach')

# Empty Box 2.
boxes[2] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")