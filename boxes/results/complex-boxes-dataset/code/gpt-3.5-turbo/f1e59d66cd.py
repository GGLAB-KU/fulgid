# Initial state of boxes
boxes = {
    0: ['car', 'tie', 'lipstick', 'horse', 'rocket'],
    1: ['butterfly', 'camera', 'piano', 'coat'],
    2: ['lion', 'starfish', 'lightning', 'leaf', 'shelf'],
    3: ['comet', 'wire'],
    4: ['shark', 'tree', 'mountain'],
    5: ['cup', 'oven'],
    6: ['helmet', 'game', 'cat', 'console']
}

# Put the bag and the book and the note into Box 5.
items_to_move = ['bag', 'book', 'note']
for item in items_to_move:
    boxes[5].append(item)

# Swap the note in Box 5 with the butterfly in Box 1.
boxes[5].remove('note')
boxes[1].remove('butterfly')
boxes[5].append('butterfly')
boxes[1].append('note')

# Remove the lion and the shelf and the lightning from Box 2.
items_to_remove = ['lion', 'shelf', 'lightning']
for item in items_to_remove:
    boxes[2].remove(item)

# Replace the leaf with the star in Box 2.
boxes[2].remove('leaf')
boxes[2].append('star')

# Replace the tree with the oven in Box 4.
boxes[4].remove('tree')
boxes[4].append('oven')

# Swap the starfish in Box 2 with the helmet in Box 6.
boxes[2].remove('starfish')
boxes[6].remove('helmet')
boxes[2].append('helmet')
boxes[6].append('starfish')

# Swap the star in Box 2 with the game in Box 6.
boxes[2].remove('star')
boxes[6].remove('game')
boxes[2].append('game')
boxes[6].append('star')

# Replace the bag with the blender in Box 5.
boxes[5].remove('bag')
boxes[5].append('blender')

# Remove the helmet and the game from Box 2.
boxes[2].remove('helmet')
boxes[2].remove('game')

# Remove the oven and the butterfly and the book from Box 5.
items_to_remove = ['oven', 'butterfly', 'book']
for item in items_to_remove:
    boxes[5].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")