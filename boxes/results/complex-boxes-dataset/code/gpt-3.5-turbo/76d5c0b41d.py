# Initial state of boxes
boxes = {
    0: ['usb', 'bell', 'sculpture', 'telescope'],
    1: ['guitar', 'phone', 'cat', 'cup'],
    2: ['bag', 'jungle', 'mountain'],
    3: ['leaf'],
    4: ['tie', 'book'],
    5: ['island', 'toaster'],
    6: ['umbrella', 'zipper', 'polish', 'violin']
}

# Replace the book with the shark in Box 4.
boxes[4].remove('book')
boxes[4].append('shark')

# Move the toaster from Box 5 to Box 0.
boxes[5].remove('toaster')
boxes[0].append('toaster')

# Move the violin and the umbrella from Box 6 to Box 2.
boxes[6].remove('violin')
boxes[6].remove('umbrella')
boxes[2].append('violin')
boxes[2].append('umbrella')

# Replace the zipper with the blanket in Box 6.
boxes[6].remove('zipper')
boxes[6].append('blanket')

# Put the toothbrush and the jacket into Box 3.
boxes[3].append('toothbrush')
boxes[3].append('jacket')

# Move the guitar and the cup and the cat from Box 1 to Box 5.
items_to_move = ['guitar', 'cup', 'cat']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Move the shark from Box 4 to Box 5.
boxes[4].remove('shark')
boxes[5].append('shark')

# Put the coral and the paint and the ring into Box 4.
items_to_put = ['coral', 'paint', 'ring']
for item in items_to_put:
    boxes[4].append(item)

# Move the polish from Box 6 to Box 4.
boxes[6].remove('polish')
boxes[4].append('polish')

# Put the flute into Box 0.
boxes[0].append('flute')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")