# Initial state of boxes
boxes = {
    0: ['tape'],
    1: [],
    2: ['controller'],
    3: [],
    4: ['headphone'],
    5: ['toaster', 'toy', 'grass'],
    6: ['blanket', 'moon', 'mask'],
    7: ['umbrella', 'sun', 'forest', 'thunder'],
    8: ['book', 'flute', 'helmet', 'ocean', 'cat'],
    9: ['desert', 'pants'],
    10: ['hat', 'card'],
    11: ['coin', 'drum', 'telescope', 'fridge', 'spoon'],
    12: []
}

# Put the polish into Box 8.
boxes[8].append('polish')

# Put the jacket and the frame and the sculpture into Box 8.
boxes[8].extend(['jacket', 'frame', 'sculpture'])

# Remove the frame and the ocean and the flute from Box 8.
boxes[8].remove('frame')
boxes[8].remove('ocean')
boxes[8].remove('flute')

# Put the star into Box 12.
boxes[12].append('star')

# Remove the tape from Box 0.
boxes[0].remove('tape')

# Move the star from Box 12 to Box 6.
boxes[12].remove('star')
boxes[6].append('star')

# Remove the controller from Box 2.
boxes[2].remove('controller')

# Move the desert from Box 9 to Box 4.
boxes[9].remove('desert')
boxes[4].append('desert')

# Put the speaker and the razor into Box 7.
boxes[7].extend(['speaker', 'razor'])

# Remove the razor from Box 7.
boxes[7].remove('razor')

# Move the pants from Box 9 to Box 5.
boxes[9].remove('pants')
boxes[5].append('pants')

# Remove the hat and the card from Box 10.
boxes[10].remove('hat')
boxes[10].remove('card')

# Move the mask from Box 6 to Box 5.
boxes[6].remove('mask')
boxes[5].append('mask')

# Move the headphone and the desert from Box 4 to Box 7.
boxes[4].remove('headphone')
boxes[9].remove('desert')
boxes[7].extend(['headphone', 'desert'])

# Empty Box 6.
boxes[6] = []

# Remove the spoon and the drum from Box 11.
boxes[11].remove('spoon')
boxes[11].remove('drum')

# Move the book from Box 8 to Box 12.
boxes[8].remove('book')
boxes[12].append('book')

# Put the butterfly and the drum and the boat into Box 5.
boxes[5].extend(['butterfly', 'drum', 'boat'])

# Remove the fridge and the coin and the telescope from Box 11.
boxes[11].remove('fridge')
boxes[11].remove('coin')
boxes[11].remove('telescope')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")