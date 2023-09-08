# Initial state of boxes
boxes = {
    0: ['river', 'plane', 'lipstick', 'whistle', 'tree'],
    1: [],
    2: ['polish', 'forest', 'pants', 'storm'],
    3: ['comb'],
    4: ['battery'],
    5: [],
    6: ['cow', 'shorts', 'seaweed', 'toy', 'jacket'],
    7: ['makeup', 'wire', 'spoon', 'book', 'shoe'],
    8: ['bicycle', 'wallet', 'flower', 'train', 'vase'],
    9: ['magnet'],
    10: ['sandals', 'grinder', 'comet', 'grass']
}

# Empty Box 8.
boxes[8] = []

# Remove the shorts and the toy and the jacket from Box 6.
items_to_remove = ['shorts', 'toy', 'jacket']
for item in items_to_remove:
    boxes[6].remove(item)

# Remove the wire from Box 7.
boxes[7].remove('wire')

# Remove the comet from Box 10.
boxes[10].remove('comet')

# Move the whistle from Box 0 to Box 2.
boxes[0].remove('whistle')
boxes[2].append('whistle')

# Swap the spoon in Box 7 with the whistle in Box 2.
boxes[7].remove('spoon')
boxes[2].remove('whistle')
boxes[7].append('whistle')
boxes[2].append('spoon')

# Swap the spoon in Box 2 with the battery in Box 4.
boxes[2].remove('spoon')
boxes[4].remove('battery')
boxes[2].append('battery')
boxes[4].append('spoon')

# Move the storm from Box 2 to Box 4.
boxes[2].remove('storm')
boxes[4].append('storm')

# Move the whistle and the book from Box 7 to Box 8.
boxes[7].remove('whistle')
boxes[7].remove('book')
boxes[8].append('whistle')
boxes[8].append('book')

# Swap the pants in Box 2 with the book in Box 8.
boxes[2].remove('pants')
boxes[8].remove('book')
boxes[2].append('book')
boxes[8].append('pants')

# Remove the storm from Box 4.
boxes[4].remove('storm')

# Move the spoon from Box 4 to Box 0.
boxes[4].remove('spoon')
boxes[0].append('spoon')

# Move the pants and the whistle from Box 8 to Box 10.
boxes[8].remove('pants')
boxes[8].remove('whistle')
boxes[10].append('pants')
boxes[10].append('whistle')

# Put the lightning and the polish into Box 9.
boxes[9].append('lightning')
boxes[2].remove('polish')
boxes[9].append('polish')

# Move the grass from Box 10 to Box 6.
boxes[10].remove('grass')
boxes[6].append('grass')

# Move the shoe from Box 7 to Box 4.
boxes[7].remove('shoe')
boxes[4].append('shoe')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")