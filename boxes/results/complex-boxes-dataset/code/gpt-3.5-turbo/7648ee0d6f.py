# Initial state of boxes
boxes = {
    0: [],
    1: ['swimsuit'],
    2: [],
    3: [],
    4: ['motorcycle', 'river', 'grinder'],
    5: ['car', 'tape', 'rocket', 'violin', 'book'],
    6: ['sock', 'shelf', 'tiger', 'grass', 'cow']
}

# Put the flute and the crown into Box 4.
boxes[4].append('flute')
boxes[4].append('crown')

# Remove the swimsuit from Box 1.
boxes[1].remove('swimsuit')

# Move the book and the tape from Box 5 to Box 4.
items_to_move = ['book', 'tape']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Swap the violin in Box 5 with the shelf in Box 6.
boxes[5].remove('violin')
boxes[6].remove('shelf')
boxes[5].append('shelf')
boxes[6].append('violin')

# Replace the tiger with the pot in Box 6.
boxes[6].remove('tiger')
boxes[6].append('pot')

# Put the coral into Box 4.
boxes[4].append('coral')

# Move the cow and the pot and the sock from Box 6 to Box 5.
items_to_move = ['cow', 'pot', 'sock']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[5].append(item)

# Swap the motorcycle in Box 4 with the shelf in Box 5.
boxes[4].remove('motorcycle')
boxes[5].remove('shelf')
boxes[4].append('shelf')
boxes[5].append('motorcycle')

# Remove the book and the grinder and the crown from Box 4.
items_to_remove = ['book', 'grinder', 'crown']
for item in items_to_remove:
    boxes[4].remove(item)

# Put the bracelet into Box 0.
boxes[0].append('bracelet')

# Remove the pot and the motorcycle from Box 5.
items_to_remove = ['pot', 'motorcycle']
for item in items_to_remove:
    boxes[5].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")