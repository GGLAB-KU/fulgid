# Initial state of boxes
boxes = {
    0: [],
    1: ['bird', 'coin', 'dog', 'speaker'],
    2: ['scissors', 'flute', 'shark', 'flower', 'candle'],
    3: ['mirror'],
    4: [],
    5: [],
    6: ['pan', 'pen', 'blanket', 'spoon'],
    7: ['ocean', 'mountain', 'glove', 'tape', 'ship'],
    8: ['cow', 'beach', 'drum', 'wire'],
    9: ['tie', 'cat', 'crown', 'doll', 'vase'],
    10: ['sculpture', 'gloves', 'motorcycle'],
    11: ['watch'],
    12: ['ring', 'swimsuit'],
    13: ['belt', 'shoes', 'coral'],
    14: ['dolphin', 'scarf', 'tree']
}

# Move the blanket and the spoon and the pan from Box 6 to Box 11.
items_to_move = ['blanket', 'spoon', 'pan']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[11].append(item)

# Remove the tree and the dolphin and the scarf from Box 14.
items_to_remove = ['tree', 'dolphin', 'scarf']
for item in items_to_remove:
    boxes[14].remove(item)

# Move the drum from Box 8 to Box 3.
boxes[8].remove('drum')
boxes[3].append('drum')

# Swap the coin in Box 1 with the spoon in Box 11.
boxes[1].remove('coin')
boxes[11].remove('spoon')
boxes[1].append('spoon')
boxes[11].append('coin')

# Put the shampoo and the microscope into Box 7.
boxes[7].extend(['shampoo', 'microscope'])

# Replace the gloves and the sculpture with the glove and the leaf in Box 10.
boxes[10].remove('gloves')
boxes[10].remove('sculpture')
boxes[10].append('glove')
boxes[10].append('leaf')

# Put the spoon into Box 8.
boxes[8].append('spoon')

# Remove the tape from Box 7.
boxes[7].remove('tape')

# Move the tie and the doll and the cat from Box 9 to Box 6.
items_to_move = ['tie', 'doll', 'cat']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[6].append(item)

# Swap the swimsuit in Box 12 with the coral in Box 13.
boxes[12].remove('swimsuit')
boxes[13].remove('coral')
boxes[12].append('coral')
boxes[13].append('swimsuit')

# Remove the coral from Box 12.
boxes[12].remove('coral')

# Put the piano and the laptop and the bracelet into Box 13.
boxes[13].extend(['piano', 'laptop', 'bracelet'])

# Put the blender and the key and the bag into Box 13.
boxes[13].extend(['blender', 'key', 'bag'])

# Swap the ring in Box 12 with the bird in Box 1.
boxes[12].remove('ring')
boxes[1].remove('bird')
boxes[12].append('bird')
boxes[1].append('ring')

# Put the dress into Box 10.
boxes[10].append('dress')

# Put the elephant and the sun and the sculpture into Box 0.
boxes[0].extend(['elephant', 'sun', 'sculpture'])

# Put the towel and the plate into Box 7.
boxes[7].extend(['towel', 'plate'])

# Put the microscope and the bus into Box 8.
boxes[8].extend(['microscope', 'bus'])

# Put the wire into Box 4.
boxes[4].append('wire')

# Move the bus and the wire and the cow from Box 8 to Box 12.
items_to_move = ['bus', 'wire', 'cow']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[12].append(item)

# Remove the drum and the mirror from Box 3.
boxes[3].remove('drum')
boxes[3].remove('mirror')

# Empty Box 0.
boxes[0] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")