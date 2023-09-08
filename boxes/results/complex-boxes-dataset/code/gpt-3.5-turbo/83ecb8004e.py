# Initial state of boxes
boxes = {
    0: ['wire', 'console', 'pillow', 'book'],
    1: [],
    2: ['controller', 'blender', 'cup', 'storm', 'gloves'],
    3: ['spoon', 'necklace'],
    4: ['camera', 'mixer'],
    5: ['flower', 'blanket', 'butterfly', 'pot', 'crown'],
    6: [],
    7: ['shampoo', 'jungle', 'scissors', 'shelf', 'skirt']
}

# Remove the flower and the pot and the crown from Box 5.
items_to_remove = ['flower', 'pot', 'crown']
for item in items_to_remove:
    boxes[5].remove(item)

# Move the shelf and the skirt from Box 7 to Box 2.
items_to_move = ['shelf', 'skirt']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[2].append(item)

# Swap the pillow in Box 0 with the necklace in Box 3.
boxes[0].remove('pillow')
boxes[3].remove('necklace')
boxes[0].append('necklace')
boxes[3].append('pillow')

# Move the camera from Box 4 to Box 5.
boxes[4].remove('camera')
boxes[5].append('camera')

# Replace the mixer with the island in Box 4.
boxes[4].remove('mixer')
boxes[4].append('island')

# Move the scissors and the jungle and the shampoo from Box 7 to Box 5.
items_to_move = ['scissors', 'jungle', 'shampoo']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[5].append(item)

# Move the book from Box 0 to Box 2.
boxes[0].remove('book')
boxes[2].append('book')

# Swap the island in Box 4 with the necklace in Box 0.
boxes[4].remove('island')
boxes[0].remove('necklace')
boxes[4].append('necklace')
boxes[0].append('island')

# Empty Box 3.
boxes[3] = []

# Move the necklace from Box 4 to Box 3.
boxes[4].remove('necklace')
boxes[3].append('necklace')

# Replace the necklace with the violin in Box 3.
boxes[3].remove('necklace')
boxes[3].append('violin')

# Move the controller and the blender from Box 2 to Box 1.
items_to_move = ['controller', 'blender']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")