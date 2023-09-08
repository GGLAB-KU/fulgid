# Initial state of boxes
boxes = {
    0: ['starfish', 'cat', 'keyboard', 'dog', 'bag'],
    1: ['toaster'],
    2: ['microscope', 'piano'],
    3: ['console', 'speaker', 'mask', 'island', 'motorcycle'],
    4: ['thread', 'tape', 'lion', 'shorts', 'storm'],
    5: ['mirror', 'beach', 'elephant', 'desert', 'glove'],
    6: ['coral', 'dress', 'fork', 'lamp'],
    7: [],
    8: ['spoon'],
    9: ['pen', 'clock'],
    10: ['oven', 'hat'],
    11: []
}

# Replace the pen with the shark in Box 9.
boxes[9].remove('pen')
boxes[9].append('shark')

# Replace the coral with the plane in Box 6.
boxes[6].remove('coral')
boxes[6].append('plane')

# Put the earring into Box 0.
boxes[0].append('earring')

# Put the grinder and the tape and the microwave into Box 1.
items_to_put = ['grinder', 'tape', 'microwave']
for item in items_to_put:
    boxes[1].append(item)

# Replace the bag and the dog with the pot and the ship in Box 0.
boxes[0].remove('bag')
boxes[0].remove('dog')
boxes[0].append('pot')
boxes[0].append('ship')

# Swap the hat in Box 10 with the console in Box 3.
boxes[10], boxes[3] = boxes[3], boxes[10]

# Replace the shark and the clock with the planet and the desert in Box 9.
boxes[9].remove('shark')
boxes[9].remove('clock')
boxes[9].append('planet')
boxes[9].append('desert')

# Swap the piano in Box 2 with the plane in Box 6.
boxes[2], boxes[6] = boxes[6], boxes[2]

# Swap the spoon in Box 8 with the planet in Box 9.
boxes[8], boxes[9] = boxes[9], boxes[8]

# Swap the beach in Box 5 with the plane in Box 2.
boxes[5], boxes[2] = boxes[2], boxes[5]

# Move the tape and the microwave from Box 1 to Box 8.
items_to_move = ['tape', 'microwave']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[8].append(item)

# Replace the microwave with the basket in Box 8.
boxes[8].remove('microwave')
boxes[8].append('basket')

# Empty Box 6.
boxes[6] = []

# Swap the pot in Box 0 with the oven in Box 10.
boxes[0], boxes[10] = boxes[10], boxes[0]

# Replace the glove and the plane and the elephant with the meteor and the razor and the star in Box 5.
boxes[5].remove('glove')
boxes[5].remove('plane')
boxes[5].remove('elephant')
boxes[5].append('meteor')
boxes[5].append('razor')
boxes[5].append('star')

# Put the cup and the star and the pants into Box 2.
items_to_put = ['cup', 'star', 'pants']
for item in items_to_put:
    boxes[2].append(item)

# Replace the toaster and the grinder with the perfume and the earring in Box 1.
boxes[1].remove('toaster')
boxes[1].remove('grinder')
boxes[1].append('perfume')
boxes[1].append('earring')

# Replace the star and the beach and the microscope with the violin and the scissors and the lock in Box 2.
boxes[2].remove('star')
boxes[2].remove('beach')
boxes[2].remove('microscope')
boxes[2].append('violin')
boxes[2].append('scissors')
boxes[2].append('lock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")