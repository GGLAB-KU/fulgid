# Initial state of boxes
boxes = {
    0: ['lamp'],
    1: ['lipstick', 'mirror', 'chair'],
    2: ['makeup', 'card', 'necklace', 'toy'],
    3: ['wig', 'soap', 'ocean', 'starfish', 'flower'],
    4: ['shark', 'console'],
    5: [],
    6: ['note'],
    7: ['fridge', 'pen', 'mountain', 'bag'],
    8: [],
    9: ['lightning', 'boat', 'button', 'bowl', 'table'],
    10: ['cat', 'bus', 'tree', 'basket'],
    11: ['planet', 'book'],
    12: ['dolphin', 'river', 'horn', 'jacket'],
    13: ['bird']
}

# Move the lamp from Box 0 to Box 11.
boxes[0].remove('lamp')
boxes[11].append('lamp')

# Swap the button in Box 9 with the card in Box 2.
boxes[9].remove('button')
boxes[2].remove('card')
boxes[9].append('card')
boxes[2].append('button')

# Remove the bird from Box 13.
boxes[13].remove('bird')

# Swap the starfish in Box 3 with the shark in Box 4.
boxes[3].remove('starfish')
boxes[4].remove('shark')
boxes[3].append('shark')
boxes[4].append('starfish')

# Remove the starfish from Box 4.
boxes[4].remove('starfish')

# Move the planet and the lamp from Box 11 to Box 13.
boxes[11].remove('planet')
boxes[11].remove('lamp')
boxes[13].append('planet')
boxes[13].append('lamp')

# Move the console from Box 4 to Box 0.
boxes[4].remove('console')
boxes[0].append('console')

# Swap the mountain in Box 7 with the note in Box 6.
boxes[7].remove('mountain')
boxes[6].remove('note')
boxes[7].append('note')
boxes[6].append('mountain')

# Remove the console from Box 0.
boxes[0].remove('console')

# Remove the shark and the wig from Box 3.
boxes[3].remove('shark')
boxes[3].remove('wig')

# Remove the soap from Box 3.
boxes[3].remove('soap')

# Replace the bus and the tree and the cat with the magnet and the pen and the mirror in Box 10.
boxes[10].remove('bus')
boxes[10].remove('tree')
boxes[10].remove('cat')
boxes[10].append('magnet')
boxes[10].append('pen')
boxes[10].append('mirror')

# Put the flower and the cup into Box 9.
boxes[9].append('flower')
boxes[9].append('cup')

# Move the mountain from Box 6 to Box 8.
boxes[6].remove('mountain')
boxes[8].append('mountain')

# Remove the mountain from Box 8.
boxes[8].remove('mountain')

# Put the lamp and the branch into Box 1.
boxes[1].append('lamp')
boxes[1].append('branch')

# Replace the pen and the magnet with the bear and the branch in Box 10.
boxes[10].remove('pen')
boxes[10].remove('magnet')
boxes[10].append('bear')
boxes[10].append('branch')

# Replace the necklace with the doll in Box 2.
boxes[2].remove('necklace')
boxes[2].append('doll')

# Replace the planet and the lamp with the laptop and the microwave in Box 13.
boxes[13].remove('planet')
boxes[13].remove('lamp')
boxes[13].append('laptop')
boxes[13].append('microwave')

# Move the fridge from Box 7 to Box 10.
boxes[7].remove('fridge')
boxes[10].append('fridge')

# Swap the jacket in Box 12 with the laptop in Box 13.
boxes[12].remove('jacket')
boxes[13].remove('laptop')
boxes[12].append('laptop')
boxes[13].append('jacket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")