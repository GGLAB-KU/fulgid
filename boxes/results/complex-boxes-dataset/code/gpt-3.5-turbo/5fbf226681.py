# Initial state of boxes
boxes = {
    0: ['book', 'soap', 'planet', 'flower'],
    1: ['tiger'],
    2: [],
    3: ['snow', 'shelf', 'bowl'],
    4: ['motorcycle', 'candle', 'whistle'],
    5: [],
    6: ['basket', 'chair', 'towel'],
    7: ['note', 'bell', 'dolphin', 'cat', 'flute'],
    8: ['submarine'],
    9: ['needle'],
    10: ['doll', 'storm', 'mountain', 'plane']
}

# Move the planet and the flower and the soap from Box 0 to Box 3.
items_to_move = ['planet', 'flower', 'soap']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Put the dress and the lipstick into Box 3.
items_to_add = ['dress', 'lipstick']
for item in items_to_add:
    boxes[3].append(item)

# Put the coral and the bowl and the tree into Box 7.
items_to_add = ['coral', 'bowl', 'tree']
for item in items_to_add:
    boxes[7].append(item)

# Empty Box 9.
boxes[9] = []

# Put the bell and the pants into Box 10.
items_to_add = ['bell', 'pants']
for item in items_to_add:
    boxes[10].append(item)

# Remove the storm from Box 10.
boxes[10].remove('storm')

# Remove the dress and the bowl from Box 3.
items_to_remove = ['dress', 'bowl']
for item in items_to_remove:
    boxes[3].remove(item)

# Put the freezer and the wig and the mixer into Box 5.
items_to_add = ['freezer', 'wig', 'mixer']
for item in items_to_add:
    boxes[5].append(item)

# Move the motorcycle and the candle and the whistle from Box 4 to Box 8.
items_to_move = ['motorcycle', 'candle', 'whistle']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[8].append(item)

# Replace the bowl with the snow in Box 7.
boxes[7].remove('bowl')
boxes[7].append('snow')

# Swap the coral in Box 7 with the basket in Box 6.
boxes[7].remove('coral')
boxes[6].remove('basket')
boxes[7].append('basket')
boxes[6].append('coral')

# Replace the towel and the coral with the cup and the shoes in Box 6.
boxes[6].remove('towel')
boxes[6].remove('coral')
boxes[6].append('cup')
boxes[6].append('shoes')

# Move the soap and the planet and the lipstick from Box 3 to Box 5.
items_to_move = ['soap', 'planet', 'lipstick']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[5].append(item)

# Put the lamp and the soap into Box 3.
items_to_add = ['lamp', 'soap']
for item in items_to_add:
    boxes[3].append(item)

# Replace the book with the horse in Box 0.
boxes[0].remove('book')
boxes[0].append('horse')

# Empty Box 5.
boxes[5] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")