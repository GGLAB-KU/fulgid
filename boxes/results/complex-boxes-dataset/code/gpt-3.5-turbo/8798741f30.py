# Initial state of boxes
boxes = {
    0: ['rock', 'shark', 'boot', 'cat', 'fish'],
    1: ['tape', 'sculpture', 'pan'],
    2: ['wallet', 'pants', 'controller'],
    3: ['snow', 'necklace', 'leaf'],
    4: ['microwave', 'motorcycle', 'watch', 'submarine']
}

# Put the jungle and the dog into Box 3.
boxes[3].append('jungle')
boxes[3].append('dog')

# Remove the fish from Box 0.
boxes[0].remove('fish')

# Put the makeup and the dog and the lamp into Box 1.
boxes[1].append('makeup')
boxes[1].append('dog')
boxes[1].append('lamp')

# Remove the jungle and the leaf from Box 3.
boxes[3].remove('jungle')
boxes[3].remove('leaf')

# Move the cat and the shark and the rock from Box 0 to Box 1.
items_to_move = ['cat', 'shark', 'rock']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Put the swimsuit and the spoon and the harmonica into Box 2.
items_to_put = ['swimsuit', 'spoon', 'harmonica']
for item in items_to_put:
    boxes[2].append(item)

# Move the motorcycle and the watch and the microwave from Box 4 to Box 1.
items_to_move = ['motorcycle', 'watch', 'microwave']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")