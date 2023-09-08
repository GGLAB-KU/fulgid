# Initial state of boxes
boxes = {
    0: ['necklace', 'truck', 'thread', 'car'],
    1: ['mirror', 'pan', 'doll', 'toaster'],
    2: ['tape', 'candle', 'gloves', 'mask'],
    3: ['island', 'sock', 'speaker', 'flower', 'boot'],
    4: []
}

# Empty Box 0
boxes[0] = []

# Swap the tape in Box 2 with the doll in Box 1
boxes[2].remove('tape')
boxes[1].remove('doll')
boxes[2].append('doll')
boxes[1].append('tape')

# Remove the pan from Box 1
boxes[1].remove('pan')

# Empty Box 3
boxes[3] = []

# Remove the candle and the doll and the gloves from Box 2
items_to_remove = ['candle', 'doll', 'gloves']
for item in items_to_remove:
    boxes[2].remove(item)

# Remove the toaster and the mirror and the tape from Box 1
items_to_remove = ['toaster', 'mirror', 'tape']
for item in items_to_remove:
    boxes[1].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")