# Initial state of boxes
boxes = {
    0: ['bracelet', 'frame', 'horse', 'blanket'],
    1: ['note', 'coat', 'book', 'sculpture', 'wig'],
    2: [],
    3: [],
    4: ['bag', 'vase', 'bus', 'motorcycle'],
    5: [],
    6: ['crown', 'dog'],
    7: [],
    8: ['sandals', 'grass', 'pen', 'boat', 'train']
}

# Put the rock and the coral into Box 0.
boxes[0].append('rock')
boxes[0].append('coral')

# Replace the bag with the glove in Box 4.
boxes[4].remove('bag')
boxes[4].append('glove')

# Remove the vase from Box 4.
boxes[4].remove('vase')

# Move the coral and the bracelet and the blanket from Box 0 to Box 5.
items_to_move = ['coral', 'bracelet', 'blanket']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Swap the dog in Box 6 with the glove in Box 4.
boxes[6].remove('dog')
boxes[4].remove('glove')
boxes[6].append('glove')
boxes[4].append('dog')

# Put the dice and the motorcycle into Box 0.
boxes[0].append('dice')
boxes[0].append('motorcycle')

# Replace the glove with the magnet in Box 6.
boxes[6].remove('glove')
boxes[6].append('magnet')

# Replace the bus and the motorcycle and the dog with the truck and the toaster and the butterfly in Box 4.
boxes[4].remove('bus')
boxes[4].remove('motorcycle')
boxes[4].remove('dog')
boxes[4].append('truck')
boxes[4].append('toaster')
boxes[4].append('butterfly')

# Put the frame into Box 3.
boxes[3].append('frame')

# Put the zipper and the magnet and the umbrella into Box 1.
boxes[1].append('zipper')
boxes[1].append('magnet')
boxes[1].append('umbrella')

# Put the magnet and the necklace into Box 8.
boxes[8].append('magnet')
boxes[8].append('necklace')

# Replace the frame with the lock in Box 3.
boxes[3].remove('frame')
boxes[3].append('lock')

# Put the motorcycle into Box 1.
boxes[1].append('motorcycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")