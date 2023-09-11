# Initial state of boxes
boxes = {
    0: ['train', 'usb', 'makeup', 'cat', 'toy'],
    1: ['desert', 'mirror', 'necklace', 'zipper', 'book'],
    2: ['pot'],
    3: [],
    4: ['mountain', 'bicycle', 'puzzle'],
    5: ['coin', 'violin', 'pants', 'swimsuit'],
    6: []
}

# Move the cat from Box 0 to Box 2.
boxes[0].remove('cat')
boxes[2].append('cat')

# Empty Box 2.
boxes[2] = []

# Move the mountain from Box 4 to Box 6.
boxes[4].remove('mountain')
boxes[6].append('mountain')

# Replace the train and the toy and the makeup with the polish and the meteor and the comet in Box 0.
boxes[0].remove('train')
boxes[0].remove('toy')
boxes[0].remove('makeup')
boxes[0].append('polish')
boxes[0].append('meteor')
boxes[0].append('comet')

# Replace the book and the mirror and the zipper with the toaster and the makeup and the sandals in Box 1.
boxes[1].remove('book')
boxes[1].remove('mirror')
boxes[1].remove('zipper')
boxes[1].append('toaster')
boxes[1].append('makeup')
boxes[1].append('sandals')

# Put the paint and the hat and the beach into Box 3.
boxes[3].append('paint')
boxes[3].append('hat')
boxes[3].append('beach')

# Swap the beach in Box 3 with the usb in Box 0.
boxes[3].remove('beach')
boxes[0].remove('usb')
boxes[3].append('usb')
boxes[0].append('beach')

# Move the meteor and the polish from Box 0 to Box 1.
boxes[0].remove('meteor')
boxes[0].remove('polish')
boxes[1].append('meteor')
boxes[1].append('polish')

# Put the lion into Box 5.
boxes[5].append('lion')

# Swap the hat in Box 3 with the beach in Box 0.
boxes[3].remove('hat')
boxes[0].remove('beach')
boxes[3].append('beach')
boxes[0].append('hat')

# Empty Box 6.
boxes[6] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")