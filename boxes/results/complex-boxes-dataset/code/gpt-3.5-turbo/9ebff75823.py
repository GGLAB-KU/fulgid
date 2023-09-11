# Initial state of boxes
boxes = {
    0: ['button', 'flute'],
    1: ['shoe', 'console', 'clock', 'basket'],
    2: ['bear', 'magnet', 'watch', 'river', 'candle'],
    3: ['fork'],
    4: [],
    5: [],
    6: [],
    7: ['bowl', 'puzzle', 'microwave', 'doll', 'sun'],
    8: []
}

# Swap the bowl in Box 7 with the button in Box 0.
boxes[0].remove('button')
boxes[7].remove('bowl')
boxes[0].append('bowl')
boxes[7].append('button')

# Replace the button and the puzzle and the sun with the tie and the freezer and the fish in Box 7.
boxes[7].remove('button')
boxes[7].remove('puzzle')
boxes[7].remove('sun')
boxes[7].append('tie')
boxes[7].append('freezer')
boxes[7].append('fish')

# Put the forest and the cup into Box 2.
boxes[2].append('forest')
boxes[2].append('cup')

# Move the freezer and the tie and the fish from Box 7 to Box 1.
items_to_move = ['freezer', 'tie', 'fish']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[1].append(item)

# Move the flute from Box 0 to Box 1.
boxes[0].remove('flute')
boxes[1].append('flute')

# Put the river and the basket and the wire into Box 1.
items_to_put = ['river', 'basket', 'wire']
for item in items_to_put:
    boxes[2].remove(item)
    boxes[1].append(item)

# Remove the bowl from Box 0.
boxes[0].remove('bowl')

# Move the console and the fish from Box 1 to Box 8.
items_to_move = ['console', 'fish']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[8].append(item)

# Move the cup from Box 2 to Box 5.
boxes[2].remove('cup')
boxes[5].append('cup')

# Put the perfume into Box 0.
boxes[0].append('perfume')

# Replace the fork with the makeup in Box 3.
boxes[3].remove('fork')
boxes[3].append('makeup')

# Replace the perfume with the elephant in Box 0.
boxes[0].remove('perfume')
boxes[0].append('elephant')

# Put the blender and the fork into Box 5.
boxes[5].append('blender')
boxes[5].append('fork')

# Swap the flute in Box 1 with the console in Box 8.
boxes[1].remove('flute')
boxes[8].remove('console')
boxes[1].append('console')
boxes[8].append('flute')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")