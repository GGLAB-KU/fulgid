# Initial state of boxes
boxes = {
    0: ['mask', 'scissors', 'thread', 'toaster'],
    1: [],
    2: ['wig'],
    3: ['rocket', 'flower'],
    4: ['shoe'],
    5: ['sun', 'cow', 'piano', 'elephant', 'note'],
    6: [],
    7: ['console', 'tiger', 'cat'],
    8: ['bicycle', 'necklace', 'storm', 'clock', 'plate'],
    9: ['zipper', 'blanket', 'pen', 'shirt', 'puzzle'],
    10: ['towel', 'crown', 'mountain', 'shorts', 'cup']
}

# Replace the shorts with the paint in Box 10.
boxes[10].remove('shorts')
boxes[10].append('paint')

# Empty Box 5.
boxes[5] = []

# Swap the cup in Box 10 with the cat in Box 7.
boxes[10].remove('cup')
boxes[7].remove('cat')
boxes[10].append('cat')
boxes[7].append('cup')

# Swap the tiger in Box 7 with the bicycle in Box 8.
boxes[7].remove('tiger')
boxes[8].remove('bicycle')
boxes[7].append('bicycle')
boxes[8].append('tiger')

# Move the plate and the necklace from Box 8 to Box 7.
boxes[8].remove('plate')
boxes[8].remove('necklace')
boxes[7].append('plate')
boxes[7].append('necklace')

# Put the river and the glasses and the sculpture into Box 1.
items_to_move = ['river', 'glasses', 'sculpture']
for item in items_to_move:
    boxes[1].append(item)

# Remove the shoe from Box 4.
boxes[4].remove('shoe')

# Move the mountain and the cat from Box 10 to Box 6.
boxes[10].remove('mountain')
boxes[10].remove('cat')
boxes[6].append('mountain')
boxes[6].append('cat')

# Remove the necklace and the bicycle from Box 7.
boxes[7].remove('necklace')
boxes[7].remove('bicycle')

# Swap the paint in Box 10 with the plate in Box 7.
boxes[10].remove('paint')
boxes[7].remove('plate')
boxes[10].append('plate')
boxes[7].append('paint')

# Remove the cat from Box 6.
boxes[6].remove('cat')

# Remove the wig from Box 2.
boxes[2].remove('wig')

# Remove the plate from Box 10.
boxes[10].remove('plate')

# Move the storm and the tiger from Box 8 to Box 0.
boxes[8].remove('storm')
boxes[8].remove('tiger')
boxes[0].append('storm')
boxes[0].append('tiger')

# Remove the toaster and the mask from Box 0.
boxes[0].remove('toaster')
boxes[0].remove('mask')

# Remove the cup and the console and the paint from Box 7.
boxes[7].remove('cup')
boxes[7].remove('console')
boxes[7].remove('paint')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")