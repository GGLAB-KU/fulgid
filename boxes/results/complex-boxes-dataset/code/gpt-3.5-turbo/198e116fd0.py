# Initial state of boxes
boxes = {
    0: ['bicycle', 'apple'],
    1: [],
    2: ['mirror', 'plane', 'guitar', 'train', 'bracelet'],
    3: [],
    4: ['river'],
    5: ['game', 'motorcycle', 'bus', 'book', 'desert'],
    6: ['coat', 'ring'],
    7: ['toothpaste'],
    8: ['headphone', 'sock'],
    9: ['shoes', 'flute'],
    10: [],
    11: ['snow']
}

# Swap the snow in Box 11 with the bicycle in Box 0.
boxes[11].remove('snow')
boxes[0].remove('bicycle')
boxes[11].append('bicycle')
boxes[0].append('snow')

# Swap the river in Box 4 with the flute in Box 9.
boxes[4].remove('river')
boxes[9].remove('flute')
boxes[4].append('flute')
boxes[9].append('river')

# Move the snow from Box 0 to Box 8.
boxes[0].remove('snow')
boxes[8].append('snow')

# Remove the bicycle from Box 11.
boxes[11].remove('bicycle')

# Remove the sock from Box 8.
boxes[8].remove('sock')

# Remove the motorcycle from Box 5.
boxes[5].remove('motorcycle')

# Move the apple from Box 0 to Box 5.
boxes[0].remove('apple')
boxes[5].append('apple')

# Move the game and the apple from Box 5 to Box 4.
boxes[5].remove('game')
boxes[5].remove('apple')
boxes[4].append('game')
boxes[4].append('apple')

# Remove the book from Box 5.
boxes[5].remove('book')

# Move the bus and the desert from Box 5 to Box 8.
boxes[5].remove('bus')
boxes[5].remove('desert')
boxes[8].append('bus')
boxes[8].append('desert')

# Swap the snow in Box 8 with the game in Box 4.
boxes[8].remove('snow')
boxes[4].remove('game')
boxes[8].append('game')
boxes[4].append('snow')

# Replace the shoes and the river with the piano and the table in Box 9.
boxes[9].remove('shoes')
boxes[9].remove('river')
boxes[9].append('piano')
boxes[9].append('table')

# Swap the desert in Box 8 with the mirror in Box 2.
boxes[8].remove('desert')
boxes[2].remove('mirror')
boxes[8].append('mirror')
boxes[2].append('desert')

# Move the coat and the ring from Box 6 to Box 1.
boxes[6].remove('coat')
boxes[6].remove('ring')
boxes[1].append('coat')
boxes[1].append('ring')

# Swap the desert in Box 2 with the game in Box 8.
boxes[2].remove('desert')
boxes[8].remove('game')
boxes[2].append('game')
boxes[8].append('desert')

# Swap the ring in Box 1 with the toothpaste in Box 7.
boxes[1].remove('ring')
boxes[7].remove('toothpaste')
boxes[1].append('toothpaste')
boxes[7].append('ring')

# Remove the game and the train from Box 2.
boxes[2].remove('game')
boxes[2].remove('train')

# Swap the ring in Box 7 with the desert in Box 8.
boxes[7].remove('ring')
boxes[8].remove('desert')
boxes[7].append('desert')
boxes[8].append('ring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")