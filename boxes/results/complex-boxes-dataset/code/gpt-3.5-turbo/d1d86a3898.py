# Initial state of boxes
boxes = {
    0: ['phone', 'scarf', 'cow', 'keyboard', 'paint'],
    1: [],
    2: ['planet', 'cat', 'toothbrush', 'whistle', 'car'],
    3: [],
    4: ['charger', 'rock']
}

# Swap the keyboard in Box 0 with the cat in Box 2.
boxes[0].remove('keyboard')
boxes[2].remove('cat')
boxes[0].append('cat')
boxes[2].append('keyboard')

# Put the star into Box 1.
boxes[1].append('star')

# Move the toothbrush from Box 2 to Box 0.
boxes[2].remove('toothbrush')
boxes[0].append('toothbrush')

# Remove the star from Box 1.
boxes[1].remove('star')

# Replace the rock with the apple in Box 4.
boxes[4].remove('rock')
boxes[4].append('apple')

# Replace the planet with the charger in Box 2.
boxes[2].remove('planet')
boxes[2].append('charger')

# Remove the apple from Box 4.
boxes[4].remove('apple')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")