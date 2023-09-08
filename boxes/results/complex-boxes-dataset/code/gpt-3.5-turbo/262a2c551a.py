# Initial state of boxes
boxes = {
    0: ['cat', 'button', 'key'],
    1: [],
    2: ['shorts', 'rain', 'blanket'],
    3: ['coral', 'pot', 'note', 'plane'],
    4: ['sandals'],
    5: ['mirror', 'oven'],
    6: ['wallet', 'cow', 'fork', 'desert', 'glasses'],
    7: ['comb', 'usb', 'vase', 'watch', 'mountain'],
    8: ['jungle', 'island', 'charger', 'zipper', 'tie'],
    9: ['glove', 'octopus', 'wire'],
    10: ['freezer', 'swimsuit', 'fish'],
    11: ['jacket', 'storm', 'sculpture'],
    12: ['doll']
}

# Put the flower and the polish into Box 5.
boxes[5].append('flower')
boxes[5].append('polish')

# Move the blanket and the shorts and the rain from Box 2 to Box 0.
items_to_move = ['blanket', 'shorts', 'rain']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Move the cat and the rain and the button from Box 0 to Box 8.
items_to_move = ['cat', 'rain', 'button']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[8].append(item)

# Swap the doll in Box 12 with the flower in Box 5.
boxes[12], boxes[5] = boxes[5], boxes[12]

# Replace the fish with the microwave in Box 10.
boxes[10].remove('fish')
boxes[10].append('microwave')

# Swap the vase in Box 7 with the cow in Box 6.
boxes[7], boxes[6] = boxes[6], boxes[7]

# Move the mirror and the oven and the doll from Box 5 to Box 9.
items_to_move = ['mirror', 'oven', 'doll']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[9].append(item)

# Swap the fork in Box 6 with the swimsuit in Box 10.
boxes[6], boxes[10] = boxes[10], boxes[6]

# Put the basket and the seaweed into Box 8.
boxes[8].append('basket')
boxes[8].append('seaweed')

# Replace the mountain and the cow with the shark and the shorts in Box 7.
boxes[7].remove('mountain')
boxes[7].remove('cow')
boxes[7].append('shark')
boxes[7].append('shorts')

# Remove the desert and the swimsuit from Box 6.
boxes[6].remove('desert')
boxes[6].remove('swimsuit')

# Put the wallet into Box 9.
boxes[9].append('wallet')

# Put the fork into Box 7.
boxes[7].append('fork')

# Move the shorts and the blanket from Box 0 to Box 2.
items_to_move = ['shorts', 'blanket']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Remove the key from Box 0.
boxes[0].remove('key')

# Move the cat from Box 8 to Box 10.
boxes[8].remove('cat')
boxes[10].append('cat')

# Swap the vase in Box 6 with the glove in Box 9.
boxes[6], boxes[9] = boxes[9], boxes[6]

# Move the blanket from Box 2 to Box 10.
boxes[2].remove('blanket')
boxes[10].append('blanket')

# Replace the usb and the comb with the rocket and the shirt in Box 7.
boxes[7].remove('usb')
boxes[7].remove('comb')
boxes[7].append('rocket')
boxes[7].append('shirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")