# Initial state of boxes
boxes = {
    0: ['sandals', 'laptop', 'console', 'blanket'],
    1: ['doll', 'wallet', 'toothpaste', 'pillow'],
    2: ['train', 'truck', 'branch', 'desert'],
    3: ['coral'],
    4: ['phone', 'chair'],
    5: ['key'],
    6: ['belt', 'scarf', 'lock', 'car', 'planet'],
    7: ['bell'],
    8: ['pot'],
    9: ['blender', 'tiger'],
    10: ['watch', 'card', 'basket', 'elephant', 'lipstick'],
    11: ['river']
}

# Swap the pillow in Box 1 with the planet in Box 6.
boxes[1].remove('pillow')
boxes[6].remove('planet')
boxes[1].append('planet')
boxes[6].append('pillow')

# Empty Box 5.
boxes[5] = []

# Replace the tiger and the blender with the harmonica and the vase in Box 9.
boxes[9].remove('tiger')
boxes[9].remove('blender')
boxes[9].append('harmonica')
boxes[9].append('vase')

# Replace the wallet and the doll and the toothpaste with the scarf and the whistle and the microwave in Box 1.
boxes[1].remove('wallet')
boxes[1].remove('doll')
boxes[1].remove('toothpaste')
boxes[1].append('scarf')
boxes[1].append('whistle')
boxes[1].append('microwave')

# Put the drum into Box 5.
boxes[5].append('drum')

# Remove the desert and the branch from Box 2.
boxes[2].remove('desert')
boxes[2].remove('branch')

# Empty Box 11.
boxes[11] = []

# Replace the bell with the sock in Box 7.
boxes[7].remove('bell')
boxes[7].append('sock')

# Move the chair and the phone from Box 4 to Box 11.
boxes[4].remove('chair')
boxes[4].remove('phone')
boxes[11].append('chair')
boxes[11].append('phone')

# Swap the scarf in Box 6 with the drum in Box 5.
boxes[6].remove('scarf')
boxes[5].remove('drum')
boxes[6].append('drum')
boxes[5].append('scarf')

# Replace the blanket with the camera in Box 0.
boxes[0].remove('blanket')
boxes[0].append('camera')

# Swap the truck in Box 2 with the drum in Box 6.
boxes[2].remove('truck')
boxes[6].remove('drum')
boxes[2].append('drum')
boxes[6].append('truck')

# Remove the lock from Box 6.
boxes[6].remove('lock')

# Put the mask and the bracelet and the pot into Box 0.
boxes[0].append('mask')
boxes[0].append('bracelet')
boxes[0].append('pot')

# Swap the planet in Box 1 with the drum in Box 2.
boxes[1].remove('planet')
boxes[2].remove('drum')
boxes[1].append('drum')
boxes[2].append('planet')

# Replace the sock with the dice in Box 7.
boxes[7].remove('sock')
boxes[7].append('dice')

# Put the candle into Box 0.
boxes[0].append('candle')

# Remove the card from Box 10.
boxes[10].remove('card')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")