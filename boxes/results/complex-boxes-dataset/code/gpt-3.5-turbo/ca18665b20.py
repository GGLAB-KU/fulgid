# Initial state of boxes
boxes = {
    0: ['leaf'],
    1: ['watch', 'keyboard', 'mountain', 'fish'],
    2: ['table', 'button', 'book', 'telescope', 'dolphin'],
    3: ['horse', 'microwave'],
    4: ['flower', 'tiger', 'shoe', 'lion']
}

# Remove the dolphin and the table from Box 2.
boxes[2].remove('dolphin')
boxes[2].remove('table')

# Replace the tiger and the lion with the grass and the mixer in Box 4.
boxes[4].remove('tiger')
boxes[4].remove('lion')
boxes[4].append('grass')
boxes[4].append('mixer')

# Remove the keyboard and the mountain from Box 1.
boxes[1].remove('keyboard')
boxes[1].remove('mountain')

# Empty Box 2.
boxes[2] = []

# Replace the fish with the note in Box 1.
boxes[1].remove('fish')
boxes[1].append('note')

# Remove the watch from Box 1.
boxes[1].remove('watch')

# Move the microwave and the horse from Box 3 to Box 1.
boxes[3].remove('microwave')
boxes[3].remove('horse')
boxes[1].append('microwave')
boxes[1].append('horse')

# Swap the grass in Box 4 with the microwave in Box 1.
boxes[4].remove('grass')
boxes[1].remove('microwave')
boxes[4].append('microwave')
boxes[1].append('grass')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")