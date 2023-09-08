# Initial state of boxes
boxes = {
    0: ['fish', 'whistle', 'submarine', 'train'],
    1: ['bird'],
    2: [],
    3: ['sun', 'harmonica'],
    4: ['beach'],
    5: ['boat', 'candle'],
    6: ['sock']
}

# Put the hat and the bird into Box 5.
boxes[5].append('hat')
boxes[5].append('bird')

# Move the whistle from Box 0 to Box 4.
boxes[0].remove('whistle')
boxes[4].append('whistle')

# Put the shark into Box 3.
boxes[3].append('shark')

# Put the scarf and the submarine and the branch into Box 5.
boxes[5].append('scarf')
boxes[5].append('submarine')
boxes[5].append('branch')

# Put the bicycle and the microwave into Box 4.
boxes[4].append('bicycle')
boxes[4].append('microwave')

# Put the star and the flute into Box 3.
boxes[3].append('star')
boxes[3].append('flute')

# Move the sun from Box 3 to Box 2.
boxes[3].remove('sun')
boxes[2].append('sun')

# Put the horn and the planet into Box 2.
boxes[2].append('horn')
boxes[2].append('planet')

# Empty Box 2.
boxes[2] = []

# Swap the bird in Box 1 with the boat in Box 5.
boxes[1].remove('bird')
boxes[5].remove('boat')
boxes[1].append('boat')
boxes[5].append('bird')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")