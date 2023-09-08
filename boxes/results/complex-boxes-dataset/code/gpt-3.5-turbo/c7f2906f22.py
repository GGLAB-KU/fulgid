# Initial state of boxes
boxes = {
    0: ['toy'],
    1: ['necklace', 'jungle', 'bowl', 'coin'],
    2: [],
    3: ['wig', 'star', 'horn', 'drum'],
    4: ['cow', 'shoes'],
    5: ['lipstick', 'snow', 'ocean', 'rocket'],
    6: ['elephant', 'shoe', 'umbrella'],
    7: ['shorts', 'butterfly'],
    8: ['game', 'doll', 'belt']
}

# Put the helmet and the bird into Box 4.
boxes[4].append('helmet')
boxes[4].append('bird')

# Remove the toy from Box 0.
boxes[0].remove('toy')

# Remove the shorts from Box 7.
boxes[7].remove('shorts')

# Swap the star in Box 3 with the snow in Box 5.
boxes[3].remove('star')
boxes[5].remove('snow')
boxes[3].append('snow')
boxes[5].append('star')

# Remove the rocket from Box 5.
boxes[5].remove('rocket')

# Move the butterfly from Box 7 to Box 6.
boxes[7].remove('butterfly')
boxes[6].append('butterfly')

# Swap the game in Box 8 with the jungle in Box 1.
boxes[8].remove('game')
boxes[1].remove('jungle')
boxes[8].append('jungle')
boxes[1].append('game')

# Move the jungle and the belt from Box 8 to Box 4.
boxes[8].remove('jungle')
boxes[8].remove('belt')
boxes[4].append('jungle')
boxes[4].append('belt')

# Replace the snow and the horn and the drum with the speaker and the octopus and the wire in Box 3.
boxes[3].remove('snow')
boxes[3].remove('horn')
boxes[3].remove('drum')
boxes[3].append('speaker')
boxes[3].append('octopus')
boxes[3].append('wire')

# Replace the helmet and the shoes and the bird with the swimsuit and the rock and the battery in Box 4.
boxes[4].remove('helmet')
boxes[4].remove('shoes')
boxes[4].remove('bird')
boxes[4].append('swimsuit')
boxes[4].append('rock')
boxes[4].append('battery')

# Remove the star from Box 5.
boxes[5].remove('star')

# Replace the doll with the button in Box 8.
boxes[8].remove('doll')
boxes[8].append('button')

# Swap the rock in Box 4 with the umbrella in Box 6.
boxes[4].remove('rock')
boxes[6].remove('umbrella')
boxes[4].append('umbrella')
boxes[6].append('rock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")