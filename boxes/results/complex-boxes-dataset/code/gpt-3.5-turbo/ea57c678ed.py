# Initial state of boxes
boxes = {
    0: ['moon', 'flower', 'bracelet', 'console'],
    1: [],
    2: [],
    3: ['earring', 'whistle'],
    4: ['submarine', 'microwave', 'charger'],
    5: ['apple', 'shoe', 'cloud', 'drum', 'seaweed'],
    6: ['grass'],
    7: ['razor', 'motorcycle'],
    8: ['sun', 'speaker', 'bell', 'comb'],
    9: ['star', 'horn', 'mirror', 'shorts', 'grinder'],
    10: ['watch', 'mask', 'telescope'],
    11: ['tape'],
    12: ['violin', 'sculpture'],
    13: ['lipstick', 'sandals']
}

# Put the watch into Box 7.
boxes[7].append('watch')

# Put the scarf and the lock into Box 11.
boxes[11].append('scarf')
boxes[11].append('lock')

# Remove the flower from Box 0.
boxes[0].remove('flower')

# Swap the sandals in Box 13 with the apple in Box 5.
boxes[13].remove('sandals')
boxes[5].remove('apple')
boxes[13].append('apple')
boxes[5].append('sandals')

# Move the charger and the microwave from Box 4 to Box 13.
items_to_move = ['charger', 'microwave']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[13].append(item)

# Move the apple and the microwave from Box 13 to Box 6.
items_to_move = ['apple', 'microwave']
for item in items_to_move:
    boxes[13].remove(item)
    boxes[6].append(item)

# Put the toothpaste into Box 5.
boxes[5].append('toothpaste')

# Swap the seaweed in Box 5 with the whistle in Box 3.
boxes[5].remove('seaweed')
boxes[3].remove('whistle')
boxes[5].append('whistle')
boxes[3].append('seaweed')

# Replace the charger with the coin in Box 13.
boxes[13].remove('charger')
boxes[13].append('coin')

# Move the whistle and the toothpaste from Box 5 to Box 1.
items_to_move = ['whistle', 'toothpaste']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[1].append(item)

# Move the console and the bracelet and the moon from Box 0 to Box 12.
items_to_move = ['console', 'bracelet', 'moon']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[12].append(item)

# Put the truck into Box 5.
boxes[5].append('truck')

# Remove the scarf and the lock and the tape from Box 11.
items_to_remove = ['scarf', 'lock', 'tape']
for item in items_to_remove:
    boxes[11].remove(item)

# Swap the seaweed in Box 3 with the bell in Box 8.
boxes[3].remove('seaweed')
boxes[8].remove('bell')
boxes[3].append('bell')
boxes[8].append('seaweed')

# Move the mirror and the grinder and the shorts from Box 9 to Box 12.
items_to_move = ['mirror', 'grinder', 'shorts']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[12].append(item)

# Empty Box 12.
boxes[12] = []

# Replace the horn and the star with the dolphin and the battery in Box 9.
boxes[9].remove('horn')
boxes[9].remove('star')
boxes[9].append('dolphin')
boxes[9].append('battery')

# Put the ocean and the skirt into Box 10.
boxes[10].append('ocean')
boxes[10].append('skirt')

# Put the truck into Box 13.
boxes[13].append('truck')

# Move the drum and the shoe from Box 5 to Box 6.
items_to_move = ['drum', 'shoe']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[6].append(item)

# Move the submarine from Box 4 to Box 10.
boxes[4].remove('submarine')
boxes[10].append('submarine')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")