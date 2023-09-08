# Initial state of boxes
boxes = {
    0: ['candle', 'snow', 'puzzle'],
    1: ['comb', 'train', 'cow'],
    2: ['dice', 'pot', 'mirror', 'gloves'],
    3: ['guitar', 'octopus', 'leaf', 'coral'],
    4: ['wire', 'magnet', 'key', 'toaster'],
    5: ['doll', 'fish', 'pants', 'tiger']
}

# Replace the tiger and the fish and the pants with the doll and the camera and the fridge in Box 5.
boxes[5].remove('tiger')
boxes[5].remove('fish')
boxes[5].remove('pants')
boxes[5].append('doll')
boxes[5].append('camera')
boxes[5].append('fridge')

# Replace the puzzle and the snow and the candle with the controller and the bowl and the bear in Box 0.
boxes[0].remove('puzzle')
boxes[0].remove('snow')
boxes[0].remove('candle')
boxes[0].append('controller')
boxes[0].append('bowl')
boxes[0].append('bear')

# Swap the key in Box 4 with the guitar in Box 3.
boxes[4].remove('key')
boxes[3].remove('guitar')
boxes[4].append('guitar')
boxes[3].append('key')

# Put the thunder and the pants into Box 0.
boxes[0].append('thunder')
boxes[0].append('pants')

# Replace the gloves and the pot and the dice with the shirt and the ocean and the swimsuit in Box 2.
boxes[2].remove('gloves')
boxes[2].remove('pot')
boxes[2].remove('dice')
boxes[2].append('shirt')
boxes[2].append('ocean')
boxes[2].append('swimsuit')

# Remove the thunder and the pants from Box 0.
boxes[0].remove('thunder')
boxes[0].remove('pants')

# Swap the controller in Box 0 with the toaster in Box 4.
boxes[0].remove('controller')
boxes[4].remove('toaster')
boxes[0].append('toaster')
boxes[4].append('controller')

# Replace the wire with the wig in Box 4.
boxes[4].remove('wire')
boxes[4].append('wig')

# Put the octopus and the bear and the dog into Box 2.
boxes[2].append('octopus')
boxes[2].append('bear')
boxes[2].append('dog')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")