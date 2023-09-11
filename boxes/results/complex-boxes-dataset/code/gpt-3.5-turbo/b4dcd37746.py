# Initial state of boxes
boxes = {
    0: [],
    1: ['grinder'],
    2: ['shelf'],
    3: ['dress', 'swimsuit'],
    4: [],
    5: ['button', 'piano', 'boat'],
    6: ['glasses', 'glove', 'bear', 'belt'],
    7: ['shoe', 'polish', 'umbrella', 'camera'],
    8: ['cup', 'perfume', 'wire', 'card'],
    9: ['shark', 'grass', 'toy', 'usb', 'microscope'],
    10: ['scissors', 'vase']
}

# Put the whistle and the oven into Box 9.
boxes[9].append('whistle')
boxes[9].append('oven')

# Remove the usb from Box 9.
boxes[9].remove('usb')

# Swap the umbrella in Box 7 with the cup in Box 8.
boxes[7].remove('umbrella')
boxes[8].remove('cup')
boxes[7].append('cup')
boxes[8].append('umbrella')

# Remove the perfume and the card from Box 8.
boxes[8].remove('perfume')
boxes[8].remove('card')

# Replace the dress and the swimsuit with the rock and the laptop in Box 3.
boxes[3].remove('dress')
boxes[3].remove('swimsuit')
boxes[3].append('rock')
boxes[3].append('laptop')

# Replace the glasses and the belt and the bear with the toothbrush and the paint and the star in Box 6.
boxes[6].remove('glasses')
boxes[6].remove('belt')
boxes[6].remove('bear')
boxes[6].append('toothbrush')
boxes[6].append('paint')
boxes[6].append('star')

# Put the sandals into Box 6.
boxes[6].append('sandals')

# Put the microwave and the river into Box 3.
boxes[3].append('microwave')
boxes[3].append('river')

# Replace the umbrella and the wire with the train and the camera in Box 8.
boxes[8].remove('umbrella')
boxes[8].remove('wire')
boxes[8].append('train')
boxes[8].append('camera')

# Move the rock and the laptop from Box 3 to Box 7.
boxes[3].remove('rock')
boxes[3].remove('laptop')
boxes[7].append('rock')
boxes[7].append('laptop')

# Replace the shoe with the violin in Box 7.
boxes[7].remove('shoe')
boxes[7].append('violin')

# Remove the grinder from Box 1.
boxes[1].remove('grinder')

# Put the pants and the starfish into Box 10.
boxes[10].append('pants')
boxes[10].append('starfish')

# Swap the toy in Box 9 with the boat in Box 5.
boxes[9].remove('toy')
boxes[5].remove('boat')
boxes[9].append('boat')
boxes[5].append('toy')

# Move the shelf from Box 2 to Box 10.
boxes[2].remove('shelf')
boxes[10].append('shelf')

# Remove the paint and the star and the sandals from Box 6.
boxes[6].remove('paint')
boxes[6].remove('star')
boxes[6].remove('sandals')

# Put the flute and the bell into Box 8.
boxes[8].append('flute')
boxes[8].append('bell')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")