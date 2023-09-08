# Initial state of boxes
boxes = {
    0: ['thunder', 'bird', 'note'],
    1: ['necklace', 'earring'],
    2: ['book', 'rock', 'watch', 'blender', 'bear'],
    3: ['vase', 'bicycle'],
    4: ['chair', 'drum', 'forest', 'mask'],
    5: ['charger', 'motorcycle'],
    6: ['clock', 'pillow', 'octopus', 'magnet'],
    7: ['cup', 'tree', 'candle'],
    8: ['hat', 'toothpaste', 'bell', 'polish', 'game']
}

# Swap the thunder in Box 0 with the toothpaste in Box 8.
boxes[0].remove('thunder')
boxes[8].remove('toothpaste')
boxes[0].append('toothpaste')
boxes[8].append('thunder')

# Move the motorcycle and the charger from Box 5 to Box 8.
items_to_move = ['motorcycle', 'charger']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[8].append(item)

# Put the shoes and the thunder and the thread into Box 2.
items_to_put = ['shoes', 'thunder', 'thread']
for item in items_to_put:
    boxes[2].append(item)

# Move the clock and the pillow from Box 6 to Box 1.
items_to_move = ['clock', 'pillow']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[1].append(item)

# Put the swimsuit and the lock into Box 1.
items_to_put = ['swimsuit', 'lock']
for item in items_to_put:
    boxes[1].append(item)

# Put the blanket and the coat and the planet into Box 0.
items_to_put = ['blanket', 'coat', 'planet']
for item in items_to_put:
    boxes[0].append(item)

# Move the forest and the mask and the drum from Box 4 to Box 5.
items_to_move = ['forest', 'mask', 'drum']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[5].append(item)

# Move the polish and the thunder from Box 8 to Box 0.
items_to_move = ['polish', 'thunder']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[0].append(item)

# Replace the chair with the cat in Box 4.
boxes[4].remove('chair')
boxes[4].append('cat')

# Remove the bicycle from Box 3.
boxes[3].remove('bicycle')

# Move the cat from Box 4 to Box 2.
boxes[4].remove('cat')
boxes[2].append('cat')

# Remove the bird and the thunder from Box 0.
boxes[0].remove('bird')
boxes[0].remove('thunder')

# Replace the drum with the crown in Box 5.
boxes[5].remove('drum')
boxes[5].append('crown')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")