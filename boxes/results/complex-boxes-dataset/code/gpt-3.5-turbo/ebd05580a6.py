# Initial state of boxes
boxes = {
    0: ['branch', 'bracelet', 'fish', 'pan', 'pants'],
    1: ['rain', 'storm', 'mixer', 'keyboard', 'phone'],
    2: ['plane', 'piano', 'zipper'],
    3: ['console'],
    4: ['doll'],
    5: ['key', 'freezer', 'wig', 'butterfly', 'starfish'],
    6: []
}

# Remove the doll from Box 4.
boxes[4].remove('doll')

# Put the river and the island and the pot into Box 1.
boxes[1].append('river')
boxes[1].append('island')
boxes[1].append('pot')

# Move the key and the starfish from Box 5 to Box 2.
boxes[5].remove('key')
boxes[5].remove('starfish')
boxes[2].append('key')
boxes[2].append('starfish')

# Move the storm and the pot and the rain from Box 1 to Box 2.
items_to_move = ['storm', 'pot', 'rain']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Move the wig and the butterfly from Box 5 to Box 6.
items_to_move = ['wig', 'butterfly']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[6].append(item)

# Replace the mixer and the river with the key and the chair in Box 1.
boxes[1].remove('mixer')
boxes[1].remove('river')
boxes[1].append('key')
boxes[1].append('chair')

# Replace the console with the car in Box 3.
boxes[3].remove('console')
boxes[3].append('car')

# Replace the pants and the fish with the lion and the glove in Box 0.
boxes[0].remove('pants')
boxes[0].remove('fish')
boxes[0].append('lion')
boxes[0].append('glove')

# Remove the wig and the butterfly from Box 6.
boxes[6].remove('wig')
boxes[6].remove('butterfly')

# Replace the freezer with the gloves in Box 5.
boxes[5].remove('freezer')
boxes[5].append('gloves')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")