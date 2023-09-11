# Initial state of boxes
boxes = {
    0: ['jungle', 'violin'],
    1: ['flute', 'oven'],
    2: ['telescope'],
    3: ['key', 'tape', 'plate', 'laptop'],
    4: ['lamp', 'star', 'apple'],
    5: ['butterfly', 'boot', 'comb', 'island'],
    6: ['river', 'freezer', 'magnet', 'bowl']
}

# Swap the comb in Box 5 with the oven in Box 1.
boxes[1].remove('oven')
boxes[5].remove('comb')
boxes[1].append('comb')
boxes[5].append('oven')

# Swap the bowl in Box 6 with the jungle in Box 0.
boxes[0].remove('jungle')
boxes[6].remove('bowl')
boxes[0].append('bowl')
boxes[6].append('jungle')

# Put the car into Box 4.
boxes[4].append('car')

# Replace the violin and the bowl with the star and the frame in Box 0.
boxes[0].remove('violin')
boxes[0].remove('bowl')
boxes[0].append('star')
boxes[0].append('frame')

# Swap the star in Box 0 with the freezer in Box 6.
boxes[0].remove('star')
boxes[6].remove('freezer')
boxes[0].append('freezer')
boxes[6].append('star')

# Empty Box 0.
boxes[0] = []

# Move the jungle and the star from Box 6 to Box 4.
items_to_move = ['jungle', 'star']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[4].append(item)

# Move the plate and the tape and the laptop from Box 3 to Box 4.
items_to_move = ['plate', 'tape', 'laptop']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[4].append(item)

# Move the key from Box 3 to Box 6.
boxes[3].remove('key')
boxes[6].append('key')

# Move the car from Box 4 to Box 1.
boxes[4].remove('car')
boxes[1].append('car')

# Move the star and the jungle and the star from Box 4 to Box 6.
items_to_move = ['star', 'jungle', 'star']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[6].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")