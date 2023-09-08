# Initial state of boxes
boxes = {
    0: ['hat', 'lightning', 'needle', 'boat', 'sandals'],
    1: ['desert', 'comet', 'chair', 'table'],
    2: [],
    3: [],
    4: ['bracelet', 'frame', 'helmet', 'shoe', 'sun']
}

# Replace the helmet and the frame with the car and the planet in Box 4.
boxes[4].remove('helmet')
boxes[4].remove('frame')
boxes[4].append('car')
boxes[4].append('planet')

# Swap the desert in Box 1 with the needle in Box 0.
boxes[1].remove('desert')
boxes[0].remove('needle')
boxes[1].append('needle')
boxes[0].append('desert')

# Put the perfume and the shelf into Box 1.
boxes[1].append('perfume')
boxes[1].append('shelf')

# Move the sandals and the hat and the desert from Box 0 to Box 2.
items_to_move = ['sandals', 'hat', 'desert']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Remove the perfume and the table from Box 1.
boxes[1].remove('perfume')
boxes[1].remove('table')

# Remove the lightning and the boat from Box 0.
boxes[0].remove('lightning')
boxes[0].remove('boat')

# Remove the sun and the bracelet from Box 4.
boxes[4].remove('sun')
boxes[4].remove('bracelet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")