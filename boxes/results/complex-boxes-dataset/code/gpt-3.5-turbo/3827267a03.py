# Initial state of boxes
boxes = {
    0: ['shoes', 'drum'],
    1: ['magnet', 'oven', 'mask', 'button', 'branch'],
    2: ['mountain', 'thread', 'tie', 'desert', 'bird'],
    3: [],
    4: ['toothbrush', 'umbrella', 'card', 'doll', 'moon'],
    5: [],
    6: ['scissors', 'controller', 'coin'],
    7: [],
    8: ['bicycle']
}

# Remove the coin from Box 6.
boxes[6].remove('coin')

# Put the mask into Box 3.
boxes[1].remove('mask')
boxes[3].append('mask')

# Replace the thread and the tie with the jungle and the earring in Box 2.
boxes[2].remove('thread')
boxes[2].remove('tie')
boxes[2].append('jungle')
boxes[2].append('earring')

# Swap the mask in Box 3 with the doll in Box 4.
boxes[3].remove('mask')
boxes[4].remove('doll')
boxes[3].append('doll')
boxes[4].append('mask')

# Swap the card in Box 4 with the bicycle in Box 8.
boxes[4].remove('card')
boxes[8].remove('bicycle')
boxes[4].append('bicycle')
boxes[8].append('card')

# Remove the branch and the magnet from Box 1.
boxes[1].remove('branch')
boxes[1].remove('magnet')

# Empty Box 2.
boxes[2] = []

# Put the table and the skirt into Box 6.
boxes[6].append('table')
boxes[6].append('skirt')

# Empty Box 1.
boxes[1] = []

# Swap the card in Box 8 with the doll in Box 3.
boxes[8].remove('card')
boxes[3].remove('doll')
boxes[8].append('doll')
boxes[3].append('card')

# Put the dice and the wallet into Box 2.
boxes[2].append('dice')
boxes[2].append('wallet')

# Replace the skirt and the table and the scissors with the tree and the puzzle and the tiger in Box 6.
boxes[6].remove('skirt')
boxes[6].remove('table')
boxes[6].remove('scissors')
boxes[6].append('tree')
boxes[6].append('puzzle')
boxes[6].append('tiger')

# Remove the toothbrush from Box 4.
boxes[4].remove('toothbrush')

# Swap the moon in Box 4 with the shoes in Box 0.
boxes[4].remove('moon')
boxes[0].remove('shoes')
boxes[4].append('shoes')
boxes[0].append('moon')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")