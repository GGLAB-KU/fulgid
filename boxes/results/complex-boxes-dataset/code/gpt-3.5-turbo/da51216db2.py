# Initial state of boxes
boxes = {
    0: ['clock', 'mirror', 'fish', 'wire', 'card'],
    1: [],
    2: ['lion'],
    3: [],
    4: [],
    5: ['drum'],
    6: [],
    7: ['island', 'pan']
}

# Move the drum from Box 5 to Box 6.
boxes[5].remove('drum')
boxes[6].append('drum')

# Remove the lion from Box 2.
boxes[2].remove('lion')

# Swap the drum in Box 6 with the wire in Box 0.
boxes[0].remove('wire')
boxes[6].remove('drum')
boxes[0].append('drum')
boxes[6].append('wire')

# Swap the island in Box 7 with the wire in Box 6.
boxes[7].remove('island')
boxes[6].remove('wire')
boxes[7].append('wire')
boxes[6].append('island')

# Move the island from Box 6 to Box 7.
boxes[6].remove('island')
boxes[7].append('island')

# Put the key and the sun and the forest into Box 3.
items_to_move = ['key', 'sun', 'forest']
for item in items_to_move:
    boxes[3].append(item)

# Put the guitar into Box 6.
boxes[6].append('guitar')

# Replace the key with the horn in Box 3.
boxes[3].remove('key')
boxes[3].append('horn')

# Move the island and the wire and the pan from Box 7 to Box 2.
items_to_move = ['island', 'wire', 'pan']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[2].append(item)

# Remove the mirror from Box 0.
boxes[0].remove('mirror')

# Remove the forest from Box 3.
boxes[3].remove('forest')

# Remove the sun and the horn from Box 3.
items_to_remove = ['sun', 'horn']
for item in items_to_remove:
    boxes[3].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")