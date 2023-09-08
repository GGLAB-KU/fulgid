# Initial state of boxes
boxes = {
    0: ['wallet', 'wire'],
    1: ['zipper', 'soap', 'wig', 'blender', 'brush'],
    2: [],
    3: ['grass', 'table', 'tape', 'shark', 'swimsuit'],
    4: ['chair', 'puzzle', 'pillow'],
    5: ['card', 'elephant', 'candle', 'shampoo'],
    6: ['flute', 'belt', 'coin'],
    7: ['cow', 'horse']
}

# Swap the wig in Box 1 with the chair in Box 4.
boxes[1].remove('wig')
boxes[4].remove('chair')
boxes[1].append('chair')
boxes[4].append('wig')

# Put the dress and the pan into Box 6.
boxes[6].append('dress')
boxes[6].append('pan')

# Put the book and the plate into Box 1.
boxes[1].append('book')
boxes[1].append('plate')

# Swap the cow in Box 7 with the table in Box 3.
boxes[7].remove('cow')
boxes[3].remove('table')
boxes[7].append('table')
boxes[3].append('cow')

# Put the motorcycle into Box 3.
boxes[3].append('motorcycle')

# Move the horse from Box 7 to Box 5.
boxes[7].remove('horse')
boxes[5].append('horse')

# Remove the card and the elephant and the candle from Box 5.
boxes[5].remove('card')
boxes[5].remove('elephant')
boxes[5].remove('candle')

# Replace the horse with the horn in Box 5.
boxes[5].remove('horse')
boxes[5].append('horn')

# Remove the tape and the cow from Box 3.
boxes[3].remove('tape')
boxes[3].remove('cow')

# Swap the shark in Box 3 with the table in Box 7.
boxes[3].remove('shark')
boxes[7].remove('table')
boxes[3].append('table')
boxes[7].append('shark')

# Put the boot and the flower and the river into Box 7.
boxes[7].append('boot')
boxes[7].append('flower')
boxes[7].append('river')

# Move the shampoo and the horn from Box 5 to Box 6.
boxes[5].remove('shampoo')
boxes[5].remove('horn')
boxes[6].append('shampoo')
boxes[6].append('horn')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")