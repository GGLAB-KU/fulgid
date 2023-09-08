# Initial state of boxes
boxes = {
    0: [],
    1: ['mountain', 'zipper', 'rain'],
    2: ['piano', 'comb', 'river'],
    3: [],
    4: ['leaf', 'charger', 'submarine'],
    5: ['console', 'lamp'],
    6: ['freezer']
}

# Put the scissors and the basket and the harmonica into Box 3.
items_to_put = ['scissors', 'basket', 'harmonica']
for item in items_to_put:
    boxes[3].append(item)

# Empty Box 2.
boxes[2] = []

# Swap the lamp in Box 5 with the rain in Box 1.
boxes[1].remove('rain')
boxes[5].remove('lamp')
boxes[1].append('lamp')
boxes[5].append('rain')

# Move the rain and the console from Box 5 to Box 3.
items_to_move = ['rain', 'console']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[3].append(item)

# Move the charger and the submarine and the leaf from Box 4 to Box 2.
items_to_move = ['charger', 'submarine', 'leaf']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Remove the mountain and the lamp from Box 1.
boxes[1].remove('mountain')
boxes[1].remove('lamp')

# Swap the charger in Box 2 with the zipper in Box 1.
boxes[1].remove('zipper')
boxes[2].remove('charger')
boxes[1].append('charger')
boxes[2].append('zipper')

# Move the submarine and the zipper from Box 2 to Box 3.
boxes[2].remove('submarine')
boxes[2].remove('zipper')
boxes[3].append('submarine')
boxes[3].append('zipper')

# Put the shorts into Box 5.
boxes[5].append('shorts')

# Swap the freezer in Box 6 with the leaf in Box 2.
boxes[2].remove('leaf')
boxes[6].remove('freezer')
boxes[2].append('freezer')
boxes[6].append('leaf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")