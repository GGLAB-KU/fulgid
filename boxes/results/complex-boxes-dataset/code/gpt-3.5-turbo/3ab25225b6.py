# Initial state of boxes
boxes = {
    0: ['tiger', 'whistle'],
    1: ['crown', 'tie', 'planet', 'lamp'],
    2: ['shark', 'bag', 'shirt', 'battery'],
    3: ['fish', 'helmet', 'lightning', 'wig', 'lipstick'],
    4: ['ocean'],
    5: ['candle'],
    6: ['coral', 'mask', 'flute', 'ship']
}

# Empty Box 4
boxes[4] = []

# Swap the battery in Box 2 with the tie in Box 1.
boxes[1].remove('tie')
boxes[2].remove('battery')
boxes[1].append('battery')
boxes[2].append('tie')

# Put the battery and the rocket and the book into Box 5.
items_to_move = ['battery', 'rocket', 'book']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[5].append(item)

# Move the planet from Box 1 to Box 3.
boxes[1].remove('planet')
boxes[3].append('planet')

# Remove the mask and the ship from Box 6.
boxes[6].remove('mask')
boxes[6].remove('ship')

# Replace the flute with the headphone in Box 6.
boxes[6].remove('flute')
boxes[6].append('headphone')

# Put the apple and the sun and the seaweed into Box 3.
items_to_move = ['apple', 'sun', 'seaweed']
for item in items_to_move:
    boxes[3].append(item)

# Remove the headphone and the coral from Box 6.
boxes[6].remove('headphone')
boxes[6].remove('coral')

# Move the lamp and the crown from Box 1 to Box 3.
items_to_move = ['lamp', 'crown']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Move the tie and the bag from Box 2 to Box 4.
items_to_move = ['tie', 'bag']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")