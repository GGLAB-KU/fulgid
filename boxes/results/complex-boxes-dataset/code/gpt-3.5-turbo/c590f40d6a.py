# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['puzzle'],
    3: [],
    4: ['pillow', 'pot', 'basket'],
    5: ['bowl'],
    6: ['button', 'cloud', 'hat', 'sandals']
}

# Put the whistle and the jacket into Box 0.
boxes[0].append('whistle')
boxes[0].append('jacket')

# Swap the bowl in Box 5 with the puzzle in Box 2.
boxes[2].remove('puzzle')
boxes[5].remove('bowl')
boxes[2].append('bowl')
boxes[5].append('puzzle')

# Swap the whistle in Box 0 with the bowl in Box 2.
boxes[0].remove('whistle')
boxes[2].remove('bowl')
boxes[0].append('bowl')
boxes[2].append('whistle')

# Swap the jacket in Box 0 with the puzzle in Box 5.
boxes[0].remove('jacket')
boxes[5].remove('puzzle')
boxes[0].append('puzzle')
boxes[5].append('jacket')

# Put the paint and the ship into Box 4.
boxes[4].append('paint')
boxes[4].append('ship')

# Swap the whistle in Box 2 with the pillow in Box 4.
boxes[2].remove('whistle')
boxes[4].remove('pillow')
boxes[2].append('pillow')
boxes[4].append('whistle')

# Put the razor and the gloves and the grinder into Box 4.
boxes[4].append('razor')
boxes[4].append('gloves')
boxes[4].append('grinder')

# Empty Box 0.
boxes[0] = []

# Remove the button and the cloud and the hat from Box 6.
boxes[6].remove('button')
boxes[6].remove('cloud')
boxes[6].remove('hat')

# Move the sandals from Box 6 to Box 3.
boxes[6].remove('sandals')
boxes[3].append('sandals')

# Remove the jacket from Box 5.
boxes[5].remove('jacket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")