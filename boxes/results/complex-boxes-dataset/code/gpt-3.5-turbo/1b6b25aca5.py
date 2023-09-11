# Initial state of boxes
boxes = {
    0: ['fridge', 'spoon', 'ocean', 'freezer'],
    1: ['blender', 'snow', 'game', 'dress'],
    2: ['card', 'sculpture', 'laptop'],
    3: ['wire', 'note', 'bicycle']
}

# Put the chair and the tie into Box 0.
boxes[0].append('chair')
boxes[0].append('tie')

# Move the dress and the blender and the snow from Box 1 to Box 0.
items_to_move = ['dress', 'blender', 'snow']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[0].append(item)

# Remove the dress and the ocean and the snow from Box 0.
items_to_remove = ['dress', 'ocean', 'snow']
for item in items_to_remove:
    boxes[0].remove(item)

# Swap the game in Box 1 with the note in Box 3.
boxes[1].remove('game')
boxes[3].remove('note')
boxes[1].append('note')
boxes[3].append('game')

# Swap the wire in Box 3 with the freezer in Box 0.
boxes[3].remove('wire')
boxes[0].remove('freezer')
boxes[3].append('freezer')
boxes[0].append('wire')

# Put the plate and the chair and the battery into Box 3.
boxes[3].append('plate')
boxes[3].append('chair')
boxes[3].append('battery')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")