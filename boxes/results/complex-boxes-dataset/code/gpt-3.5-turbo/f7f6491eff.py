# Initial state of boxes
boxes = {
    0: ['console'],
    1: ['starfish', 'hat', 'bicycle'],
    2: [],
    3: ['comb', 'candle', 'perfume', 'star'],
    4: ['makeup', 'desert', 'puzzle', 'apple', 'cat'],
    5: [],
    6: ['crown', 'meteor', 'dice'],
    7: ['keyboard', 'telescope', 'dress', 'mirror', 'guitar'],
    8: ['shark', 'doll', 'bowl', 'shirt', 'earring'],
    9: ['piano', 'car'],
    10: ['ring', 'shorts', 'bear']
}

# Put the mixer into Box 2.
boxes[2].append('mixer')

# Empty Box 6.
boxes[6] = []

# Replace the makeup with the brush in Box 4.
boxes[4].remove('makeup')
boxes[4].append('brush')

# Swap the desert in Box 4 with the guitar in Box 7.
boxes[4].remove('desert')
boxes[7].remove('guitar')
boxes[4].append('guitar')
boxes[7].append('desert')

# Swap the console in Box 0 with the starfish in Box 1.
boxes[0].remove('console')
boxes[1].remove('starfish')
boxes[0].append('starfish')
boxes[1].append('console')

# Move the mixer from Box 2 to Box 1.
boxes[2].remove('mixer')
boxes[1].append('mixer')

# Replace the keyboard with the ring in Box 7.
boxes[7].remove('keyboard')
boxes[7].append('ring')

# Move the puzzle and the guitar from Box 4 to Box 9.
boxes[4].remove('puzzle')
boxes[4].remove('guitar')
boxes[9].append('puzzle')
boxes[9].append('guitar')

# Move the brush and the cat from Box 4 to Box 6.
boxes[4].remove('brush')
boxes[4].remove('cat')
boxes[6].append('brush')
boxes[6].append('cat')

# Remove the brush from Box 6.
boxes[6].remove('brush')

# Replace the candle with the sun in Box 3.
boxes[3].remove('candle')
boxes[3].append('sun')

# Remove the dress and the desert and the telescope from Box 7.
boxes[7].remove('dress')
boxes[7].remove('desert')
boxes[7].remove('telescope')

# Move the starfish from Box 0 to Box 7.
boxes[0].remove('starfish')
boxes[7].append('starfish')

# Move the star from Box 3 to Box 10.
boxes[3].remove('star')
boxes[10].append('star')

# Replace the starfish and the ring with the headphone and the cow in Box 7.
boxes[7].remove('starfish')
boxes[7].remove('ring')
boxes[7].append('headphone')
boxes[7].append('cow')

# Move the ring and the star and the bear from Box 10 to Box 1.
boxes[10].remove('ring')
boxes[10].remove('star')
boxes[10].remove('bear')
boxes[1].append('ring')
boxes[1].append('star')
boxes[1].append('bear')

# Empty Box 7.
boxes[7] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")