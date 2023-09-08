# Initial state of boxes
boxes = {
    0: ['jacket', 'lamp'],
    1: ['scissors', 'magnet', 'forest', 'microscope'],
    2: ['telescope', 'thunder', 'lipstick'],
    3: [],
    4: ['island', 'sandals', 'table', 'bowl', 'beach'],
    5: ['truck', 'boat'],
    6: ['bird', 'rain', 'pot'],
    7: ['pen', 'toaster', 'glove', 'ring', 'guitar'],
    8: ['flower', 'comb', 'dice', 'grinder', 'towel']
}

# Remove the island and the table from Box 4.
boxes[4].remove('island')
boxes[4].remove('table')

# Put the whistle into Box 5.
boxes[5].append('whistle')

# Replace the truck with the flower in Box 5.
boxes[5].remove('truck')
boxes[5].append('flower')

# Swap the glove in Box 7 with the flower in Box 5.
boxes[7].remove('glove')
boxes[5].remove('flower')
boxes[7].append('flower')
boxes[5].append('glove')

# Remove the toaster from Box 7.
boxes[7].remove('toaster')

# Swap the dice in Box 8 with the whistle in Box 5.
boxes[8].remove('dice')
boxes[5].remove('whistle')
boxes[8].append('whistle')
boxes[5].append('dice')

# Put the book into Box 3.
boxes[3].append('book')

# Move the guitar from Box 7 to Box 0.
boxes[7].remove('guitar')
boxes[0].append('guitar')

# Remove the whistle from Box 8.
boxes[8].remove('whistle')

# Move the beach and the bowl from Box 4 to Box 1.
boxes[4].remove('beach')
boxes[4].remove('bowl')
boxes[1].append('beach')
boxes[1].append('bowl')

# Swap the flower in Box 8 with the thunder in Box 2.
boxes[8].remove('flower')
boxes[2].remove('thunder')
boxes[8].append('thunder')
boxes[2].append('flower')

# Put the book and the razor into Box 2.
boxes[2].append('book')
boxes[2].append('razor')

# Replace the lipstick with the bear in Box 2.
boxes[2].remove('lipstick')
boxes[2].append('bear')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")