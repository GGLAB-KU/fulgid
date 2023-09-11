# Initial state of boxes
boxes = {
    0: ['bicycle'],
    1: [],
    2: ['toothpaste', 'pan', 'flower', 'fork'],
    3: ['shorts', 'meteor', 'microscope', 'telescope', 'rocket'],
    4: ['skirt'],
    5: ['clock', 'pot'],
    6: ['piano']
}

# Put the flute and the pen into Box 6.
boxes[6].append('flute')
boxes[6].append('pen')

# Replace the clock with the desert in Box 5.
boxes[5].remove('clock')
boxes[5].append('desert')

# Remove the pot and the desert from Box 5.
boxes[5].remove('pot')
boxes[5].remove('desert')

# Replace the flute and the pen with the pot and the laptop in Box 6.
boxes[6].remove('flute')
boxes[6].remove('pen')
boxes[6].append('pot')
boxes[6].append('laptop')

# Move the pan and the flower from Box 2 to Box 5.
items_to_move = ['pan', 'flower']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Move the skirt from Box 4 to Box 6.
boxes[4].remove('skirt')
boxes[6].append('skirt')

# Replace the pot with the toothpaste in Box 6.
boxes[6].remove('pot')
boxes[6].append('toothpaste')

# Move the toothpaste and the piano from Box 6 to Box 1.
boxes[6].remove('toothpaste')
boxes[6].remove('piano')
boxes[1].append('toothpaste')
boxes[1].append('piano')

# Replace the microscope and the rocket with the thread and the comet in Box 3.
boxes[3].remove('microscope')
boxes[3].remove('rocket')
boxes[3].append('thread')
boxes[3].append('comet')

# Empty Box 6.
boxes[6] = []

# Move the shorts and the comet and the meteor from Box 3 to Box 2.
items_to_move = ['shorts', 'comet', 'meteor']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")