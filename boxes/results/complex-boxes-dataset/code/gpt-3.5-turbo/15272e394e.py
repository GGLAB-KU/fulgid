# Initial state of boxes
boxes = {
    0: ['tie', 'drum', 'needle'],
    1: ['pan'],
    2: [],
    3: ['bag', 'shoe', 'microscope', 'tiger', 'rain'],
    4: ['lion', 'planet', 'freezer', 'whistle'],
    5: ['microwave', 'towel', 'shirt', 'hat', 'umbrella'],
    6: ['card', 'wire'],
    7: ['flower', 'zipper'],
    8: ['motorcycle', 'desert', 'coin'],
    9: ['bell', 'polish', 'shorts'],
    10: ['perfume', 'elephant', 'frame', 'dog', 'toothpaste'],
    11: ['grinder'],
    12: ['helmet', 'toaster', 'tape', 'island'],
    13: ['meteor', 'branch', 'blanket'],
    14: []
}

# Remove the planet from Box 4.
boxes[4].remove('planet')

# Replace the card with the sculpture in Box 6.
boxes[6].remove('card')
boxes[6].append('sculpture')

# Put the hat and the grass into Box 11.
boxes[11].append('hat')
boxes[11].append('grass')

# Replace the meteor with the blanket in Box 13.
boxes[13].remove('meteor')
boxes[13].append('blanket')

# Move the pan from Box 1 to Box 5.
boxes[1].remove('pan')
boxes[5].append('pan')

# Put the wallet and the piano and the train into Box 1.
boxes[1].append('wallet')
boxes[1].append('piano')
boxes[1].append('train')

# Swap the lion in Box 4 with the tie in Box 0.
boxes[4].remove('lion')
boxes[0].remove('tie')
boxes[4].append('tie')
boxes[0].append('lion')

# Put the polish into Box 2.
boxes[2].append('polish')

# Remove the shoe and the microscope from Box 3.
boxes[3].remove('shoe')
boxes[3].remove('microscope')

# Swap the freezer in Box 4 with the desert in Box 8.
boxes[4].remove('freezer')
boxes[8].remove('desert')
boxes[4].append('desert')
boxes[8].append('freezer')

# Replace the blanket with the sun in Box 13.
boxes[13].remove('blanket')
boxes[13].append('sun')

# Empty Box 13.
boxes[13] = []

# Put the oven and the island into Box 5.
boxes[5].append('oven')
boxes[5].append('island')

# Swap the polish in Box 9 with the grinder in Box 11.
boxes[9].remove('polish')
boxes[11].remove('grinder')
boxes[9].append('grinder')
boxes[11].append('polish')

# Swap the grass in Box 11 with the oven in Box 5.
boxes[11].remove('grass')
boxes[5].remove('oven')
boxes[11].append('oven')
boxes[5].append('grass')

# Swap the train in Box 1 with the zipper in Box 7.
boxes[1].remove('train')
boxes[7].remove('zipper')
boxes[1].append('zipper')
boxes[7].append('train')

# Put the lion and the truck into Box 3.
boxes[3].append('lion')
boxes[3].append('truck')

# Move the grass and the pan from Box 5 to Box 11.
boxes[5].remove('grass')
boxes[5].remove('pan')
boxes[11].append('grass')
boxes[11].append('pan')

# Move the polish and the grass and the pan from Box 11 to Box 10.
items_to_move = ['polish', 'grass', 'pan']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[10].append(item)

# Replace the flower and the train with the bicycle and the chair in Box 7.
boxes[7].remove('flower')
boxes[7].remove('train')
boxes[7].append('bicycle')
boxes[7].append('chair')

# Remove the wallet from Box 1.
boxes[1].remove('wallet')

# Empty Box 10.
boxes[10] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")