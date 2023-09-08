# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: [],
    3: ['tape', 'button', 'game', 'swimsuit', 'comb'],
    4: ['bus', 'island']
}

# Remove the island from Box 4.
boxes[4].remove('island')

# Swap the bus in Box 4 with the button in Box 3.
boxes[4].remove('bus')
boxes[3].remove('button')
boxes[4].append('button')
boxes[3].append('bus')

# Remove the game from Box 3.
boxes[3].remove('game')

# Move the tape and the bus from Box 3 to Box 4.
boxes[3].remove('tape')
boxes[3].remove('bus')
boxes[4].append('tape')
boxes[4].append('bus')

# Remove the comb and the swimsuit from Box 3.
boxes[3].remove('comb')
boxes[3].remove('swimsuit')

# Put the apple and the drum and the planet into Box 1.
items_to_move = ['apple', 'drum', 'planet']
for item in items_to_move:
    boxes[1].append(item)

# Remove the planet from Box 1.
boxes[1].remove('planet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")