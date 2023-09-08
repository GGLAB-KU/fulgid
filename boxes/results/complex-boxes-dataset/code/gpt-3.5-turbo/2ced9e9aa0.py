# Initial state of boxes
boxes = {
    0: ['console', 'cow', 'shoes', 'sun', 'toaster'],
    1: ['rock', 'telescope', 'soap', 'snow', 'toothpaste'],
    2: ['shorts', 'boot', 'tape', 'scarf'],
    3: ['mixer', 'moon'],
    4: [],
    5: [],
    6: ['note', 'branch', 'book', 'cloud']
}

# Put the hat and the toothbrush and the sculpture into Box 1.
items_to_move = ['hat', 'toothbrush', 'sculpture']
for item in items_to_move:
    boxes[1].append(item)

# Put the cow into Box 5.
boxes[5].append('cow')

# Move the moon from Box 3 to Box 1.
boxes[3].remove('moon')
boxes[1].append('moon')

# Remove the cow from Box 5.
boxes[5].remove('cow')

# Move the cloud and the branch and the note from Box 6 to Box 0.
items_to_move = ['cloud', 'branch', 'note']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[0].append(item)

# Move the hat from Box 1 to Box 6.
boxes[1].remove('hat')
boxes[6].append('hat')

# Swap the mixer in Box 3 with the hat in Box 6.
boxes[3].remove('mixer')
boxes[6].remove('hat')
boxes[3].append('hat')
boxes[6].append('mixer')

# Replace the book with the bicycle in Box 6.
boxes[6].remove('book')
boxes[6].append('bicycle')

# Remove the bicycle and the mixer from Box 6.
boxes[6].remove('bicycle')
boxes[6].remove('mixer')

# Replace the tape and the boot and the shorts with the mirror and the oven and the moon in Box 2.
boxes[2].remove('tape')
boxes[2].remove('boot')
boxes[2].remove('shorts')
boxes[2].append('mirror')
boxes[2].append('oven')
boxes[2].append('moon')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")