# Initial state of boxes
boxes = {
    0: ['shirt', 'rain', 'puzzle', 'wig'],
    1: [],
    2: [],
    3: ['grass'],
    4: ['octopus', 'wallet', 'moon', 'umbrella', 'cat'],
    5: [],
    6: ['flower', 'helmet', 'coral'],
    7: ['bag', 'bell', 'toy'],
    8: [],
    9: [],
    10: ['jungle', 'dress', 'perfume'],
    11: ['drum'],
    12: ['fridge', 'towel', 'shampoo', 'truck'],
    13: ['usb']
}

# Put the card into Box 13.
boxes[13].append('card')

# Replace the flower with the perfume in Box 6.
boxes[6].remove('flower')
boxes[6].append('perfume')

# Replace the usb with the comet in Box 13.
boxes[13].remove('usb')
boxes[13].append('comet')

# Swap the jungle in Box 10 with the helmet in Box 6.
boxes[10].remove('jungle')
boxes[6].remove('helmet')
boxes[10].append('helmet')
boxes[6].append('jungle')

# Put the hat into Box 0.
boxes[0].append('hat')

# Put the shelf into Box 6.
boxes[6].append('shelf')

# Move the wig and the rain and the hat from Box 0 to Box 8.
items_to_move = ['wig', 'rain', 'hat']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[8].append(item)

# Put the spoon and the mask and the mountain into Box 10.
items_to_put = ['spoon', 'mask', 'mountain']
for item in items_to_put:
    boxes[10].append(item)

# Swap the spoon in Box 10 with the drum in Box 11.
boxes[10].remove('spoon')
boxes[11].remove('drum')
boxes[10].append('drum')
boxes[11].append('spoon')

# Swap the grass in Box 3 with the spoon in Box 11.
boxes[3].remove('grass')
boxes[11].remove('spoon')
boxes[3].append('spoon')
boxes[11].append('grass')

# Put the lion and the console and the book into Box 4.
items_to_put = ['lion', 'console', 'book']
for item in items_to_put:
    boxes[4].append(item)

# Replace the jungle with the lightning in Box 6.
boxes[6].remove('jungle')
boxes[6].append('lightning')

# Swap the comet in Box 13 with the cat in Box 4.
boxes[13].remove('comet')
boxes[4].remove('cat')
boxes[13].append('cat')
boxes[4].append('comet')

# Replace the umbrella and the lion with the needle and the wig in Box 4.
boxes[4].remove('umbrella')
boxes[4].remove('lion')
boxes[4].append('needle')
boxes[4].append('wig')

# Move the wallet and the comet and the octopus from Box 4 to Box 3.
items_to_move = ['wallet', 'comet', 'octopus']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Remove the wig and the hat and the rain from Box 8.
items_to_remove = ['wig', 'hat', 'rain']
for item in items_to_remove:
    boxes[8].remove(item)

# Replace the dress and the drum with the lightning and the flute in Box 10.
boxes[10].remove('dress')
boxes[10].remove('drum')
boxes[10].append('lightning')
boxes[10].append('flute')

# Remove the card from Box 13.
boxes[13].remove('card')

# Replace the puzzle and the shirt with the jacket and the piano in Box 0.
boxes[0].remove('puzzle')
boxes[0].remove('shirt')
boxes[0].append('jacket')
boxes[0].append('piano')

# Put the sun into Box 6.
boxes[6].append('sun')

# Replace the jacket and the piano with the tiger and the controller in Box 0.
boxes[0].remove('jacket')
boxes[0].remove('piano')
boxes[0].append('tiger')
boxes[0].append('controller')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")