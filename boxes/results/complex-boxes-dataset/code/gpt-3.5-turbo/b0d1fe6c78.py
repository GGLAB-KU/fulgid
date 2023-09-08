# Initial state of boxes
boxes = {
    0: [],
    1: ['fish'],
    2: ['sandals', 'tiger', 'flute'],
    3: ['zipper', 'belt', 'cat'],
    4: ['makeup', 'dog', 'horn'],
    5: ['drum', 'spoon', 'blender'],
    6: [],
    7: []
}

# Swap the fish in Box 1 with the sandals in Box 2.
boxes[1].remove('fish')
boxes[2].remove('sandals')
boxes[1].append('sandals')
boxes[2].append('fish')

# Put the cloud and the basket and the guitar into Box 1.
items_to_add = ['cloud', 'basket', 'guitar']
for item in items_to_add:
    boxes[1].append(item)

# Swap the makeup in Box 4 with the drum in Box 5.
boxes[4].remove('makeup')
boxes[5].remove('drum')
boxes[4].append('drum')
boxes[5].append('makeup')

# Replace the zipper and the belt and the cat with the ring and the plane and the bicycle in Box 3.
boxes[3].remove('zipper')
boxes[3].remove('belt')
boxes[3].remove('cat')
boxes[3].append('ring')
boxes[3].append('plane')
boxes[3].append('bicycle')

# Move the drum and the horn and the dog from Box 4 to Box 6.
items_to_move = ['drum', 'horn', 'dog']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[6].append(item)

# Swap the flute in Box 2 with the ring in Box 3.
boxes[2].remove('flute')
boxes[3].remove('ring')
boxes[2].append('ring')
boxes[3].append('flute')

# Replace the cloud and the guitar with the toothbrush and the sandals in Box 1.
boxes[1].remove('cloud')
boxes[1].remove('guitar')
boxes[1].append('toothbrush')
boxes[1].append('sandals')

# Move the tiger and the fish from Box 2 to Box 3.
items_to_move = ['tiger', 'fish']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Replace the toothbrush and the sandals and the sandals with the shark and the ship and the desert in Box 1.
boxes[1].remove('toothbrush')
boxes[1].remove('sandals')
boxes[1].remove('sandals')
boxes[1].append('shark')
boxes[1].append('ship')
boxes[1].append('desert')

# Remove the dog and the horn and the drum from Box 6.
items_to_remove = ['dog', 'horn', 'drum']
for item in items_to_remove:
    boxes[6].remove(item)

# Move the ring from Box 2 to Box 3.
boxes[2].remove('ring')
boxes[3].append('ring')

# Replace the shark with the candle in Box 1.
boxes[1].remove('shark')
boxes[1].append('candle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")