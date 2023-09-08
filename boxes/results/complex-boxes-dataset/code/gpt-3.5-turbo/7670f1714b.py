# Initial state of boxes
boxes = {
    0: ['shelf', 'blanket', 'controller', 'drum'],
    1: ['coral', 'tape', 'star'],
    2: ['oven', 'coin', 'polish', 'boat', 'thread'],
    3: [],
    4: [],
    5: ['bag']
}

# Swap the thread in Box 2 with the drum in Box 0.
boxes[0].remove('drum')
boxes[2].remove('thread')
boxes[0].append('thread')
boxes[2].append('drum')

# Move the polish and the oven from Box 2 to Box 5.
items_to_move = ['polish', 'oven']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Remove the thread and the shelf from Box 0.
boxes[0].remove('thread')
boxes[0].remove('shelf')

# Replace the drum and the boat and the coin with the scissors and the train and the cat in Box 2.
boxes[2].remove('drum')
boxes[2].remove('boat')
boxes[2].remove('coin')
boxes[2].append('scissors')
boxes[2].append('train')
boxes[2].append('cat')

# Swap the polish in Box 5 with the blanket in Box 0.
boxes[0].remove('blanket')
boxes[5].remove('polish')
boxes[0].append('polish')
boxes[5].append('blanket')

# Put the car and the paint into Box 4.
boxes[4].append('car')
boxes[4].append('paint')

# Move the paint and the car from Box 4 to Box 2.
items_to_move = ['paint', 'car']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Replace the cat with the shoes in Box 2.
boxes[2].remove('cat')
boxes[2].append('shoes')

# Move the coral and the star and the tape from Box 1 to Box 2.
items_to_move = ['coral', 'star', 'tape']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")