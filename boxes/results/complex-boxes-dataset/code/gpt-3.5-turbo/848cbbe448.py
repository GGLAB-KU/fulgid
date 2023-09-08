# Initial state of boxes
boxes = {
    0: ['rain'],
    1: ['toy'],
    2: [],
    3: ['boat', 'thunder', 'bag', 'polish'],
    4: ['fork', 'pillow'],
    5: ['wig', 'glasses', 'flower'],
    6: []
}

# Remove the toy from Box 1.
boxes[1].remove('toy')

# Put the puzzle and the paint and the train into Box 5.
boxes[5].append('puzzle')
boxes[5].append('paint')
boxes[5].append('train')

# Put the guitar and the card into Box 1.
boxes[1].append('guitar')
boxes[1].append('card')

# Put the phone and the submarine and the thread into Box 4.
boxes[4].append('phone')
boxes[4].append('submarine')
boxes[4].append('thread')

# Replace the card and the guitar with the chair and the shirt in Box 1.
boxes[1].remove('card')
boxes[1].remove('guitar')
boxes[1].append('chair')
boxes[1].append('shirt')

# Remove the wig from Box 5.
boxes[5].remove('wig')

# Empty Box 4.
boxes[4] = []

# Move the train and the flower and the paint from Box 5 to Box 0.
items_to_move = ['train', 'flower', 'paint']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[0].append(item)

# Remove the chair and the shirt from Box 1.
boxes[1].remove('chair')
boxes[1].remove('shirt')

# Swap the bag in Box 3 with the glasses in Box 5.
boxes[3].remove('bag')
boxes[5].remove('glasses')
boxes[3].append('glasses')
boxes[5].append('bag')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")