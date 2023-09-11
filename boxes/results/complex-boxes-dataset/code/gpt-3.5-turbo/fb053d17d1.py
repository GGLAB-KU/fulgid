# Initial state of boxes
boxes = {
    0: ['shoes'],
    1: ['scissors', 'wig', 'bell', 'truck', 'meteor'],
    2: ['belt', 'horn'],
    3: ['camera', 'usb'],
    4: ['bus'],
    5: ['forest', 'flower', 'dice'],
    6: ['harmonica'],
    7: ['dress'],
    8: ['candle', 'spoon', 'skirt', 'toothpaste', 'note']
}

# Remove the horn from Box 2.
boxes[2].remove('horn')

# Replace the belt with the snow in Box 2.
boxes[2].remove('belt')
boxes[2].append('snow')

# Put the elephant and the grinder into Box 8.
boxes[8].append('elephant')
boxes[8].append('grinder')

# Swap the flower in Box 5 with the toothpaste in Box 8.
boxes[5].remove('flower')
boxes[8].remove('toothpaste')
boxes[5].append('toothpaste')
boxes[8].append('flower')

# Replace the bus with the crown in Box 4.
boxes[4].remove('bus')
boxes[4].append('crown')

# Replace the dress with the doll in Box 7.
boxes[7].remove('dress')
boxes[7].append('doll')

# Put the chair and the vase into Box 4.
boxes[4].append('chair')
boxes[4].append('vase')

# Move the harmonica from Box 6 to Box 1.
boxes[6].remove('harmonica')
boxes[1].append('harmonica')

# Remove the spoon from Box 8.
boxes[8].remove('spoon')

# Remove the grinder and the flower and the elephant from Box 8.
items_to_remove = ['grinder', 'flower', 'elephant']
for item in items_to_remove:
    boxes[8].remove(item)

# Empty Box 2.
boxes[2] = []

# Put the bracelet and the keyboard and the sock into Box 2.
boxes[2].append('bracelet')
boxes[2].append('keyboard')
boxes[2].append('sock')

# Replace the crown and the chair with the coat and the shelf in Box 4.
boxes[4].remove('crown')
boxes[4].remove('chair')
boxes[4].append('coat')
boxes[4].append('shelf')

# Put the leaf and the grass into Box 0.
boxes[0].append('leaf')
boxes[0].append('grass')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")