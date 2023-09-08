# Initial state of boxes
boxes = {
    0: [],
    1: ['wire'],
    2: ['snow', 'comb'],
    3: ['glove', 'fridge', 'skirt', 'table', 'cloud'],
    4: ['pillow', 'cow'],
    5: ['battery', 'dice'],
    6: ['pen', 'lipstick', 'flute'],
    7: ['octopus', 'console'],
    8: ['umbrella'],
    9: ['toothbrush', 'boot'],
    10: ['phone', 'island', 'puzzle', 'moon']
}

# Put the car and the cup and the sun into Box 5.
items_to_put = ['car', 'cup', 'sun']
for item in items_to_put:
    boxes[5].append(item)

# Move the console from Box 7 to Box 4.
boxes[4].append(boxes[7].pop(boxes[7].index('console')))

# Put the keyboard and the motorcycle into Box 4.
items_to_put = ['keyboard', 'motorcycle']
for item in items_to_put:
    boxes[4].append(item)

# Move the wire from Box 1 to Box 7.
boxes[7].append(boxes[1].pop())

# Remove the island and the phone from Box 10.
boxes[10].remove('island')
boxes[10].remove('phone')

# Swap the moon in Box 10 with the octopus in Box 7.
boxes[10].remove('moon')
boxes[7].remove('octopus')
boxes[10].append('octopus')
boxes[7].append('moon')

# Swap the pen in Box 6 with the cloud in Box 3.
boxes[6].remove('pen')
boxes[3].remove('cloud')
boxes[6].append('cloud')
boxes[3].append('pen')

# Put the comb into Box 10.
boxes[10].append('comb')

# Replace the cloud and the flute with the guitar and the polish in Box 6.
boxes[6].remove('cloud')
boxes[6].remove('flute')
boxes[6].append('guitar')
boxes[6].append('polish')

# Empty Box 5.
boxes[5] = []

# Put the comb into Box 9.
boxes[9].append('comb')

# Put the toothpaste into Box 0.
boxes[0].append('toothpaste')

# Put the perfume and the microwave and the bicycle into Box 4.
items_to_put = ['perfume', 'microwave', 'bicycle']
for item in items_to_put:
    boxes[4].append(item)

# Move the glove and the skirt from Box 3 to Box 9.
items_to_move = ['glove', 'skirt']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[9].append(item)

# Replace the wire with the seaweed in Box 7.
boxes[7].remove('wire')
boxes[7].append('seaweed')

# Replace the motorcycle with the submarine in Box 4.
boxes[4].remove('motorcycle')
boxes[4].append('submarine')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")