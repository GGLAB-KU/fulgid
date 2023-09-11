# Initial state of boxes
boxes = {
    0: ['rock', 'comet', 'forest'],
    1: [],
    2: [],
    3: ['tree'],
    4: ['zipper', 'pillow']
}

# Replace the tree with the ocean in Box 3.
boxes[3].remove('tree')
boxes[3].append('ocean')

# Swap the forest in Box 0 with the ocean in Box 3.
boxes[0].remove('forest')
boxes[3].remove('ocean')
boxes[0].append('ocean')
boxes[3].append('forest')

# Empty Box 3.
boxes[3] = []

# Move the pillow and the zipper from Box 4 to Box 0.
items_to_move = ['pillow', 'zipper']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Replace the comet and the rock and the ocean with the glove and the lamp and the bear in Box 0.
boxes[0].remove('comet')
boxes[0].remove('rock')
boxes[0].remove('ocean')
boxes[0].append('glove')
boxes[0].append('lamp')
boxes[0].append('bear')

# Move the bear and the lamp and the zipper from Box 0 to Box 3.
items_to_move = ['bear', 'lamp', 'zipper']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Swap the bear in Box 3 with the glove in Box 0.
boxes[3].remove('bear')
boxes[0].remove('glove')
boxes[3].append('glove')
boxes[0].append('bear')

# Remove the bear and the pillow from Box 0.
boxes[0].remove('bear')
boxes[0].remove('pillow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")