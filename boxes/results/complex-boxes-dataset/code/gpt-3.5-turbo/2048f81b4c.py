# Initial state of boxes
boxes = {
    0: ['desert', 'apple', 'rain', 'star'],
    1: ['necklace', 'beach', 'game'],
    2: ['towel'],
    3: ['pot', 'candle', 'shoe'],
    4: ['wallet', 'branch', 'freezer', 'bird', 'guitar'],
    5: ['dice', 'shoes', 'scissors'],
    6: ['glasses', 'leaf', 'polish'],
    7: ['toaster', 'blanket', 'whistle'],
    8: ['toothbrush', 'boat', 'umbrella'],
    9: ['telescope'],
    10: ['jungle', 'bicycle'],
    11: ['sun'],
    12: ['phone', 'starfish', 'button', 'boot', 'puzzle'],
    13: ['basket', 'pan']
}

# Move the bird from Box 4 to Box 3.
boxes[4].remove('bird')
boxes[3].append('bird')

# Remove the bicycle from Box 10.
boxes[10].remove('bicycle')

# Swap the boat in Box 8 with the dice in Box 5.
boxes[8].remove('boat')
boxes[5].remove('dice')
boxes[8].append('dice')
boxes[5].append('boat')

# Replace the telescope with the island in Box 9.
boxes[9].remove('telescope')
boxes[9].append('island')

# Move the pan and the basket from Box 13 to Box 7.
boxes[13].remove('pan')
boxes[13].remove('basket')
boxes[7].append('pan')
boxes[7].append('basket')

# Put the jungle and the thunder and the microwave into Box 2.
boxes[2].append('jungle')
boxes[2].append('thunder')
boxes[2].append('microwave')

# Move the toothbrush and the umbrella from Box 8 to Box 3.
boxes[8].remove('toothbrush')
boxes[8].remove('umbrella')
boxes[3].append('toothbrush')
boxes[3].append('umbrella')

# Replace the bird and the pot and the shoe with the puzzle and the forest and the blender in Box 3.
boxes[3].remove('bird')
boxes[3].remove('pot')
boxes[3].remove('shoe')
boxes[3].append('puzzle')
boxes[3].append('forest')
boxes[3].append('blender')

# Remove the dice from Box 8.
boxes[8].remove('dice')

# Replace the island with the perfume in Box 9.
boxes[9].remove('island')
boxes[9].append('perfume')

# Replace the shoes and the scissors with the sandals and the watch in Box 5.
boxes[5].remove('shoes')
boxes[5].remove('scissors')
boxes[5].append('sandals')
boxes[5].append('watch')

# Remove the sun from Box 11.
boxes[11].remove('sun')

# Move the candle and the blender and the forest from Box 3 to Box 2.
boxes[3].remove('candle')
boxes[3].remove('blender')
boxes[3].remove('forest')
boxes[2].append('candle')
boxes[2].append('blender')
boxes[2].append('forest')

# Put the headphone into Box 6.
boxes[6].append('headphone')

# Empty Box 6.
boxes[6] = []

# Replace the beach and the game and the necklace with the bicycle and the harmonica and the toothbrush in Box 1.
boxes[1].remove('beach')
boxes[1].remove('game')
boxes[1].remove('necklace')
boxes[1].append('bicycle')
boxes[1].append('harmonica')
boxes[1].append('toothbrush')

# Remove the blanket and the pan and the toaster from Box 7.
boxes[7].remove('blanket')
boxes[7].remove('pan')
boxes[7].remove('toaster')

# Replace the umbrella and the puzzle with the rain and the flower in Box 3.
boxes[3].remove('umbrella')
boxes[3].remove('puzzle')
boxes[3].append('rain')
boxes[3].append('flower')

# Put the hat and the whistle and the butterfly into Box 4.
boxes[4].append('hat')
boxes[4].append('whistle')
boxes[4].append('butterfly')

# Swap the perfume in Box 9 with the freezer in Box 4.
boxes[9].remove('perfume')
boxes[4].remove('freezer')
boxes[9].append('freezer')
boxes[4].append('perfume')

# Put the table into Box 13.
boxes[13].append('table')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")