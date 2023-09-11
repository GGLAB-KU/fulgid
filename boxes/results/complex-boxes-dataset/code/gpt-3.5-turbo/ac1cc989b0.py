# Initial state of boxes
boxes = {
    0: ['comet'],
    1: ['glasses'],
    2: ['shoes', 'phone'],
    3: ['wallet'],
    4: ['glove', 'motorcycle', 'shorts', 'bell', 'frame']
}

# Swap the wallet in Box 3 with the glasses in Box 1.
boxes[3].remove('wallet')
boxes[1].remove('glasses')
boxes[3].append('glasses')
boxes[1].append('wallet')

# Move the glasses from Box 3 to Box 1.
boxes[3].remove('glasses')
boxes[1].append('glasses')

# Put the dog and the button and the battery into Box 4.
items_to_put = ['dog', 'button', 'battery']
for item in items_to_put:
    boxes[4].append(item)

# Put the rocket into Box 4.
boxes[4].append('rocket')

# Remove the button from Box 4.
boxes[4].remove('button')

# Put the paint and the pot into Box 4.
items_to_put = ['paint', 'pot']
for item in items_to_put:
    boxes[4].append(item)

# Put the thunder into Box 4.
boxes[4].append('thunder')

# Move the comet from Box 0 to Box 4.
boxes[0].remove('comet')
boxes[4].append('comet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")