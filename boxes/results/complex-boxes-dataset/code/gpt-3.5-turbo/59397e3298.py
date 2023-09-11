# Initial state of boxes
boxes = {
    0: [],
    1: ['lion'],
    2: [],
    3: ['pen', 'keyboard', 'coat'],
    4: [],
    5: ['watch', 'battery', 'spoon'],
    6: ['sock', 'coin', 'grass', 'table'],
    7: ['console', 'laptop', 'thread'],
    8: [],
    9: ['tie'],
    10: [],
    11: [],
    12: ['lock', 'ship', 'candle']
}

# Move the tie from Box 9 to Box 2.
boxes[9].remove('tie')
boxes[2].append('tie')

# Put the candle and the jungle into Box 11.
boxes[11].append('candle')
boxes[11].append('jungle')

# Replace the grass and the sock with the doll and the ring in Box 6.
boxes[6].remove('grass')
boxes[6].remove('sock')
boxes[6].append('doll')
boxes[6].append('ring')

# Empty Box 12.
boxes[12] = []

# Put the mask and the candle into Box 12.
boxes[12].append('mask')
boxes[12].append('candle')

# Remove the spoon and the battery and the watch from Box 5.
boxes[5].remove('spoon')
boxes[5].remove('battery')
boxes[5].remove('watch')

# Remove the candle from Box 12.
boxes[12].remove('candle')

# Replace the doll and the coin with the perfume and the jungle in Box 6.
boxes[6].remove('doll')
boxes[6].remove('coin')
boxes[6].append('perfume')
boxes[6].append('jungle')

# Remove the lion from Box 1.
boxes[1].remove('lion')

# Move the mask from Box 12 to Box 3.
boxes[12].remove('mask')
boxes[3].append('mask')

# Empty Box 3.
boxes[3] = []

# Replace the jungle with the train in Box 11.
boxes[11].remove('jungle')
boxes[11].append('train')

# Move the table and the perfume and the ring from Box 6 to Box 1.
items_to_move = ['table', 'perfume', 'ring']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[1].append(item)

# Put the dice into Box 9.
boxes[9].append('dice')

# Swap the train in Box 11 with the laptop in Box 7.
boxes[11].remove('train')
boxes[7].remove('laptop')
boxes[11].append('laptop')
boxes[7].append('train')

# Put the key and the helmet and the candle into Box 4.
boxes[4].append('key')
boxes[4].append('helmet')
boxes[4].append('candle')

# Move the key from Box 4 to Box 2.
boxes[4].remove('key')
boxes[2].append('key')

# Move the candle from Box 4 to Box 8.
boxes[4].remove('candle')
boxes[8].append('candle')

# Move the table and the ring and the perfume from Box 1 to Box 10.
items_to_move = ['table', 'ring', 'perfume']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[10].append(item)

# Move the laptop from Box 11 to Box 7.
boxes[11].remove('laptop')
boxes[7].append('laptop')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")