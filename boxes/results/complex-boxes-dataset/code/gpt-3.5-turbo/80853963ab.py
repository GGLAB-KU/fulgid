# Initial state of boxes
boxes = {
    0: ['jungle', 'submarine', 'sandals'],
    1: ['bear', 'usb', 'card', 'sock'],
    2: ['motorcycle', 'bird'],
    3: ['swimsuit'],
    4: ['zipper'],
    5: ['sun', 'mountain', 'razor'],
    6: ['tiger'],
    7: ['bus', 'fork', 'butterfly'],
    8: ['soap', 'meteor', 'lipstick', 'toaster', 'guitar'],
    9: ['oven']
}

# Put the meteor and the comet and the soap into Box 4.
boxes[4].extend(['meteor', 'comet', 'soap'])

# Put the cow into Box 9.
boxes[9].append('cow')

# Remove the bus and the fork and the butterfly from Box 7.
boxes[7].remove('bus')
boxes[7].remove('fork')
boxes[7].remove('butterfly')

# Remove the comet from Box 4.
boxes[4].remove('comet')

# Remove the toaster from Box 8.
boxes[8].remove('toaster')

# Move the submarine and the jungle and the sandals from Box 0 to Box 4.
items_to_move = ['submarine', 'jungle', 'sandals']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Put the belt and the harmonica and the pot into Box 1.
boxes[1].extend(['belt', 'harmonica', 'pot'])

# Remove the swimsuit from Box 3.
boxes[3].remove('swimsuit')

# Move the meteor and the zipper and the jungle from Box 4 to Box 7.
items_to_move = ['meteor', 'zipper', 'jungle']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[7].append(item)

# Swap the sun in Box 5 with the oven in Box 9.
boxes[5].remove('sun')
boxes[9].remove('oven')
boxes[5].append('oven')
boxes[9].append('sun')

# Move the sandals and the submarine from Box 4 to Box 0.
items_to_move = ['sandals', 'submarine']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Move the lipstick from Box 8 to Box 7.
boxes[8].remove('lipstick')
boxes[7].append('lipstick')

# Empty Box 5.
boxes[5] = []

# Move the meteor from Box 7 to Box 0.
boxes[7].remove('meteor')
boxes[0].append('meteor')

# Move the usb and the harmonica and the belt from Box 1 to Box 6.
items_to_move = ['usb', 'harmonica', 'belt']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[6].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")