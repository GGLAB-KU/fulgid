# Initial state of boxes
boxes = {
    0: ['dog', 'game', 'razor', 'starfish'],
    1: [],
    2: ['dice'],
    3: ['shirt'],
    4: ['shorts', 'polish', 'blender'],
    5: ['pan', 'note', 'jacket', 'lock', 'planet'],
    6: ['zipper', 'fridge', 'apple', 'cloud']
}

# Move the polish and the blender and the shorts from Box 4 to Box 2.
items_to_move = ['polish', 'blender', 'shorts']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Move the game and the razor from Box 0 to Box 2.
items_to_move = ['game', 'razor']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Replace the jacket with the coat in Box 5.
boxes[5].remove('jacket')
boxes[5].append('coat')

# Put the brush and the ship and the clock into Box 4.
items_to_put = ['brush', 'ship', 'clock']
for item in items_to_put:
    boxes[4].append(item)

# Replace the fridge and the cloud with the console and the wallet in Box 6.
boxes[6].remove('fridge')
boxes[6].remove('cloud')
boxes[6].append('console')
boxes[6].append('wallet')

# Replace the starfish with the makeup in Box 0.
boxes[0].remove('starfish')
boxes[0].append('makeup')

# Put the console and the towel and the comet into Box 6.
items_to_put = ['console', 'towel', 'comet']
for item in items_to_put:
    boxes[6].append(item)

# Remove the makeup from Box 0.
boxes[0].remove('makeup')

# Empty Box 0.
boxes[0] = []

# Remove the ship and the brush and the clock from Box 4.
items_to_remove = ['ship', 'brush', 'clock']
for item in items_to_remove:
    boxes[4].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")