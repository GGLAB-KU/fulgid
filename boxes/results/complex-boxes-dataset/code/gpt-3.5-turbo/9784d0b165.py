# Initial state of boxes
boxes = {
    0: ['polish', 'key', 'game'],
    1: ['gloves', 'mountain'],
    2: ['starfish', 'piano', 'cat', 'horse'],
    3: ['hat'],
    4: ['toy'],
    5: ['desert', 'leaf', 'apple'],
    6: ['spoon', 'console', 'pen', 'lightning']
}

# Move the mountain from Box 1 to Box 6.
boxes[1].remove('mountain')
boxes[6].append('mountain')

# Replace the toy with the tape in Box 4.
boxes[4].remove('toy')
boxes[4].append('tape')

# Move the hat from Box 3 to Box 5.
boxes[3].remove('hat')
boxes[5].append('hat')

# Swap the gloves in Box 1 with the hat in Box 5.
boxes[1].remove('gloves')
boxes[5].remove('hat')
boxes[1].append('hat')
boxes[5].append('gloves')

# Move the mountain from Box 6 to Box 0.
boxes[6].remove('mountain')
boxes[0].append('mountain')

# Remove the mountain and the game from Box 0.
boxes[0].remove('mountain')
boxes[0].remove('game')

# Put the cat and the console and the sun into Box 5.
boxes[5].append('cat')
boxes[5].append('console')
boxes[5].append('sun')

# Put the bell into Box 3.
boxes[3].append('bell')

# Put the oven and the planet into Box 3.
boxes[3].append('oven')
boxes[3].append('planet')

# Remove the hat from Box 1.
boxes[1].remove('hat')

# Replace the starfish and the cat with the vase and the rocket in Box 2.
boxes[2].remove('starfish')
boxes[2].remove('cat')
boxes[2].append('vase')
boxes[2].append('rocket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")