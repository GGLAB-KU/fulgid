# Initial state of boxes
boxes = {
    0: ['table', 'helmet'],
    1: ['bag', 'belt', 'shirt', 'flute', 'needle'],
    2: ['desert', 'lion'],
    3: ['cat', 'key', 'controller', 'horn', 'toothpaste'],
    4: ['bell', 'keyboard', 'bird', 'horse'],
    5: [],
    6: ['chair', 'leaf', 'perfume']
}

# Remove the perfume and the leaf and the chair from Box 6.
boxes[6].remove('perfume')
boxes[6].remove('leaf')
boxes[6].remove('chair')

# Move the bird from Box 4 to Box 1.
boxes[4].remove('bird')
boxes[1].append('bird')

# Move the controller and the cat and the toothpaste from Box 3 to Box 5.
items_to_move = ['controller', 'cat', 'toothpaste']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[5].append(item)

# Replace the helmet with the fish in Box 0.
boxes[0].remove('helmet')
boxes[0].append('fish')

# Remove the desert and the lion from Box 2.
boxes[2].remove('desert')
boxes[2].remove('lion')

# Put the glove and the submarine into Box 6.
boxes[6].append('glove')
boxes[6].append('submarine')

# Put the card into Box 0.
boxes[0].append('card')

# Remove the horn from Box 3.
boxes[3].remove('horn')

# Remove the belt and the flute from Box 1.
boxes[1].remove('belt')
boxes[1].remove('flute')

# Put the storm into Box 6.
boxes[6].append('storm')

# Remove the table and the card and the fish from Box 0.
items_to_remove = ['table', 'card', 'fish']
for item in items_to_remove:
    boxes[0].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")