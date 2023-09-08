# Initial state of boxes
boxes = {
    0: ['tiger', 'car', 'dice', 'microscope'],
    1: [],
    2: ['sun', 'motorcycle', 'ring', 'gloves', 'bear'],
    3: ['coat'],
    4: ['key', 'glove'],
    5: ['tie'],
    6: [],
    7: [],
    8: ['dolphin'],
    9: ['frame', 'grinder', 'basket'],
    10: ['mirror', 'zipper', 'phone', 'jacket', 'toothpaste']
}

# Put the elephant and the lock into Box 4.
boxes[4].append('elephant')
boxes[4].append('lock')

# Remove the coat from Box 3.
boxes[3].remove('coat')

# Remove the tie from Box 5.
boxes[5].remove('tie')

# Move the frame and the basket from Box 9 to Box 3.
items_to_move = ['frame', 'basket']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[3].append(item)

# Swap the grinder in Box 9 with the dolphin in Box 8.
boxes[9].remove('grinder')
boxes[8].remove('dolphin')
boxes[9].append('dolphin')
boxes[8].append('grinder')

# Move the dolphin from Box 9 to Box 3.
boxes[9].remove('dolphin')
boxes[3].append('dolphin')

# Move the elephant and the lock and the key from Box 4 to Box 1.
items_to_move = ['elephant', 'lock', 'key']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[1].append(item)

# Replace the glove with the ring in Box 4.
boxes[4].remove('glove')
boxes[4].append('ring')

# Remove the lock from Box 1.
boxes[1].remove('lock')

# Swap the grinder in Box 8 with the motorcycle in Box 2.
boxes[8].remove('grinder')
boxes[2].remove('motorcycle')
boxes[8].append('motorcycle')
boxes[2].append('grinder')

# Remove the grinder and the sun and the ring from Box 2.
items_to_remove = ['grinder', 'sun', 'ring']
for item in items_to_remove:
    boxes[2].remove(item)

# Swap the motorcycle in Box 8 with the car in Box 0.
boxes[8].remove('motorcycle')
boxes[0].remove('car')
boxes[8].append('car')
boxes[0].append('motorcycle')

# Move the zipper and the jacket and the toothpaste from Box 10 to Box 2.
items_to_move = ['zipper', 'jacket', 'toothpaste']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[2].append(item)

# Move the car from Box 8 to Box 2.
boxes[8].remove('car')
boxes[2].append('car')

# Remove the mirror and the phone from Box 10.
items_to_remove = ['mirror', 'phone']
for item in items_to_remove:
    boxes[10].remove(item)

# Swap the dolphin in Box 3 with the ring in Box 4.
boxes[3].remove('dolphin')
boxes[4].remove('ring')
boxes[3].append('ring')
boxes[4].append('dolphin')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")