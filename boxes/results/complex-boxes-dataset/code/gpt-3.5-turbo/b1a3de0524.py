# Initial state of boxes
boxes = {
    0: ['bowl', 'comb', 'shoes'],
    1: ['starfish'],
    2: ['elephant', 'clock', 'horn', 'planet', 'thread'],
    3: ['blanket']
}

# Empty Box 0
boxes[0] = []

# Swap the blanket in Box 3 with the starfish in Box 1.
boxes[1].remove('starfish')
boxes[3].remove('blanket')
boxes[1].append('blanket')
boxes[3].append('starfish')

# Remove the planet and the thread and the horn from Box 2.
items_to_remove = ['planet', 'thread', 'horn']
for item in items_to_remove:
    boxes[2].remove(item)

# Put the cow and the note and the game into Box 3.
items_to_add = ['cow', 'note', 'game']
for item in items_to_add:
    boxes[3].append(item)

# Swap the note in Box 3 with the blanket in Box 1.
boxes[1].remove('blanket')
boxes[3].remove('note')
boxes[1].append('note')
boxes[3].append('blanket')

# Remove the clock from Box 2.
boxes[2].remove('clock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")