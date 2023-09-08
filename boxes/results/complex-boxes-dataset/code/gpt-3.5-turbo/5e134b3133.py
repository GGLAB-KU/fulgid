# Initial state of boxes
boxes = {
    0: ['phone', 'wig', 'sculpture', 'shampoo', 'whistle'],
    1: ['moon', 'snow', 'leaf', 'soap', 'dolphin'],
    2: ['rock', 'coral'],
    3: ['train', 'flute', 'cup', 'candle', 'grinder'],
    4: [],
    5: ['brush', 'lightning', 'note', 'planet'],
    6: ['cow', 'grass', 'sandals', 'swimsuit'],
    7: ['toy', 'dog', 'thread']
}

# Put the starfish into Box 4.
boxes[4].append('starfish')

# Remove the starfish from Box 4.
boxes[4].remove('starfish')

# Remove the cup and the train and the grinder from Box 3.
items_to_remove = ['cup', 'train', 'grinder']
for item in items_to_remove:
    boxes[3].remove(item)

# Swap the rock in Box 2 with the candle in Box 3.
boxes[2].remove('rock')
boxes[3].remove('candle')
boxes[2].append('candle')
boxes[3].append('rock')

# Remove the thread and the toy from Box 7.
boxes[7].remove('thread')
boxes[7].remove('toy')

# Remove the whistle from Box 0.
boxes[0].remove('whistle')

# Put the frame and the book into Box 1.
boxes[1].append('frame')
boxes[1].append('book')

# Move the lightning from Box 5 to Box 3.
boxes[5].remove('lightning')
boxes[3].append('lightning')

# Move the brush and the note and the planet from Box 5 to Box 6.
items_to_move = ['brush', 'note', 'planet']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[6].append(item)

# Replace the leaf with the tape in Box 1.
boxes[1].remove('leaf')
boxes[1].append('tape')

# Put the glasses and the game into Box 4.
boxes[4].append('glasses')
boxes[4].append('game')

# Swap the dog in Box 7 with the snow in Box 1.
boxes[7].remove('dog')
boxes[1].remove('snow')
boxes[7].append('snow')
boxes[1].append('dog')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")