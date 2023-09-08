# Initial state of boxes
boxes = {
    0: ['nothing'],
    1: ['grinder', 'fish', 'cloud', 'lamp'],
    2: ['puzzle'],
    3: ['skirt', 'glove', 'fork'],
    4: ['toothpaste', 'crown', 'rocket'],
    5: ['ocean'],
    6: ['game'],
    7: ['nothing']
}

# Replace the skirt and the fork with the gloves and the snow in Box 3.
boxes[3].remove('skirt')
boxes[3].remove('fork')
boxes[3].append('gloves')
boxes[3].append('snow')

# Swap the fish in Box 1 with the ocean in Box 5.
boxes[1].remove('fish')
boxes[5].remove('ocean')
boxes[1].append('ocean')
boxes[5].append('fish')

# Put the makeup and the submarine into Box 4.
boxes[4].append('makeup')
boxes[4].append('submarine')

# Move the puzzle from Box 2 to Box 3.
boxes[2].remove('puzzle')
boxes[3].append('puzzle')

# Replace the submarine with the lion in Box 4.
boxes[4].remove('submarine')
boxes[4].append('lion')

# Put the swimsuit and the tape into Box 7.
boxes[7].append('swimsuit')
boxes[7].append('tape')

# Replace the snow and the gloves and the puzzle with the frame and the watch and the wallet in Box 3.
boxes[3].remove('snow')
boxes[3].remove('gloves')
boxes[3].remove('puzzle')
boxes[3].append('frame')
boxes[3].append('watch')
boxes[3].append('wallet')

# Remove the tape from Box 7.
boxes[7].remove('tape')

# Put the elephant into Box 3.
boxes[3].append('elephant')

# Put the mask into Box 0.
boxes[0].remove('nothing')
boxes[0].append('mask')

# Move the frame from Box 3 to Box 7.
boxes[3].remove('frame')
boxes[7].append('frame')

# Move the watch and the elephant and the glove from Box 3 to Box 7.
items_to_move = ['watch', 'elephant', 'glove']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[7].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")