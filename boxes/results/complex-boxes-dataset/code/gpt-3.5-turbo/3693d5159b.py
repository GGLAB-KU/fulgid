# Initial state of boxes
boxes = {
    0: ['console', 'button'],
    1: ['dress', 'glasses', 'whistle', 'jacket'],
    2: ['card', 'blanket'],
    3: ['ocean', 'zipper', 'frame', 'plane', 'scissors'],
    4: ['guitar', 'forest', 'shelf', 'pants', 'headphone'],
    5: [],
    6: ['lion', 'snow', 'desert', 'star', 'camera'],
    7: ['doll'],
    8: ['wire'],
    9: ['storm', 'brush', 'octopus', 'watch'],
    10: ['jungle', 'swimsuit', 'mask', 'tie', 'mixer'],
    11: ['leaf'],
    12: ['candle', 'sock', 'shampoo', 'bag'],
    13: ['starfish', 'branch', 'tree', 'mountain'],
    14: ['boat']
}

# Put the console into Box 5.
boxes[5].append('console')
boxes[0].remove('console')

# Remove the mountain and the branch and the starfish from Box 13.
items_to_remove = ['mountain', 'branch', 'starfish']
for item in items_to_remove:
    boxes[13].remove(item)

# Swap the boat in Box 14 with the ocean in Box 3.
boxes[14].remove('boat')
boxes[3].remove('ocean')
boxes[14].append('ocean')
boxes[3].append('boat')

# Move the ocean from Box 14 to Box 2.
boxes[14].remove('ocean')
boxes[2].append('ocean')

# Put the dog into Box 13.
boxes[13].append('dog')

# Replace the glasses and the jacket and the dress with the starfish and the forest and the horn in Box 1.
boxes[1].remove('glasses')
boxes[1].remove('jacket')
boxes[1].remove('dress')
boxes[1].append('starfish')
boxes[1].append('forest')
boxes[1].append('horn')

# Empty Box 3.
boxes[3] = []

# Replace the star and the camera with the harmonica and the violin in Box 6.
boxes[6].remove('star')
boxes[6].remove('camera')
boxes[6].append('harmonica')
boxes[6].append('violin')

# Put the car into Box 9.
boxes[9].append('car')

# Empty Box 6.
boxes[6] = []

# Replace the wire with the shelf in Box 8.
boxes[8].remove('wire')
boxes[8].append('shelf')

# Put the lipstick and the helmet and the microwave into Box 8.
boxes[8].append('lipstick')
boxes[8].append('helmet')
boxes[8].append('microwave')

# Move the doll from Box 7 to Box 1.
boxes[7].remove('doll')
boxes[1].append('doll')

# Move the leaf from Box 11 to Box 3.
boxes[11].remove('leaf')
boxes[3].append('leaf')

# Move the tie and the mask and the jungle from Box 10 to Box 1.
boxes[10].remove('tie')
boxes[10].remove('mask')
boxes[10].remove('jungle')
boxes[1].append('tie')
boxes[1].append('mask')
boxes[1].append('jungle')

# Put the jacket and the umbrella into Box 12.
boxes[12].append('jacket')
boxes[12].append('umbrella')

# Replace the console with the plane in Box 5.
boxes[5].remove('console')
boxes[5].append('plane')

# Move the shelf from Box 4 to Box 11.
boxes[4].remove('shelf')
boxes[11].append('shelf')

# Put the headphone into Box 0.
boxes[0].append('headphone')

# Put the glove and the toaster and the spoon into Box 14.
boxes[14].append('glove')
boxes[14].append('toaster')
boxes[14].append('spoon')

# Swap the card in Box 2 with the tree in Box 13.
boxes[2].remove('card')
boxes[13].remove('tree')
boxes[2].append('tree')
boxes[13].append('card')

# Move the umbrella and the bag and the sock from Box 12 to Box 0.
boxes[12].remove('umbrella')
boxes[12].remove('bag')
boxes[12].remove('sock')
boxes[0].append('umbrella')
boxes[0].append('bag')
boxes[0].append('sock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")