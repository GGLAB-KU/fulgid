# Initial state of boxes
boxes = {
    0: ['planet', 'violin', 'boot'],
    1: ['dice', 'button'],
    2: [],
    3: ['controller', 'forest', 'crown', 'pot', 'microscope'],
    4: ['submarine', 'pen', 'cup', 'headphone', 'dolphin'],
    5: ['shoes', 'branch'],
    6: ['skirt', 'glove', 'coat', 'starfish'],
    7: ['ring', 'leaf', 'lock', 'hat', 'tiger'],
    8: ['polish', 'pants', 'shampoo'],
    9: ['zipper', 'charger', 'cat'],
    10: ['butterfly'],
    11: ['octopus', 'fork', 'freezer'],
    12: ['laptop']
}

# Replace the violin and the boot with the bracelet and the island in Box 0.
boxes[0].remove('violin')
boxes[0].remove('boot')
boxes[0].append('bracelet')
boxes[0].append('island')

# Replace the planet with the sun in Box 0.
boxes[0].remove('planet')
boxes[0].append('sun')

# Put the cloud into Box 9.
boxes[9].append('cloud')

# Put the tree and the island and the desert into Box 6.
boxes[6].append('tree')
boxes[6].append('island')
boxes[6].append('desert')

# Swap the laptop in Box 12 with the shoes in Box 5.
boxes[12], boxes[5] = boxes[5], boxes[12]

# Replace the button and the dice with the oven and the coat in Box 1.
boxes[1].remove('button')
boxes[1].remove('dice')
boxes[1].append('oven')
boxes[1].append('coat')

# Move the butterfly from Box 10 to Box 4.
boxes[10].remove('butterfly')
boxes[4].append('butterfly')

# Move the branch from Box 5 to Box 0.
boxes[5].remove('branch')
boxes[0].append('branch')

# Remove the pen and the dolphin and the headphone from Box 4.
boxes[4].remove('pen')
boxes[4].remove('dolphin')
boxes[4].remove('headphone')

# Put the coin and the usb into Box 11.
boxes[11].append('coin')
boxes[11].append('usb')

# Replace the submarine and the butterfly and the cup with the planet and the bird and the comb in Box 4.
boxes[4].remove('submarine')
boxes[4].remove('butterfly')
boxes[4].remove('cup')
boxes[4].append('planet')
boxes[4].append('bird')
boxes[4].append('comb')

# Remove the shoes from Box 12.
boxes[12].remove('shoes')

# Swap the bracelet in Box 0 with the pants in Box 8.
boxes[0].remove('bracelet')
boxes[8].remove('pants')
boxes[0].append('pants')
boxes[8].append('bracelet')

# Replace the skirt and the desert and the starfish with the spoon and the dog and the card in Box 6.
boxes[6].remove('skirt')
boxes[6].remove('desert')
boxes[6].remove('starfish')
boxes[6].append('spoon')
boxes[6].append('dog')
boxes[6].append('card')

# Put the guitar and the horn and the thunder into Box 2.
boxes[2].append('guitar')
boxes[2].append('horn')
boxes[2].append('thunder')

# Remove the oven from Box 1.
boxes[1].remove('oven')

# Remove the comb from Box 4.
boxes[4].remove('comb')

# Replace the crown with the microscope in Box 3.
boxes[3].remove('crown')
boxes[3].append('microscope')

# Move the microscope and the pot from Box 3 to Box 9.
boxes[3].remove('microscope')
boxes[3].remove('pot')
boxes[9].append('microscope')
boxes[9].append('pot')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")