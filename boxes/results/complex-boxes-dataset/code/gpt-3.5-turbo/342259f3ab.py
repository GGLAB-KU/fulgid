# Initial state of boxes
boxes = {
    0: ['elephant'],
    1: ['toothpaste', 'crown', 'plane', 'island', 'swimsuit'],
    2: ['pot', 'book', 'charger'],
    3: ['toy'],
    4: ['oven', 'whistle', 'phone', 'plate', 'microwave'],
    5: ['tie'],
    6: ['frame', 'jacket'],
    7: ['bus'],
    8: ['coin', 'toaster', 'comb'],
    9: ['shoe', 'pillow', 'note']
}

# Empty Box 5.
boxes[5] = []

# Replace the frame with the belt in Box 6.
boxes[6].remove('frame')
boxes[6].append('belt')

# Move the bus from Box 7 to Box 1.
boxes[7].remove('bus')
boxes[1].append('bus')

# Replace the shoe and the pillow with the rocket and the pants in Box 9.
boxes[9].remove('shoe')
boxes[9].remove('pillow')
boxes[9].append('rocket')
boxes[9].append('pants')

# Move the belt from Box 6 to Box 5.
boxes[6].remove('belt')
boxes[5].append('belt')

# Put the octopus and the coin into Box 2.
boxes[2].append('octopus')
boxes[2].append('coin')

# Move the belt from Box 5 to Box 3.
boxes[5].remove('belt')
boxes[3].append('belt')

# Move the oven and the phone from Box 4 to Box 9.
boxes[4].remove('oven')
boxes[4].remove('phone')
boxes[9].append('oven')
boxes[9].append('phone')

# Empty Box 8.
boxes[8] = []

# Swap the note in Box 9 with the belt in Box 3.
boxes[9].remove('note')
boxes[3].remove('belt')
boxes[9].append('belt')
boxes[3].append('note')

# Swap the toy in Box 3 with the plate in Box 4.
boxes[3].remove('toy')
boxes[4].remove('plate')
boxes[3].append('plate')
boxes[4].append('toy')

# Put the lamp and the microwave into Box 7.
boxes[7].append('lamp')
boxes[7].append('microwave')

# Move the oven and the rocket from Box 9 to Box 1.
boxes[9].remove('oven')
boxes[9].remove('rocket')
boxes[1].append('oven')
boxes[1].append('rocket')

# Swap the microwave in Box 4 with the lamp in Box 7.
boxes[4].remove('microwave')
boxes[7].remove('lamp')
boxes[4].append('lamp')
boxes[7].append('microwave')

# Move the toy and the whistle from Box 4 to Box 1.
boxes[4].remove('toy')
boxes[4].remove('whistle')
boxes[1].append('toy')
boxes[1].append('whistle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")