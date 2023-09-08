# Initial state of boxes
boxes = {
    0: ['sandals', 'clock'],
    1: [],
    2: ['doll', 'oven', 'mask'],
    3: ['key', 'dog', 'shorts', 'shampoo'],
    4: [],
    5: ['lamp'],
    6: ['glove'],
    7: ['horse', 'toothbrush', 'tie'],
    8: ['guitar', 'boot', 'charger', 'candle'],
    9: ['headphone', 'lightning', 'spoon', 'dice'],
    10: ['camera', 'laptop', 'helmet']
}

# Move the spoon from Box 9 to Box 10.
boxes[9].remove('spoon')
boxes[10].append('spoon')

# Move the clock and the sandals from Box 0 to Box 10.
boxes[0].remove('clock')
boxes[0].remove('sandals')
boxes[10].append('clock')
boxes[10].append('sandals')

# Replace the lamp with the sock in Box 5.
boxes[5].remove('lamp')
boxes[5].append('sock')

# Remove the tie and the toothbrush from Box 7.
boxes[7].remove('tie')
boxes[7].remove('toothbrush')

# Move the horse from Box 7 to Box 3.
boxes[7].remove('horse')
boxes[3].append('horse')

# Empty Box 5.
boxes[5] = []

# Remove the doll and the mask and the oven from Box 2.
boxes[2].remove('doll')
boxes[2].remove('mask')
boxes[2].remove('oven')

# Put the basket and the toaster into Box 2.
boxes[2].append('basket')
boxes[2].append('toaster')

# Remove the toaster and the basket from Box 2.
boxes[2].remove('toaster')
boxes[2].remove('basket')

# Put the console and the mixer into Box 7.
boxes[7].append('console')
boxes[7].append('mixer')

# Move the dice from Box 9 to Box 1.
boxes[9].remove('dice')
boxes[1].append('dice')

# Move the shorts and the horse from Box 3 to Box 7.
boxes[3].remove('shorts')
boxes[3].remove('horse')
boxes[7].append('shorts')
boxes[7].append('horse')

# Put the piano and the button into Box 0.
boxes[0].append('piano')
boxes[0].append('button')

# Move the dog and the shampoo and the key from Box 3 to Box 9.
boxes[3].remove('dog')
boxes[3].remove('shampoo')
boxes[3].remove('key')
boxes[9].append('dog')
boxes[9].append('shampoo')
boxes[9].append('key')

# Put the cat and the book into Box 4.
boxes[4].append('cat')
boxes[4].append('book')

# Put the polish into Box 7.
boxes[7].append('polish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")