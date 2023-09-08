# Initial state of boxes
boxes = {
    0: ['gloves', 'pen', 'desert', 'bowl', 'jungle'],
    1: ['elephant', 'chair', 'piano', 'cow'],
    2: ['rocket', 'razor', 'bracelet', 'bag'],
    3: ['fish', 'butterfly', 'sandals'],
    4: ['jacket', 'wallet', 'table', 'bicycle'],
    5: ['moon', 'pot', 'clock', 'dolphin', 'necklace'],
    6: ['mixer', 'swimsuit', 'coral', 'card'],
    7: ['mask', 'flute', 'skirt', 'beach'],
    8: ['plane', 'lock', 'perfume', 'pants'],
    9: ['shampoo', 'camera']
}

# Move the cow and the elephant and the piano from Box 1 to Box 0.
items_to_move = ['cow', 'elephant', 'piano']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[0].append(item)

# Move the chair from Box 1 to Box 5.
boxes[1].remove('chair')
boxes[5].append('chair')

# Empty Box 8.
boxes[8] = []

# Remove the cow from Box 0.
boxes[0].remove('cow')

# Move the piano and the jungle and the gloves from Box 0 to Box 9.
items_to_move = ['piano', 'jungle', 'gloves']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[9].append(item)

# Remove the elephant from Box 0.
boxes[0].remove('elephant')

# Swap the bicycle in Box 4 with the rocket in Box 2.
boxes[4].remove('bicycle')
boxes[2].remove('rocket')
boxes[4].append('rocket')
boxes[2].append('bicycle')

# Replace the mask and the skirt and the flute with the camera and the snow and the boot in Box 7.
boxes[7].remove('mask')
boxes[7].remove('skirt')
boxes[7].remove('flute')
boxes[7].append('camera')
boxes[7].append('snow')
boxes[7].append('boot')

# Remove the pen and the desert from Box 0.
boxes[0].remove('pen')
boxes[0].remove('desert')

# Remove the bowl from Box 0.
boxes[0].remove('bowl')

# Replace the necklace and the pot with the beach and the scarf in Box 5.
boxes[5].remove('necklace')
boxes[5].remove('pot')
boxes[5].append('beach')
boxes[5].append('scarf')

# Remove the snow and the boot and the camera from Box 7.
boxes[7].remove('snow')
boxes[7].remove('boot')
boxes[7].remove('camera')

# Empty Box 6.
boxes[6] = []

# Remove the fish from Box 3.
boxes[3].remove('fish')

# Move the bracelet from Box 2 to Box 8.
boxes[2].remove('bracelet')
boxes[8].append('bracelet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")