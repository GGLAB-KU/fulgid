# Initial state of boxes
boxes = {
    0: ['sandals', 'glove', 'battery', 'ring', 'lion'],
    1: [],
    2: [],
    3: ['toaster'],
    4: ['scissors'],
    5: ['doll', 'flower', 'bell', 'toy'],
    6: ['game'],
    7: ['horse', 'wallet', 'toothpaste'],
    8: ['candle', 'magnet'],
    9: [],
    10: ['river', 'chair']
}

# Swap the scissors in Box 4 with the game in Box 6.
boxes[4].remove('scissors')
boxes[6].remove('game')
boxes[4].append('game')
boxes[6].append('scissors')

# Swap the scissors in Box 6 with the horse in Box 7.
boxes[6].remove('scissors')
boxes[7].remove('horse')
boxes[6].append('horse')
boxes[7].append('scissors')

# Replace the ring and the glove with the moon and the scissors in Box 0.
boxes[0].remove('ring')
boxes[0].remove('glove')
boxes[0].append('moon')
boxes[0].append('scissors')

# Swap the game in Box 4 with the horse in Box 6.
boxes[4].remove('game')
boxes[6].remove('horse')
boxes[4].append('horse')
boxes[6].append('game')

# Move the candle from Box 8 to Box 2.
boxes[8].remove('candle')
boxes[2].append('candle')

# Move the game from Box 6 to Box 2.
boxes[6].remove('game')
boxes[2].append('game')

# Put the speaker into Box 1.
boxes[1].append('speaker')

# Remove the toy and the bell and the doll from Box 5.
items_to_remove = ['toy', 'bell', 'doll']
for item in items_to_remove:
    boxes[5].remove(item)

# Put the rock and the harmonica into Box 3.
boxes[3].append('rock')
boxes[3].append('harmonica')

# Swap the magnet in Box 8 with the speaker in Box 1.
boxes[8].remove('magnet')
boxes[1].remove('speaker')
boxes[8].append('speaker')
boxes[1].append('magnet')

# Move the flower from Box 5 to Box 1.
boxes[5].remove('flower')
boxes[1].append('flower')

# Move the candle from Box 2 to Box 9.
boxes[2].remove('candle')
boxes[9].append('candle')

# Replace the flower with the note in Box 1.
boxes[1].remove('flower')
boxes[1].append('note')

# Put the starfish and the bag into Box 4.
boxes[4].append('starfish')
boxes[4].append('bag')

# Swap the note in Box 1 with the harmonica in Box 3.
boxes[1].remove('note')
boxes[3].remove('harmonica')
boxes[1].append('harmonica')
boxes[3].append('note')

# Empty Box 9.
boxes[9] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")