# Initial state of boxes
boxes = {
    0: ['butterfly', 'shoes', 'shark'],
    1: ['tie', 'note', 'towel', 'thread'],
    2: ['doll', 'telescope', 'necklace', 'violin'],
    3: ['mask', 'whistle', 'shelf', 'boat'],
    4: [],
    5: ['lipstick', 'chair', 'watch'],
    6: [],
    7: ['flute', 'cup'],
    8: ['phone', 'submarine', 'beach'],
    9: ['rain'],
    10: ['swimsuit', 'polish'],
    11: ['candle', 'table', 'glove', 'island'],
    12: ['rocket', 'elephant', 'razor', 'speaker', 'umbrella'],
    13: ['zipper', 'needle'],
    14: []
}

# Replace the needle with the toothpaste in Box 13.
boxes[13].remove('needle')
boxes[13].append('toothpaste')

# Swap the flute in Box 7 with the shark in Box 0.
boxes[7].remove('flute')
boxes[0].remove('shark')
boxes[7].append('shark')
boxes[0].append('flute')

# Move the towel from Box 1 to Box 5.
boxes[1].remove('towel')
boxes[5].append('towel')

# Move the tie and the note and the thread from Box 1 to Box 2.
items_to_move = ['tie', 'note', 'thread']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Put the bracelet and the sculpture into Box 6.
boxes[6].append('bracelet')
boxes[6].append('sculpture')

# Swap the umbrella in Box 12 with the sculpture in Box 6.
boxes[12].remove('umbrella')
boxes[6].remove('sculpture')
boxes[12].append('sculpture')
boxes[6].append('umbrella')

# Swap the towel in Box 5 with the umbrella in Box 6.
boxes[5].remove('towel')
boxes[6].remove('umbrella')
boxes[5].append('umbrella')
boxes[6].append('towel')

# Move the shoes and the flute from Box 0 to Box 9.
items_to_move = ['shoes', 'flute']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[9].append(item)

# Replace the watch with the camera in Box 5.
boxes[5].remove('watch')
boxes[5].append('camera')

# Move the glove from Box 11 to Box 12.
boxes[11].remove('glove')
boxes[12].append('glove')

# Move the table and the candle from Box 11 to Box 5.
items_to_move = ['table', 'candle']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[5].append(item)

# Swap the cup in Box 7 with the island in Box 11.
boxes[7].remove('cup')
boxes[11].remove('island')
boxes[7].append('island')
boxes[11].append('cup')

# Remove the cup from Box 11.
boxes[11].remove('cup')

# Empty Box 0.
boxes[0] = []

# Replace the zipper and the toothpaste with the tree and the spoon in Box 13.
boxes[13].remove('zipper')
boxes[13].remove('toothpaste')
boxes[13].append('tree')
boxes[13].append('spoon')

# Move the chair and the umbrella from Box 5 to Box 1.
items_to_move = ['chair', 'umbrella']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[1].append(item)

# Put the flower and the mirror into Box 1.
boxes[1].append('flower')
boxes[1].append('mirror')

# Remove the swimsuit and the polish from Box 10.
boxes[10].remove('swimsuit')
boxes[10].remove('polish')

# Swap the shark in Box 7 with the flute in Box 9.
boxes[7].remove('shark')
boxes[9].remove('flute')
boxes[7].append('flute')
boxes[9].append('shark')

# Put the tape and the planet into Box 8.
boxes[8].append('tape')
boxes[8].append('planet')

# Empty Box 13.
boxes[13] = []

# Swap the flute in Box 7 with the rain in Box 9.
boxes[7].remove('flute')
boxes[9].remove('rain')
boxes[7].append('rain')
boxes[9].append('flute')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")