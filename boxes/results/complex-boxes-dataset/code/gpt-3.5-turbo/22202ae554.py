# Initial state of boxes
boxes = {
    0: ['chair'],
    1: [],
    2: ['doll', 'bicycle', 'violin', 'button'],
    3: ['headphone', 'ring', 'shampoo', 'oven', 'shoes'],
    4: ['submarine', 'shoe', 'lightning', 'octopus'],
    5: ['dice', 'sandals', 'rain', 'comb'],
    6: ['pot'],
    7: ['meteor'],
    8: ['truck'],
    9: ['brush', 'cat', 'car', 'mirror', 'guitar'],
    10: [],
    11: ['swimsuit', 'butterfly'],
    12: ['toaster', 'lock'],
    13: ['polish', 'spoon', 'clock', 'keyboard', 'console'],
    14: ['earring', 'pan', 'candle', 'zipper']
}

# Move the pot from Box 6 to Box 2.
boxes[6].remove('pot')
boxes[2].append('pot')

# Swap the shoe in Box 4 with the keyboard in Box 13.
boxes[4].remove('shoe')
boxes[13].remove('keyboard')
boxes[4].append('keyboard')
boxes[13].append('shoe')

# Replace the lock and the toaster with the cow and the soap in Box 12.
boxes[12].remove('lock')
boxes[12].remove('toaster')
boxes[12].append('cow')
boxes[12].append('soap')

# Remove the chair from Box 0.
boxes[0].remove('chair')

# Replace the car with the plane in Box 9.
boxes[9].remove('car')
boxes[9].append('plane')

# Put the razor into Box 13.
boxes[13].append('razor')

# Put the skirt into Box 1.
boxes[1].append('skirt')

# Move the pot and the violin and the doll from Box 2 to Box 0.
items_to_move = ['pot', 'violin', 'doll']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Move the sandals from Box 5 to Box 8.
boxes[5].remove('sandals')
boxes[8].append('sandals')

# Move the skirt from Box 1 to Box 8.
boxes[1].remove('skirt')
boxes[8].append('skirt')

# Move the candle and the zipper from Box 14 to Box 7.
boxes[14].remove('candle')
boxes[14].remove('zipper')
boxes[7].append('candle')
boxes[7].append('zipper')

# Move the butterfly and the swimsuit from Box 11 to Box 7.
boxes[11].remove('butterfly')
boxes[11].remove('swimsuit')
boxes[7].append('butterfly')
boxes[7].append('swimsuit')

# Put the lion and the frame into Box 1.
boxes[1].append('lion')
boxes[1].append('frame')

# Swap the pan with the zipper in Box 14.
boxes[14].remove('pan')
boxes[14].remove('zipper')
boxes[14].append('zipper')
boxes[14].append('pan')

# Move the cow and the soap from Box 12 to Box 2.
boxes[12].remove('cow')
boxes[12].remove('soap')
boxes[2].append('cow')
boxes[2].append('soap')

# Remove the lightning from Box 4.
boxes[4].remove('lightning')

# Remove the violin from Box 0.
boxes[0].remove('violin')

# Move the octopus from Box 4 to Box 7.
boxes[4].remove('octopus')
boxes[7].append('octopus')

# Swap the submarine in Box 4 with the earring in Box 14.
boxes[4].remove('submarine')
boxes[14].remove('earring')
boxes[4].append('earring')
boxes[14].append('submarine')

# Swap the pot in Box 0 with the console in Box 13.
boxes[0].remove('pot')
boxes[13].remove('console')
boxes[0].append('console')
boxes[13].append('pot')

# Remove the spoon and the shoe and the pot from Box 13.
boxes[13].remove('spoon')
boxes[13].remove('shoe')
boxes[13].remove('pot')

# Move the swimsuit and the meteor from Box 7 to Box 14.
boxes[7].remove('swimsuit')
boxes[7].remove('meteor')
boxes[14].append('swimsuit')
boxes[14].append('meteor')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")