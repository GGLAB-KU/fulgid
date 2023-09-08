# Initial state of boxes
boxes = {
    0: [],
    1: ['belt', 'pan', 'mirror'],
    2: ['branch', 'guitar'],
    3: ['skirt', 'pillow', 'butterfly', 'shirt'],
    4: ['leaf']
}

# Swap the pillow in Box 3 with the leaf in Box 4.
boxes[3].remove('pillow')
boxes[4].remove('leaf')
boxes[3].append('leaf')
boxes[4].append('pillow')

# Put the sculpture and the horn and the umbrella into Box 1.
items_to_move = ['sculpture', 'horn', 'umbrella']
for item in items_to_move:
    boxes[1].append(item)

# Swap the pillow in Box 4 with the shirt in Box 3.
boxes[4].remove('pillow')
boxes[3].remove('shirt')
boxes[4].append('shirt')
boxes[3].append('pillow')

# Replace the shirt with the toothpaste in Box 4.
boxes[4].remove('shirt')
boxes[4].append('toothpaste')

# Move the butterfly and the leaf and the pillow from Box 3 to Box 4.
items_to_move = ['butterfly', 'leaf', 'pillow']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[4].append(item)

# Replace the skirt with the boot in Box 3.
boxes[3].remove('skirt')
boxes[3].append('boot')

# Empty Box 4.
boxes[4] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")