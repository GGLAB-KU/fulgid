# Initial state of boxes
boxes = {
    0: ['toothbrush', 'cat'],
    1: ['guitar', 'flute'],
    2: [],
    3: ['dolphin'],
    4: [],
    5: ['desert', 'battery', 'bell', 'pot', 'basket'],
    6: ['earring', 'island', 'thread', 'lightning', 'dress']
}

# Remove the dolphin from Box 3.
boxes[3].remove('dolphin')

# Move the thread and the earring from Box 6 to Box 1.
boxes[6].remove('thread')
boxes[6].remove('earring')
boxes[1].append('thread')
boxes[1].append('earring')

# Remove the dress and the island and the lightning from Box 6.
boxes[6].remove('dress')
boxes[6].remove('island')
boxes[6].remove('lightning')

# Replace the flute and the thread with the helmet and the watch in Box 1.
boxes[1].remove('flute')
boxes[1].remove('thread')
boxes[1].append('helmet')
boxes[1].append('watch')

# Put the polish and the moon into Box 0.
boxes[0].append('polish')
boxes[0].append('moon')

# Empty Box 1.
boxes[1] = []

# Move the polish and the cat and the moon from Box 0 to Box 3.
items_to_move = ['polish', 'cat', 'moon']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Put the lightning and the rocket and the doll into Box 5.
items_to_put = ['lightning', 'rocket', 'doll']
for item in items_to_put:
    boxes[5].append(item)

# Put the plane into Box 3.
boxes[3].append('plane')

# Swap the battery in Box 5 with the toothbrush in Box 0.
boxes[0].remove('toothbrush')
boxes[5].remove('battery')
boxes[0].append('battery')
boxes[5].append('toothbrush')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")