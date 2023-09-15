box = {
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

# Remove the hat from Box 1
box[1].remove('hat')

# Move the camera from Box 6 to Box 4
box[4].append(box[6].pop(box[6].index('camera')))

# Replace the headphone and the soap with the tree and the piano in Box 9
box[9].remove('headphone')
box[9].remove('soap')
box[9].extend(['tree', 'piano'])

# Replace the console and the elephant and the controller with the candle and the guitar and the cat in Box 7
box[7].remove('console')
box[7].remove('elephant')
box[7].remove('controller')
box[7].extend(['candle', 'guitar', 'cat'])

# Replace the tape and the book with the candle and the ocean in Box 6
box[6].remove('tape')
box[6].remove('book')
box[6].extend(['candle', 'ocean'])

# Put the zipper into Box 11
box[11].append('zipper')

# Move the camera and the toaster from Box 4 to Box 3
box[3].extend([box[4].pop(box[4].index('camera')), box[4].pop(box[4].index('toaster'))])

# Put the dog into Box 0
box[0].append('dog')

# Put the skirt into Box 7
box[7].append('skirt')

# Remove the toaster from Box 3
box[3].remove('toaster')

# Swap the candle in Box 6 with the zipper in Box 11
box[6].remove('candle')
box[11].remove('zipper')
box[6].append('zipper')
box[11].append('candle')

# Empty Box 7
box[7] = []

# Put the flower and the needle into Box 11
box[11].extend(['flower', 'needle'])

# Remove the camera from Box 3
box[3].remove('camera')

# Swap the zipper in Box 6 with the piano in Box 9
box[6].remove('zipper')
box[9].remove('piano')
box[6].append('piano')
box[9].append('zipper')

# Put the makeup and the shirt into Box 9
box[9].extend(['makeup', 'shirt'])

# Swap the comet in Box 6 with the candle in Box 11
box[6].remove('comet')
box[11].remove('candle')
box[6].append('candle')
box[11].append('comet')

# Move the piano from Box 6 to Box 7
box[7].append(box[6].pop(box[6].index('piano')))

# Print the contents of each box
for i in range(12):
    print(f"Box {i}: {box[i]}")