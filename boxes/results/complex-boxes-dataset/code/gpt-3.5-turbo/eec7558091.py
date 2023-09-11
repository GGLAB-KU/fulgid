# Initial state of boxes
boxes = {
    0: ['scissors'],
    1: ['mask'],
    2: ['car', 'violin'],
    3: ['razor', 'mirror'],
    4: [],
    5: ['coin', 'clock', 'console', 'perfume', 'whistle'],
    6: ['paint'],
    7: [],
    8: ['headphone']
}

# Move the paint from Box 6 to Box 1.
boxes[6].remove('paint')
boxes[1].append('paint')

# Swap the mask in Box 1 with the scissors in Box 0.
boxes[1].remove('mask')
boxes[0].remove('scissors')
boxes[1].append('scissors')
boxes[0].append('mask')

# Put the branch and the forest and the card into Box 3.
items_to_put = ['branch', 'forest', 'card']
for item in items_to_put:
    boxes[3].append(item)

# Put the shirt into Box 4.
boxes[4].append('shirt')

# Remove the console and the perfume and the coin from Box 5.
items_to_remove = ['console', 'perfume', 'coin']
for item in items_to_remove:
    boxes[5].remove(item)

# Move the mask from Box 0 to Box 3.
boxes[0].remove('mask')
boxes[3].append('mask')

# Put the dog and the sandals and the thunder into Box 7.
items_to_put = ['dog', 'sandals', 'thunder']
for item in items_to_put:
    boxes[7].append(item)

# Replace the paint and the scissors with the piano and the mixer in Box 1.
boxes[1].remove('paint')
boxes[1].remove('scissors')
boxes[1].append('piano')
boxes[1].append('mixer')

# Put the coin and the charger into Box 3.
items_to_put = ['coin', 'charger']
for item in items_to_put:
    boxes[3].append(item)

# Move the piano and the mixer from Box 1 to Box 3.
boxes[1].remove('piano')
boxes[1].remove('mixer')
boxes[3].append('piano')
boxes[3].append('mixer')

# Swap the car in Box 2 with the whistle in Box 5.
boxes[2].remove('car')
boxes[5].remove('whistle')
boxes[2].append('whistle')
boxes[5].append('car')

# Swap the piano in Box 3 with the headphone in Box 8.
boxes[3].remove('piano')
boxes[8].remove('headphone')
boxes[3].append('headphone')
boxes[8].append('piano')

# Put the lamp and the skirt and the dog into Box 7.
items_to_put = ['lamp', 'skirt', 'dog']
for item in items_to_put:
    boxes[7].append(item)

# Remove the clock and the car from Box 5.
items_to_remove = ['clock', 'car']
for item in items_to_remove:
    boxes[5].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")