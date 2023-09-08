# Initial state of boxes
boxes = {
    0: ['submarine', 'car', 'sock', 'jacket', 'river'],
    1: ['button', 'leaf', 'boot', 'fridge', 'freezer'],
    2: ['candle', 'glove'],
    3: ['skirt'],
    4: ['scarf', 'cloud', 'telescope'],
    5: ['violin', 'train'],
    6: ['microscope'],
    7: ['moon', 'puzzle']
}

# Move the sock and the river from Box 0 to Box 1.
boxes[0].remove('sock')
boxes[0].remove('river')
boxes[1].append('sock')
boxes[1].append('river')

# Move the microscope from Box 6 to Box 5.
boxes[6].remove('microscope')
boxes[5].append('microscope')

# Empty Box 3.
boxes[3] = []

# Move the cloud and the telescope from Box 4 to Box 3.
boxes[4].remove('cloud')
boxes[4].remove('telescope')
boxes[3].append('cloud')
boxes[3].append('telescope')

# Move the candle and the glove from Box 2 to Box 3.
boxes[2].remove('candle')
boxes[2].remove('glove')
boxes[3].append('candle')
boxes[3].append('glove')

# Empty Box 5.
boxes[5] = []

# Remove the puzzle from Box 7.
boxes[7].remove('puzzle')

# Replace the jacket and the submarine and the car with the spoon and the comb and the cow in Box 0.
boxes[0].remove('jacket')
boxes[0].remove('submarine')
boxes[0].remove('car')
boxes[0].append('spoon')
boxes[0].append('comb')
boxes[0].append('cow')

# Swap the cow in Box 0 with the cloud in Box 3.
boxes[0].remove('cow')
boxes[3].remove('cloud')
boxes[0].append('cloud')
boxes[3].append('cow')

# Replace the sock and the freezer and the river with the ocean and the zipper and the spoon in Box 1.
boxes[1].remove('sock')
boxes[1].remove('freezer')
boxes[1].remove('river')
boxes[1].append('ocean')
boxes[1].append('zipper')
boxes[1].append('spoon')

# Move the scarf from Box 4 to Box 2.
boxes[4].remove('scarf')
boxes[2].append('scarf')

# Replace the scarf with the toothpaste in Box 2.
boxes[2].remove('scarf')
boxes[2].append('toothpaste')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")