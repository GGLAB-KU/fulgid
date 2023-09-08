# Initial state of boxes
boxes = {
    0: ['pot', 'moon', 'train', 'grinder', 'paint'],
    1: ['boat', 'soap', 'river', 'lightning'],
    2: ['microscope', 'flute', 'rocket'],
    3: ['card'],
    4: ['glove'],
    5: ['bicycle', 'submarine'],
    6: ['jungle', 'helmet', 'basket', 'harmonica', 'storm'],
    7: ['bus', 'watch', 'island'],
    8: ['speaker', 'gloves', 'brush', 'mirror', 'ocean']
}

# Replace the speaker and the gloves and the mirror with the toothpaste and the spoon and the thunder in Box 8.
boxes[8].remove('speaker')
boxes[8].remove('gloves')
boxes[8].remove('mirror')
boxes[8].append('toothpaste')
boxes[8].append('spoon')
boxes[8].append('thunder')

# Move the rocket and the flute and the microscope from Box 2 to Box 6.
items_to_move = ['rocket', 'flute', 'microscope']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Put the skirt and the battery into Box 3.
boxes[3].append('skirt')
boxes[3].append('battery')

# Remove the submarine and the bicycle from Box 5.
boxes[5].remove('submarine')
boxes[5].remove('bicycle')

# Remove the boat and the river from Box 1.
boxes[1].remove('boat')
boxes[1].remove('river')

# Remove the glove from Box 4.
boxes[4].remove('glove')

# Put the frame into Box 4.
boxes[4].append('frame')

# Put the button into Box 2.
boxes[2].append('button')

# Replace the frame with the button in Box 4.
boxes[4].remove('frame')
boxes[4].append('button')

# Replace the button with the dress in Box 2.
boxes[2].remove('button')
boxes[2].append('dress')

# Put the shorts and the drum into Box 3.
boxes[3].append('shorts')
boxes[3].append('drum')

# Remove the dress from Box 2.
boxes[2].remove('dress')

# Move the brush and the spoon from Box 8 to Box 0.
items_to_move = ['brush', 'spoon']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")