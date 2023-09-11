# Initial state of boxes
boxes = {
    0: ['keyboard'],
    1: [],
    2: ['mirror', 'shark', 'watch'],
    3: ['sun', 'scissors', 'needle'],
    4: ['ocean', 'pants', 'fork', 'bag'],
    5: ['towel', 'island', 'fridge', 'lion', 'mountain'],
    6: ['bird', 'cloud', 'perfume'],
    7: ['grinder'],
    8: ['tiger', 'toothbrush', 'controller'],
    9: ['swimsuit', 'tape', 'comet', 'lock', 'note'],
    10: ['game']
}

# Move the fork and the ocean and the bag from Box 4 to Box 3.
items_to_move = ['fork', 'ocean', 'bag']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Remove the perfume and the bird and the cloud from Box 6.
items_to_remove = ['perfume', 'bird', 'cloud']
for item in items_to_remove:
    boxes[6].remove(item)

# Remove the toothbrush and the tiger from Box 8.
items_to_remove = ['toothbrush', 'tiger']
for item in items_to_remove:
    boxes[8].remove(item)

# Put the basket into Box 6.
boxes[6].append('basket')

# Replace the keyboard with the rain in Box 0.
boxes[0].remove('keyboard')
boxes[0].append('rain')

# Remove the needle and the ocean from Box 3.
items_to_remove = ['needle', 'ocean']
for item in items_to_remove:
    boxes[3].remove(item)

# Swap the grinder in Box 7 with the scissors in Box 3.
boxes[7], boxes[3] = boxes[3], boxes[7]

# Put the elephant and the bicycle into Box 7.
boxes[7].append('elephant')
boxes[7].append('bicycle')

# Put the skirt and the towel and the magnet into Box 0.
items_to_move = ['skirt', 'towel', 'magnet']
for item in items_to_move:
    boxes[0].append(item)

# Move the swimsuit and the note and the comet from Box 9 to Box 4.
items_to_move = ['swimsuit', 'note', 'comet']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[4].append(item)

# Swap the sun in Box 3 with the elephant in Box 7.
boxes[3], boxes[7] = boxes[7], boxes[3]

# Swap the scissors in Box 7 with the island in Box 5.
boxes[7], boxes[5] = boxes[5], boxes[7]

# Move the island and the bicycle from Box 7 to Box 4.
items_to_move = ['island', 'bicycle']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[4].append(item)

# Put the coin into Box 2.
boxes[2].append('coin')

# Move the controller from Box 8 to Box 1.
boxes[8].remove('controller')
boxes[1].append('controller')

# Put the grass into Box 0.
boxes[0].append('grass')

# Move the bag from Box 3 to Box 10.
boxes[3].remove('bag')
boxes[10].append('bag')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")