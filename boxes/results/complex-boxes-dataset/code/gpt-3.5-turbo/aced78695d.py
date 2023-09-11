# Initial state of boxes
boxes = {
    0: ['card'],
    1: ['note', 'chair', 'sock'],
    2: ['truck', 'ring', 'dog', 'thread', 'horse'],
    3: ['starfish', 'polish'],
    4: ['perfume', 'keyboard', 'shampoo']
}

# Replace the polish with the bowl in Box 3.
boxes[3].remove('polish')
boxes[3].append('bowl')

# Replace the bowl with the blender in Box 3.
boxes[3].remove('bowl')
boxes[3].append('blender')

# Put the brush and the dolphin and the bell into Box 3.
boxes[3].extend(['brush', 'dolphin', 'bell'])

# Remove the shampoo and the keyboard and the perfume from Box 4.
items_to_remove = ['shampoo', 'keyboard', 'perfume']
for item in items_to_remove:
    boxes[4].remove(item)

# Move the dog and the truck from Box 2 to Box 4.
items_to_move = ['dog', 'truck']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[4].append(item)

# Replace the sock and the chair and the note with the rock and the branch and the dice in Box 1.
items_to_remove = ['sock', 'chair', 'note']
items_to_add = ['rock', 'branch', 'dice']
for item in items_to_remove:
    boxes[1].remove(item)
for item in items_to_add:
    boxes[1].append(item)

# Remove the thread and the horse and the ring from Box 2.
items_to_remove = ['thread', 'horse', 'ring']
for item in items_to_remove:
    boxes[2].remove(item)

# Put the oven and the card into Box 2.
boxes[2].extend(['oven', 'card'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")