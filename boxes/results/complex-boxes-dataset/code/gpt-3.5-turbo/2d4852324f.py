# Initial state of boxes
boxes = {
    0: ['toothbrush', 'jungle'],
    1: [],
    2: [],
    3: ['camera', 'lamp', 'starfish', 'helmet', 'fish'],
    4: ['perfume', 'star', 'tree', 'ring'],
    5: ['zipper', 'scarf', 'ship', 'shirt'],
    6: ['coat', 'game', 'chair', 'planet'],
    7: ['hat', 'coral', 'cow', 'thunder']
}

# Move the chair from Box 6 to Box 2.
boxes[6].remove('chair')
boxes[2].append('chair')

# Empty Box 4.
boxes[4] = []

# Remove the chair from Box 2.
boxes[2].remove('chair')

# Move the cow and the thunder and the coral from Box 7 to Box 0.
items_to_move = ['cow', 'thunder', 'coral']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[0].append(item)

# Swap the game in Box 6 with the camera in Box 3.
boxes[6].remove('game')
boxes[3].remove('camera')
boxes[6].append('camera')
boxes[3].append('game')

# Remove the scarf and the ship and the shirt from Box 5.
items_to_remove = ['scarf', 'ship', 'shirt']
for item in items_to_remove:
    boxes[5].remove(item)

# Swap the camera in Box 6 with the zipper in Box 5.
boxes[6].remove('camera')
boxes[5].remove('zipper')
boxes[6].append('zipper')
boxes[5].append('camera')

# Remove the hat from Box 7.
boxes[7].remove('hat')

# Put the lamp into Box 6.
boxes[6].append('lamp')

# Swap the lamp in Box 6 with the lamp in Box 3.
boxes[6].remove('lamp')
boxes[3].remove('lamp')
boxes[6].append('lamp')
boxes[3].append('lamp')

# Put the book into Box 0.
boxes[0].append('book')

# Replace the planet and the zipper and the lamp with the shoes and the storm and the rain in Box 6.
boxes[6].remove('planet')
boxes[6].remove('zipper')
boxes[6].remove('lamp')
boxes[6].append('shoes')
boxes[6].append('storm')
boxes[6].append('rain')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")