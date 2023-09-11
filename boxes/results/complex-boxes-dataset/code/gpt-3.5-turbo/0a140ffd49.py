# Initial state of boxes
boxes = {
    0: ['microscope'],
    1: [],
    2: ['fork', 'car'],
    3: ['whistle', 'watch'],
    4: ['jacket']
}

# Remove the car from Box 2.
boxes[2].remove('car')

# Replace the fork with the butterfly in Box 2.
boxes[2].remove('fork')
boxes[2].append('butterfly')

# Move the jacket from Box 4 to Box 1.
boxes[4].remove('jacket')
boxes[1].append('jacket')

# Put the blender and the dog and the crown into Box 3.
items_to_add = ['blender', 'dog', 'crown']
for item in items_to_add:
    boxes[3].append(item)

# Put the rain and the thunder into Box 4.
items_to_add = ['rain', 'thunder']
for item in items_to_add:
    boxes[4].append(item)

# Move the jacket from Box 1 to Box 2.
boxes[1].remove('jacket')
boxes[2].append('jacket')

# Move the rain and the thunder from Box 4 to Box 0.
items_to_move = ['rain', 'thunder']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Put the flute and the skirt and the scarf into Box 4.
items_to_add = ['flute', 'skirt', 'scarf']
for item in items_to_add:
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")