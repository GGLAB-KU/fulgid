# Initial state of boxes
boxes = {
    0: [],
    1: ['boot', 'star'],
    2: ['comet', 'note', 'horn'],
    3: ['flute', 'truck', 'piano', 'train', 'octopus'],
    4: [],
    5: [],
    6: ['sock', 'lamp', 'jacket', 'submarine', 'microscope'],
    7: ['mixer', 'boat'],
    8: ['spoon', 'starfish', 'fridge', 'makeup', 'bag'],
    9: ['magnet', 'glove']
}

# Remove the bag and the spoon and the fridge from Box 8.
boxes[8].remove('bag')
boxes[8].remove('spoon')
boxes[8].remove('fridge')

# Put the dress and the rock and the lipstick into Box 0.
boxes[0].append('dress')
boxes[0].append('rock')
boxes[0].append('lipstick')

# Replace the starfish with the mirror in Box 8.
boxes[8].remove('starfish')
boxes[8].append('mirror')

# Put the leaf and the bicycle and the frame into Box 9.
boxes[9].append('leaf')
boxes[9].append('bicycle')
boxes[9].append('frame')

# Put the plate into Box 4.
boxes[4].append('plate')

# Move the rock and the lipstick and the dress from Box 0 to Box 2.
items_to_move = ['rock', 'lipstick', 'dress']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Replace the mixer with the desert in Box 7.
boxes[7].remove('mixer')
boxes[7].append('desert')

# Swap the star in Box 1 with the submarine in Box 6.
boxes[1].remove('star')
boxes[6].remove('submarine')
boxes[1].append('submarine')
boxes[6].append('star')

# Put the starfish and the mountain and the button into Box 1.
boxes[1].append('starfish')
boxes[1].append('mountain')
boxes[1].append('button')

# Swap the frame in Box 9 with the sock in Box 6.
boxes[9].remove('frame')
boxes[6].remove('sock')
boxes[9].append('sock')
boxes[6].append('frame')

# Replace the boat and the desert with the truck and the branch in Box 7.
boxes[7].remove('boat')
boxes[7].remove('desert')
boxes[7].append('truck')
boxes[7].append('branch')

# Swap the piano in Box 3 with the magnet in Box 9.
boxes[3].remove('piano')
boxes[9].remove('magnet')
boxes[3].append('magnet')
boxes[9].append('piano')

# Swap the microscope in Box 6 with the truck in Box 3.
boxes[6].remove('microscope')
boxes[3].remove('truck')
boxes[6].append('truck')
boxes[3].append('microscope')

# Swap the mountain in Box 1 with the leaf in Box 9.
boxes[1].remove('mountain')
boxes[9].remove('leaf')
boxes[1].append('leaf')
boxes[9].append('mountain')

# Swap the boot in Box 1 with the plate in Box 4.
boxes[1].remove('boot')
boxes[4].remove('plate')
boxes[1].append('plate')
boxes[4].append('boot')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")