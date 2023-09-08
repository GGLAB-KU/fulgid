# Initial state of boxes
boxes = {
    0: ['dress', 'laptop', 'perfume', 'candle', 'rock'],
    1: ['hat'],
    2: [],
    3: [],
    4: ['toaster'],
    5: [],
    6: ['book', 'tape', 'fork', 'camera', 'comet'],
    7: ['console', 'paint', 'elephant', 'glove', 'controller'],
    8: [],
    9: ['headphone', 'soap'],
    10: [],
    11: []
}

# Remove the hat from Box 1.
boxes[1].remove('hat')

# Move the camera from Box 6 to Box 4.
boxes[6].remove('camera')
boxes[4].append('camera')

# Replace the headphone and the soap with the tree and the piano in Box 9.
boxes[9].remove('headphone')
boxes[9].remove('soap')
boxes[9].append('tree')
boxes[9].append('piano')

# Replace the console and the elephant and the controller with the candle and the guitar and the cat in Box 7.
boxes[7].remove('console')
boxes[7].remove('elephant')
boxes[7].remove('controller')
boxes[7].append('candle')
boxes[7].append('guitar')
boxes[7].append('cat')

# Replace the tape and the book with the candle and the ocean in Box 6.
boxes[6].remove('tape')
boxes[6].remove('book')
boxes[6].append('candle')
boxes[6].append('ocean')

# Put the zipper into Box 11.
boxes[11].append('zipper')

# Move the camera and the toaster from Box 4 to Box 3.
boxes[4].remove('camera')
boxes[4].remove('toaster')
boxes[3].append('camera')
boxes[3].append('toaster')

# Put the dog into Box 0.
boxes[0].append('dog')

# Put the skirt into Box 7.
boxes[7].append('skirt')

# Remove the toaster from Box 3.
boxes[3].remove('toaster')

# Swap the candle in Box 6 with the zipper in Box 11.
boxes[6].remove('candle')
boxes[11].remove('zipper')
boxes[6].append('zipper')
boxes[11].append('candle')

# Empty Box 7.
boxes[7] = []

# Put the flower and the needle into Box 11.
boxes[11].append('flower')
boxes[11].append('needle')

# Remove the camera from Box 3.
boxes[3].remove('camera')

# Swap the zipper in Box 6 with the piano in Box 9.
boxes[6].remove('zipper')
boxes[9].remove('piano')
boxes[6].append('piano')
boxes[9].append('zipper')

# Put the makeup and the shirt into Box 9.
boxes[9].append('makeup')
boxes[9].append('shirt')

# Swap the comet in Box 6 with the candle in Box 11.
boxes[6].remove('comet')
boxes[11].remove('candle')
boxes[6].append('candle')
boxes[11].append('comet')

# Move the piano from Box 6 to Box 7.
boxes[6].remove('piano')
boxes[7].append('piano')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")