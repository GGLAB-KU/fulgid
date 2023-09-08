# Initial state of boxes
boxes = {
    0: ['river', 'pillow', 'table'],
    1: ['card'],
    2: [],
    3: [],
    4: ['coin', 'oven', 'comet', 'sun'],
    5: ['pan'],
    6: [],
    7: ['dice', 'note', 'bicycle', 'charger', 'mask'],
    8: [],
    9: ['bell', 'butterfly', 'fish', 'flute', 'plane'],
    10: ['octopus', 'apple', 'vase']
}

# Remove the card from Box 1.
boxes[1].remove('card')

# Put the pen and the harmonica into Box 9.
boxes[9].append('pen')
boxes[9].append('harmonica')

# Empty Box 10.
boxes[10] = []

# Move the pillow and the table from Box 0 to Box 10.
items_to_move = ['pillow', 'table']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[10].append(item)

# Remove the coin and the sun and the comet from Box 4.
items_to_remove = ['coin', 'sun', 'comet']
for item in items_to_remove:
    boxes[4].remove(item)

# Remove the table and the pillow from Box 10.
items_to_remove = ['table', 'pillow']
for item in items_to_remove:
    boxes[10].remove(item)

# Replace the river with the coat in Box 0.
boxes[0].remove('river')
boxes[0].append('coat')

# Move the pan from Box 5 to Box 7.
boxes[5].remove('pan')
boxes[7].append('pan')

# Move the coat from Box 0 to Box 5.
boxes[0].remove('coat')
boxes[5].append('coat')

# Move the oven from Box 4 to Box 7.
boxes[4].remove('oven')
boxes[7].append('oven')

# Move the coat from Box 5 to Box 7.
boxes[5].remove('coat')
boxes[7].append('coat')

# Put the phone into Box 4.
boxes[4].append('phone')

# Move the phone from Box 4 to Box 3.
boxes[4].remove('phone')
boxes[3].append('phone')

# Replace the flute with the bell in Box 9.
boxes[9].remove('flute')
boxes[9].append('bell')

# Replace the note and the mask and the coat with the button and the comet and the moon in Box 7.
boxes[7].remove('note')
boxes[7].remove('mask')
boxes[7].remove('coat')
boxes[7].append('button')
boxes[7].append('comet')
boxes[7].append('moon')

# Swap the moon in Box 7 with the phone in Box 3.
boxes[7].remove('moon')
boxes[3].remove('phone')
boxes[7].append('phone')
boxes[3].append('moon')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")