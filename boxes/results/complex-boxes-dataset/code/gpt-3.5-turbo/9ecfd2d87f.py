# Initial state of boxes
boxes = {
    0: ['dice', 'horn', 'elephant', 'wallet', 'coin'],
    1: ['pen', 'octopus', 'brush', 'thunder'],
    2: ['lightning', 'doll', 'toy', 'shampoo', 'mixer'],
    3: ['grass'],
    4: ['toothpaste'],
    5: ['forest', 'star', 'clock', 'spoon', 'lock']
}

# Swap the lock in Box 5 with the octopus in Box 1.
boxes[1].remove('octopus')
boxes[5].remove('lock')
boxes[1].append('lock')
boxes[5].append('octopus')

# Replace the toothpaste with the telescope in Box 4.
boxes[4].remove('toothpaste')
boxes[4].append('telescope')

# Swap the toy in Box 2 with the grass in Box 3.
boxes[2].remove('toy')
boxes[3].remove('grass')
boxes[2].append('grass')
boxes[3].append('toy')

# Remove the shampoo and the doll from Box 2.
boxes[2].remove('shampoo')
boxes[2].remove('doll')

# Remove the dice and the horn and the coin from Box 0.
items_to_remove = ['dice', 'horn', 'coin']
for item in items_to_remove:
    boxes[0].remove(item)

# Replace the forest with the beach in Box 5.
boxes[5].remove('forest')
boxes[5].append('beach')

# Move the telescope from Box 4 to Box 0.
boxes[4].remove('telescope')
boxes[0].append('telescope')

# Swap the lightning in Box 2 with the elephant in Box 0.
boxes[0].remove('elephant')
boxes[2].remove('lightning')
boxes[0].append('lightning')
boxes[2].append('elephant')

# Remove the star from Box 5.
boxes[5].remove('star')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")