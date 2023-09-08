# Initial state of boxes
boxes = {
    0: ['horn'],
    1: ['octopus'],
    2: ['fish', 'microwave'],
    3: ['ocean', 'candle', 'needle'],
    4: ['rain', 'makeup', 'cat'],
    5: ['tie', 'book', 'boat'],
    6: ['dolphin', 'microscope', 'towel', 'piano'],
    7: ['mask', 'soap'],
    8: ['river', 'dog', 'vase'],
    9: ['coat', 'watch', 'blanket'],
    10: ['leaf', 'fork', 'elephant'],
    11: ['guitar', 'harmonica', 'apple', 'bear'],
    12: ['table', 'belt', 'shorts', 'planet'],
    13: ['pan', 'pen', 'helmet', 'crown', 'battery'],
    14: ['freezer', 'laptop', 'spoon', 'grinder', 'boot']
}

# Put the boot and the pot into Box 14.
boxes[14].append('boot')
boxes[14].append('pot')

# Remove the book from Box 5.
boxes[5].remove('book')

# Remove the table and the belt from Box 12.
boxes[12].remove('table')
boxes[12].remove('belt')

# Replace the piano and the towel and the dolphin with the telescope and the scarf and the console in Box 6.
boxes[6].remove('piano')
boxes[6].remove('towel')
boxes[6].remove('dolphin')
boxes[6].append('telescope')
boxes[6].append('scarf')
boxes[6].append('console')

# Put the key and the game and the desert into Box 7.
boxes[7].append('key')
boxes[7].append('game')
boxes[7].append('desert')

# Replace the telescope and the console with the ship and the meteor in Box 6.
boxes[6].remove('telescope')
boxes[6].remove('console')
boxes[6].append('ship')
boxes[6].append('meteor')

# Swap the desert in Box 7 with the planet in Box 12.
boxes[7].remove('desert')
boxes[12].remove('planet')
boxes[7].append('planet')
boxes[12].append('desert')

# Move the horn from Box 0 to Box 1.
boxes[0].remove('horn')
boxes[1].append('horn')

# Put the flower into Box 11.
boxes[11].append('flower')

# Move the game from Box 7 to Box 9.
boxes[7].remove('game')
boxes[9].append('game')

# Remove the candle and the ocean and the needle from Box 3.
boxes[3].remove('candle')
boxes[3].remove('ocean')
boxes[3].remove('needle')

# Swap the guitar in Box 11 with the freezer in Box 14.
boxes[11].remove('guitar')
boxes[14].remove('freezer')
boxes[11].append('freezer')
boxes[14].append('guitar')

# Move the planet and the key and the soap from Box 7 to Box 3.
boxes[7].remove('planet')
boxes[7].remove('key')
boxes[7].remove('soap')
boxes[3].append('planet')
boxes[3].append('key')
boxes[3].append('soap')

# Remove the coat and the blanket from Box 9.
boxes[9].remove('coat')
boxes[9].remove('blanket')

# Remove the fish from Box 2.
boxes[2].remove('fish')

# Remove the rain from Box 4.
boxes[4].remove('rain')

# Move the planet and the soap from Box 3 to Box 12.
boxes[3].remove('planet')
boxes[3].remove('soap')
boxes[12].append('planet')
boxes[12].append('soap')

# Move the microwave from Box 2 to Box 4.
boxes[2].remove('microwave')
boxes[4].append('microwave')

# Swap the oven in Box 14 with the mask in Box 7.
boxes[14].remove('oven')
boxes[7].remove('mask')
boxes[14].append('mask')
boxes[7].append('oven')

# Put the rock and the controller and the island into Box 12.
boxes[12].append('rock')
boxes[12].append('controller')
boxes[12].append('island')

# Put the hat and the pen and the branch into Box 12.
boxes[12].append('hat')
boxes[12].append('pen')
boxes[12].append('branch')

# Move the oven from Box 7 to Box 5.
boxes[7].remove('oven')
boxes[5].append('oven')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")