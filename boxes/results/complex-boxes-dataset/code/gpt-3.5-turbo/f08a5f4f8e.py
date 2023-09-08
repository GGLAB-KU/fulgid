# Initial state of boxes
boxes = {
    0: ['gloves'],
    1: ['skirt', 'piano', 'speaker', 'wire'],
    2: ['crown', 'scarf', 'drum', 'microwave'],
    3: ['mountain', 'oven', 'wig', 'bear', 'shampoo'],
    4: [],
    5: ['flower', 'rock', 'umbrella', 'candle', 'grinder'],
    6: [],
    7: ['blanket'],
    8: ['dice', 'violin'],
    9: [],
    10: ['branch']
}

# Put the toothbrush and the zipper and the dice into Box 7.
items_to_put = ['toothbrush', 'zipper', 'dice']
for item in items_to_put:
    boxes[7].append(item)

# Put the horn and the basket and the star into Box 4.
items_to_put = ['horn', 'basket', 'star']
for item in items_to_put:
    boxes[4].append(item)

# Remove the gloves from Box 0.
boxes[0].remove('gloves')

# Put the button and the cup and the tie into Box 4.
items_to_put = ['button', 'cup', 'tie']
for item in items_to_put:
    boxes[4].append(item)

# Move the violin and the dice from Box 8 to Box 1.
items_to_move = ['violin', 'dice']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[1].append(item)

# Put the cat into Box 8.
boxes[8].append('cat')

# Remove the zipper and the blanket from Box 7.
boxes[7].remove('zipper')
boxes[7].remove('blanket')

# Remove the cat from Box 8.
boxes[8].remove('cat')

# Put the note and the storm into Box 6.
items_to_put = ['note', 'storm']
for item in items_to_put:
    boxes[6].append(item)

# Put the blender and the shelf and the pants into Box 10.
items_to_put = ['blender', 'shelf', 'pants']
for item in items_to_put:
    boxes[10].append(item)

# Swap the microwave in Box 2 with the skirt in Box 1.
boxes[1].remove('skirt')
boxes[2].remove('microwave')
boxes[1].append('microwave')
boxes[2].append('skirt')

# Put the glove into Box 1.
boxes[1].append('glove')

# Replace the drum with the laptop in Box 2.
boxes[2].remove('drum')
boxes[2].append('laptop')

# Remove the storm from Box 6.
boxes[6].remove('storm')

# Move the note from Box 6 to Box 8.
boxes[6].remove('note')
boxes[8].append('note')

# Replace the wig and the bear and the mountain with the vase and the toaster and the beach in Box 3.
boxes[3].remove('wig')
boxes[3].remove('bear')
boxes[3].remove('mountain')
boxes[3].append('vase')
boxes[3].append('toaster')
boxes[3].append('beach')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")