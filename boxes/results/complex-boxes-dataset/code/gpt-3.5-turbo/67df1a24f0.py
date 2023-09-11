# Initial state of boxes
boxes = {
    0: ['polish', 'tape', 'elephant', 'mirror'],
    1: ['desert', 'headphone', 'bag', 'sock', 'branch'],
    2: ['violin', 'dress', 'dog', 'cloud', 'toaster'],
    3: ['sculpture']
}

# Remove the mirror and the polish from Box 0.
boxes[0].remove('mirror')
boxes[0].remove('polish')

# Swap the dress in Box 2 with the sculpture in Box 3.
boxes[2].remove('dress')
boxes[3].remove('sculpture')
boxes[2].append('sculpture')
boxes[3].append('dress')

# Put the cat into Box 2.
boxes[2].append('cat')

# Remove the tape from Box 0.
boxes[0].remove('tape')

# Put the wallet into Box 1.
boxes[1].append('wallet')

# Move the cat and the sculpture from Box 2 to Box 0.
items_to_move = ['cat', 'sculpture']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")