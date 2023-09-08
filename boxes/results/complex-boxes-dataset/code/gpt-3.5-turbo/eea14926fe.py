# Initial state of boxes
boxes = {
    0: ['lock', 'shark', 'comb', 'note', 'ring'],
    1: [],
    2: ['hat'],
    3: ['fork', 'train', 'puzzle', 'magnet'],
    4: ['usb', 'whistle'],
    5: ['rain'],
    6: ['rock', 'pan'],
    7: ['plate', 'boat', 'watch', 'grinder'],
    8: ['shoes', 'soap', 'toothpaste']
}

# Remove the rain from Box 5.
boxes[5].remove('rain')

# Put the guitar and the mirror and the fork into Box 4.
boxes[4].append('guitar')
boxes[4].append('mirror')
boxes[4].append('fork')

# Put the rock and the tape into Box 8.
boxes[8].append('rock')
boxes[8].append('tape')

# Move the hat from Box 2 to Box 4.
boxes[2].remove('hat')
boxes[4].append('hat')

# Replace the whistle with the octopus in Box 4.
boxes[4].remove('whistle')
boxes[4].append('octopus')

# Replace the shark and the note and the comb with the blender and the doll and the shelf in Box 0.
boxes[0].remove('shark')
boxes[0].remove('note')
boxes[0].remove('comb')
boxes[0].append('blender')
boxes[0].append('doll')
boxes[0].append('shelf')

# Replace the doll and the blender and the lock with the jungle and the cow and the camera in Box 0.
boxes[0].remove('doll')
boxes[0].remove('blender')
boxes[0].remove('lock')
boxes[0].append('jungle')
boxes[0].append('cow')
boxes[0].append('camera')

# Remove the ring from Box 0.
boxes[0].remove('ring')

# Put the basket and the dice into Box 0.
boxes[0].append('basket')
boxes[0].append('dice')

# Remove the cow from Box 0.
boxes[0].remove('cow')

# Remove the plate and the boat from Box 7.
boxes[7].remove('plate')
boxes[7].remove('boat')

# Empty Box 7.
boxes[7] = []

# Put the piano into Box 2.
boxes[2].append('piano')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")