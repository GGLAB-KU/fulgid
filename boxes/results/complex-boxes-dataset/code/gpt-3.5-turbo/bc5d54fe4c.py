# Initial state of boxes
boxes = {
    0: ['pants', 'lock', 'river', 'glasses', 'horse'],
    1: ['button', 'puzzle', 'earring', 'dress', 'camera'],
    2: ['paint'],
    3: ['flower', 'necklace', 'toothpaste', 'shelf', 'microscope']
}

# Move the river and the lock and the horse from Box 0 to Box 3.
items_to_move = ['river', 'lock', 'horse']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Swap the puzzle in Box 1 with the river in Box 3.
boxes[1].remove('puzzle')
boxes[3].remove('river')
boxes[1].append('river')
boxes[3].append('puzzle')

# Put the hat and the makeup into Box 0.
boxes[0].append('hat')
boxes[0].append('makeup')

# Swap the lock in Box 3 with the glasses in Box 0.
boxes[3].remove('lock')
boxes[0].remove('glasses')
boxes[3].append('glasses')
boxes[0].append('lock')

# Move the shelf and the flower from Box 3 to Box 1.
items_to_move = ['shelf', 'flower']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Swap the paint in Box 2 with the glasses in Box 3.
boxes[2].remove('paint')
boxes[3].remove('glasses')
boxes[2].append('glasses')
boxes[3].append('paint')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")