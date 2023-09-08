# Initial state of boxes
boxes = {
    0: ['frame', 'pot', 'starfish', 'coat', 'mask'],
    1: ['note', 'boot', 'needle', 'toothbrush', 'branch'],
    2: ['ocean', 'meteor'],
    3: ['shark', 'candle', 'horn', 'swimsuit', 'beach'],
    4: ['laptop', 'rock', 'shoes', 'speaker', 'glasses'],
    5: ['sock'],
    6: ['mixer', 'tree', 'clock', 'shampoo', 'bell'],
    7: ['glove', 'dolphin', 'necklace', 'leaf', 'comb'],
    8: ['boat', 'wire', 'bicycle'],
    9: ['cat', 'freezer'],
    10: ['drum', 'microscope', 'blanket'],
    11: ['phone'],
    12: ['brush', 'toaster', 'vase', 'harmonica', 'bus'],
    13: ['apple', 'puzzle', 'plate', 'moon']
}

# Swap the laptop in Box 4 with the sock in Box 5.
boxes[4].remove('laptop')
boxes[5].remove('sock')
boxes[4].append('sock')
boxes[5].append('laptop')

# Swap the ocean in Box 2 with the harmonica in Box 12.
boxes[2].remove('ocean')
boxes[12].remove('harmonica')
boxes[2].append('harmonica')
boxes[12].append('ocean')

# Remove the frame and the coat from Box 0.
boxes[0].remove('frame')
boxes[0].remove('coat')

# Move the laptop from Box 5 to Box 12.
boxes[5].remove('laptop')
boxes[12].append('laptop')

# Swap the ocean in Box 12 with the drum in Box 10.
boxes[12].remove('ocean')
boxes[10].remove('drum')
boxes[12].append('drum')
boxes[10].append('ocean')

# Move the leaf and the comb and the necklace from Box 7 to Box 3.
items_to_move = ['leaf', 'comb', 'necklace']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[3].append(item)

# Remove the starfish and the pot from Box 0.
boxes[0].remove('starfish')
boxes[0].remove('pot')

# Swap the freezer in Box 9 with the shampoo in Box 6.
boxes[9].remove('freezer')
boxes[6].remove('shampoo')
boxes[9].append('shampoo')
boxes[6].append('freezer')

# Move the apple from Box 13 to Box 12.
boxes[13].remove('apple')
boxes[12].append('apple')

# Move the ocean and the blanket from Box 10 to Box 4.
items_to_move = ['ocean', 'blanket']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[4].append(item)

# Swap the swimsuit in Box 3 with the needle in Box 1.
boxes[3].remove('swimsuit')
boxes[1].remove('needle')
boxes[3].append('needle')
boxes[1].append('swimsuit')

# Replace the microscope with the apple in Box 10.
boxes[10].remove('microscope')
boxes[10].append('apple')

# Remove the phone from Box 11.
boxes[11].remove('phone')

# Swap the leaf in Box 3 with the note in Box 1.
boxes[3].remove('leaf')
boxes[1].remove('note')
boxes[3].append('note')
boxes[1].append('leaf')

# Remove the dolphin and the glove from Box 7.
boxes[7].remove('dolphin')
boxes[7].remove('glove')

# Replace the boat and the bicycle and the wire with the puzzle and the pen and the necklace in Box 8.
boxes[8].remove('boat')
boxes[8].remove('bicycle')
boxes[8].remove('wire')
boxes[8].append('puzzle')
boxes[8].append('pen')
boxes[8].append('necklace')

# Swap the cat in Box 9 with the mask in Box 0.
boxes[9].remove('cat')
boxes[0].remove('mask')
boxes[9].append('mask')
boxes[0].append('cat')

# Swap the pen in Box 8 with the moon in Box 13.
boxes[8].remove('pen')
boxes[13].remove('moon')
boxes[8].append('moon')
boxes[13].append('pen')

# Remove the shampoo from Box 9.
boxes[9].remove('shampoo')

# Swap the leaf in Box 1 with the mask in Box 9.
boxes[1].remove('leaf')
boxes[9].remove('mask')
boxes[1].append('mask')
boxes[9].append('leaf')

# Remove the tree and the freezer and the mixer from Box 6.
boxes[6].remove('tree')
boxes[6].remove('freezer')
boxes[6].remove('mixer')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")