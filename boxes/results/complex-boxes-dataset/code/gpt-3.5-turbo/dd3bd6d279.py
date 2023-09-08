# Initial state of boxes
boxes = {
    0: ['grass', 'leaf', 'makeup', 'razor', 'comet'],
    1: [],
    2: ['storm', 'console', 'butterfly', 'table', 'perfume'],
    3: ['rain'],
    4: []
}

# Swap the rain in Box 3 with the makeup in Box 0.
boxes[0].remove('makeup')
boxes[3].remove('rain')
boxes[0].append('rain')
boxes[3].append('makeup')

# Swap the perfume in Box 2 with the makeup in Box 3.
boxes[2].remove('perfume')
boxes[3].remove('makeup')
boxes[2].append('makeup')
boxes[3].append('perfume')

# Move the console and the makeup and the storm from Box 2 to Box 1.
items_to_move = ['console', 'makeup', 'storm']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Move the rain and the grass from Box 0 to Box 2.
items_to_move = ['rain', 'grass']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Remove the razor from Box 0.
boxes[0].remove('razor')

# Swap the perfume in Box 3 with the leaf in Box 0.
boxes[0].remove('leaf')
boxes[3].remove('perfume')
boxes[0].append('perfume')
boxes[3].append('leaf')

# Move the leaf from Box 3 to Box 1.
boxes[3].remove('leaf')
boxes[1].append('leaf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")