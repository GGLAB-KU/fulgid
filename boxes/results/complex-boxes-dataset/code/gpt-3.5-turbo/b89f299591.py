# Initial state of boxes
boxes = {
    0: ['bus', 'key'],
    1: ['elephant', 'button'],
    2: ['pen', 'laptop', 'shark', 'bag'],
    3: ['shampoo', 'telescope'],
    4: ['lion', 'doll', 'card', 'dog', 'toothbrush'],
    5: ['zipper', 'toy', 'razor'],
    6: ['game', 'beach', 'table'],
    7: [],
    8: ['clock', 'comet'],
    9: []
}

# Move the razor from Box 5 to Box 4.
boxes[5].remove('razor')
boxes[4].append('razor')

# Remove the laptop and the shark from Box 2.
boxes[2].remove('laptop')
boxes[2].remove('shark')

# Swap the telescope in Box 3 with the bus in Box 0.
boxes[0].remove('bus')
boxes[3].remove('telescope')
boxes[0].append('telescope')
boxes[3].append('bus')

# Remove the comet from Box 8.
boxes[8].remove('comet')

# Replace the zipper and the toy with the coat and the hat in Box 5.
boxes[5].remove('zipper')
boxes[5].remove('toy')
boxes[5].append('coat')
boxes[5].append('hat')

# Swap the hat in Box 5 with the elephant in Box 1.
boxes[1].remove('elephant')
boxes[5].remove('hat')
boxes[1].append('hat')
boxes[5].append('elephant')

# Swap the button in Box 1 with the pen in Box 2.
boxes[1].remove('button')
boxes[2].remove('pen')
boxes[1].append('pen')
boxes[2].append('button')

# Put the shoe and the headphone into Box 8.
boxes[8].append('shoe')
boxes[8].append('headphone')

# Remove the key and the telescope from Box 0.
boxes[0].remove('key')
boxes[0].remove('telescope')

# Empty Box 8.
boxes[8] = []

# Remove the game from Box 6.
boxes[6].remove('game')

# Put the horn into Box 5.
boxes[5].append('horn')

# Replace the button and the bag with the dice and the phone in Box 2.
boxes[2].remove('button')
boxes[2].remove('bag')
boxes[2].append('dice')
boxes[2].append('phone')

# Put the tree into Box 6.
boxes[6].append('tree')

# Remove the shampoo from Box 3.
boxes[3].remove('shampoo')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")