# Initial state of boxes
boxes = {
    0: ['coral', 'cow', 'moon'],
    1: ['doll', 'grinder'],
    2: ['lipstick'],
    3: [],
    4: ['soap', 'keyboard', 'train', 'paint', 'toothpaste']
}

# Put the hat and the starfish and the game into Box 1.
items_to_add = ['hat', 'starfish', 'game']
for item in items_to_add:
    boxes[1].append(item)

# Remove the lipstick from Box 2.
boxes[2].remove('lipstick')

# Move the game from Box 1 to Box 0.
boxes[0].append(boxes[1].pop(boxes[1].index('game')))

# Put the speaker into Box 1.
boxes[1].append('speaker')

# Put the oven and the rain and the comb into Box 1.
items_to_add = ['oven', 'rain', 'comb']
for item in items_to_add:
    boxes[1].append(item)

# Empty Box 0.
boxes[0] = []

# Replace the speaker and the oven with the ocean and the note in Box 1.
boxes[1].remove('speaker')
boxes[1].remove('oven')
boxes[1].append('ocean')
boxes[1].append('note')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")