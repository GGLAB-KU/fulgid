# Initial state of boxes
boxes = {
    0: ['hat', 'dog', 'puzzle', 'horn', 'soap'],
    1: ['flower', 'swimsuit', 'watch'],
    2: ['star', 'tape', 'river', 'freezer'],
    3: [],
    4: ['elephant', 'bear', 'jacket', 'lightning', 'tiger'],
    5: ['frame', 'dress', 'rock'],
    6: ['boat'],
    7: ['toy', 'toaster'],
    8: ['book', 'violin', 'wallet', 'spoon', 'forest'],
    9: ['submarine', 'bell', 'island', 'basket', 'mirror'],
    10: ['headphone']
}

# Swap the violin in Box 8 with the hat in Box 0.
boxes[0].remove('hat')
boxes[8].remove('violin')
boxes[0].append('violin')
boxes[8].append('hat')

# Move the spoon and the book from Box 8 to Box 3.
items_to_move = ['spoon', 'book']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[3].append(item)

# Move the spoon from Box 3 to Box 10.
boxes[3].remove('spoon')
boxes[10].append('spoon')

# Remove the mirror from Box 9.
boxes[9].remove('mirror')

# Empty Box 10.
boxes[10] = []

# Move the elephant and the bear and the lightning from Box 4 to Box 7.
items_to_move = ['elephant', 'bear', 'lightning']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[7].append(item)

# Put the drum into Box 3.
boxes[3].append('drum')

# Swap the drum in Box 3 with the boat in Box 6.
boxes[3].remove('drum')
boxes[6].remove('boat')
boxes[3].append('boat')
boxes[6].append('drum')

# Swap the dress in Box 5 with the swimsuit in Box 1.
boxes[1].remove('swimsuit')
boxes[5].remove('dress')
boxes[1].append('dress')
boxes[5].append('swimsuit')

# Replace the elephant and the lightning with the mountain and the scarf in Box 7.
boxes[7].remove('elephant')
boxes[7].remove('lightning')
boxes[7].append('mountain')
boxes[7].append('scarf')

# Move the dress and the watch from Box 1 to Box 3.
items_to_move = ['dress', 'watch']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Remove the tiger and the jacket from Box 4.
boxes[4].remove('tiger')
boxes[4].remove('jacket')

# Move the watch and the dress and the book from Box 3 to Box 8.
items_to_move = ['watch', 'dress', 'book']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[8].append(item)

# Replace the boat with the shark in Box 3.
boxes[3].remove('boat')
boxes[3].append('shark')

# Swap the drum in Box 6 with the wallet in Box 8.
boxes[6].remove('drum')
boxes[8].remove('wallet')
boxes[6].append('wallet')
boxes[8].append('drum')

# Move the toy from Box 7 to Box 4.
boxes[7].remove('toy')
boxes[4].append('toy')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")