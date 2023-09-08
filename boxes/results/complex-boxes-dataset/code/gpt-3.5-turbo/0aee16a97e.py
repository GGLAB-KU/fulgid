# Initial state of boxes
boxes = {
    0: ['game', 'hat', 'headphone'],
    1: ['brush', 'ship', 'grinder', 'spoon', 'desert'],
    2: [],
    3: [],
    4: ['wig', 'moon', 'plate', 'zipper', 'console'],
    5: ['needle', 'candle', 'gloves', 'sock', 'glasses'],
    6: ['microwave', 'keyboard', 'coin', 'card', 'motorcycle'],
    7: ['mountain', 'necklace', 'truck', 'beach', 'shampoo'],
    8: ['bracelet', 'camera'],
    9: ['island', 'apple', 'coral', 'lamp'],
    10: ['dress'],
    11: ['phone']
}

# Remove the coral and the lamp and the apple from Box 9.
items_to_remove = ['coral', 'lamp', 'apple']
for item in items_to_remove:
    boxes[9].remove(item)

# Move the ship and the desert from Box 1 to Box 8.
items_to_move = ['ship', 'desert']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[8].append(item)

# Put the submarine into Box 4.
boxes[4].append('submarine')

# Move the beach and the shampoo from Box 7 to Box 6.
items_to_move = ['beach', 'shampoo']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[6].append(item)

# Empty Box 8.
boxes[8] = []

# Replace the brush and the spoon with the magnet and the needle in Box 1.
boxes[1].remove('brush')
boxes[1].remove('spoon')
boxes[1].append('magnet')
boxes[1].append('needle')

# Swap the mountain in Box 7 with the phone in Box 11.
boxes[7].remove('mountain')
boxes[11].remove('phone')
boxes[7].append('phone')
boxes[11].append('mountain')

# Replace the island with the needle in Box 9.
boxes[9].remove('island')
boxes[9].append('needle')

# Move the grinder and the magnet from Box 1 to Box 4.
items_to_move = ['grinder', 'magnet']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Replace the needle with the lamp in Box 9.
boxes[9].remove('needle')
boxes[9].append('lamp')

# Replace the magnet and the plate and the console with the bicycle and the flute and the pan in Box 4.
boxes[4].remove('magnet')
boxes[4].remove('plate')
boxes[4].remove('console')
boxes[4].append('bicycle')
boxes[4].append('flute')
boxes[4].append('pan')

# Remove the candle from Box 5.
boxes[5].remove('candle')

# Swap the sock in Box 5 with the game in Box 0.
boxes[5].remove('sock')
boxes[0].remove('game')
boxes[5].append('game')
boxes[0].append('sock')

# Put the console and the swimsuit into Box 8.
boxes[8].append('console')
boxes[8].append('swimsuit')

# Put the basket and the mountain into Box 6.
boxes[6].append('basket')
boxes[6].append('mountain')

# Move the console from Box 8 to Box 7.
boxes[8].remove('console')
boxes[7].append('console')

# Move the phone from Box 7 to Box 11.
boxes[7].remove('phone')
boxes[11].append('phone')

# Swap the necklace in Box 7 with the lamp in Box 9.
boxes[7].remove('necklace')
boxes[9].remove('lamp')
boxes[7].append('lamp')
boxes[9].append('necklace')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")