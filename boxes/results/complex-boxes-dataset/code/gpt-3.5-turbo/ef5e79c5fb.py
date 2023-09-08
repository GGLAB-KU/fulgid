# Initial state of boxes
boxes = {
    0: [],
    1: ['star', 'shoe', 'perfume', 'rock', 'shirt'],
    2: ['toy', 'dolphin', 'drum', 'swimsuit'],
    3: [],
    4: [],
    5: ['button', 'scissors', 'storm'],
    6: ['bear', 'horn', 'ship', 'whistle'],
    7: ['fridge', 'tape', 'telescope', 'key'],
    8: ['camera', 'toaster']
}

# Move the bear from Box 6 to Box 5.
boxes[6].remove('bear')
boxes[5].append('bear')

# Empty Box 6.
boxes[6] = []

# Replace the perfume and the star with the pants and the wig in Box 1.
boxes[1].remove('perfume')
boxes[1].remove('star')
boxes[1].append('pants')
boxes[1].append('wig')

# Move the camera from Box 8 to Box 0.
boxes[8].remove('camera')
boxes[0].append('camera')

# Replace the toaster with the pants in Box 8.
boxes[8].remove('toaster')
boxes[8].append('pants')

# Move the camera from Box 0 to Box 6.
boxes[0].remove('camera')
boxes[6].append('camera')

# Swap the button in Box 5 with the pants in Box 8.
boxes[5].remove('button')
boxes[8].remove('pants')
boxes[5].append('pants')
boxes[8].append('button')

# Replace the shoe with the toothpaste in Box 1.
boxes[1].remove('shoe')
boxes[1].append('toothpaste')

# Move the toy from Box 2 to Box 5.
boxes[2].remove('toy')
boxes[5].append('toy')

# Put the phone into Box 8.
boxes[8].append('phone')

# Swap the wig in Box 1 with the dolphin in Box 2.
boxes[1].remove('wig')
boxes[2].remove('dolphin')
boxes[1].append('dolphin')
boxes[2].append('wig')

# Move the button and the phone from Box 8 to Box 0.
boxes[8].remove('button')
boxes[8].remove('phone')
boxes[0].append('button')
boxes[0].append('phone')

# Move the tape and the telescope from Box 7 to Box 0.
boxes[7].remove('tape')
boxes[7].remove('telescope')
boxes[0].append('tape')
boxes[0].append('telescope')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")