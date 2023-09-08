# Initial state of boxes
boxes = {
    0: ['spoon', 'rocket', 'fish', 'plate'],
    1: ['zipper'],
    2: ['bird'],
    3: ['ocean', 'belt', 'star', 'island', 'flower'],
    4: ['dice', 'coat', 'drum']
}

# Remove the star and the island and the belt from Box 3.
items_to_remove = ['star', 'island', 'belt']
for item in items_to_remove:
    boxes[3].remove(item)

# Move the dice and the drum from Box 4 to Box 2.
items_to_move = ['dice', 'drum']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Put the charger and the blanket and the tape into Box 3.
items_to_add = ['charger', 'blanket', 'tape']
for item in items_to_add:
    boxes[3].append(item)

# Remove the ocean from Box 3.
boxes[3].remove('ocean')

# Replace the zipper with the charger in Box 1.
boxes[1].remove('zipper')
boxes[1].append('charger')

# Empty Box 1.
boxes[1] = []

# Remove the blanket from Box 3.
boxes[3].remove('blanket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")