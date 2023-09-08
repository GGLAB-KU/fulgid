# Initial state of boxes
boxes = {
    0: ['flower'],
    1: ['bracelet'],
    2: ['plate'],
    3: ['game'],
    4: ['rock', 'toothbrush', 'clock'],
    5: ['bird', 'toy'],
    6: ['doll', 'swimsuit', 'boot', 'controller', 'horn'],
    7: [],
    8: [],
    9: ['telescope', 'freezer'],
    10: ['table'],
    11: ['brush', 'spoon']
}

# Remove the spoon and the brush from Box 11.
boxes[11].remove('spoon')
boxes[11].remove('brush')

# Swap the bracelet in Box 1 with the rock in Box 4.
boxes[1].remove('bracelet')
boxes[4].remove('rock')
boxes[1].append('rock')
boxes[4].append('bracelet')

# Swap the rock in Box 1 with the table in Box 10.
boxes[1].remove('rock')
boxes[10].remove('table')
boxes[1].append('table')
boxes[10].append('rock')

# Move the table from Box 1 to Box 10.
boxes[1].remove('table')
boxes[10].append('table')

# Remove the freezer from Box 9.
boxes[9].remove('freezer')

# Remove the controller and the swimsuit from Box 6.
boxes[6].remove('controller')
boxes[6].remove('swimsuit')

# Swap the toothbrush in Box 4 with the telescope in Box 9.
boxes[4].remove('toothbrush')
boxes[9].remove('telescope')
boxes[4].append('telescope')
boxes[9].append('toothbrush')

# Swap the toothbrush in Box 9 with the bird in Box 5.
boxes[9].remove('toothbrush')
boxes[5].remove('bird')
boxes[9].append('bird')
boxes[5].append('toothbrush')

# Move the telescope and the bracelet from Box 4 to Box 6.
boxes[4].remove('telescope')
boxes[4].remove('bracelet')
boxes[6].append('telescope')
boxes[6].append('bracelet')

# Remove the bird from Box 9.
boxes[9].remove('bird')

# Replace the bracelet and the horn and the boot with the island and the submarine and the rock in Box 6.
boxes[6].remove('bracelet')
boxes[6].remove('horn')
boxes[6].remove('boot')
boxes[6].append('island')
boxes[6].append('submarine')
boxes[6].append('rock')

# Put the button and the lamp and the game into Box 7.
boxes[7].append('button')
boxes[7].append('lamp')
boxes[7].append('game')

# Move the game from Box 3 to Box 7.
boxes[3].remove('game')
boxes[7].append('game')

# Remove the telescope from Box 6.
boxes[6].remove('telescope')

# Replace the toy with the forest in Box 5.
boxes[5].remove('toy')
boxes[5].append('forest')

# Remove the flower from Box 0.
boxes[0].remove('flower')

# Remove the plate from Box 2.
boxes[2].remove('plate')

# Swap the button in Box 7 with the doll in Box 6.
boxes[7].remove('button')
boxes[6].remove('doll')
boxes[7].append('doll')
boxes[6].append('button')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")