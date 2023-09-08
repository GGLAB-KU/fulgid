# Initial state of boxes
boxes = {
    0: ['snow'],
    1: ['toaster', 'coral', 'star'],
    2: [],
    3: ['chair', 'elephant'],
    4: ['pen'],
    5: ['shoe', 'dice', 'toothpaste', 'fork'],
    6: ['tiger'],
    7: [],
    8: ['vase', 'scissors', 'wire'],
    9: ['lightning', 'cloud', 'seaweed'],
    10: ['pillow', 'guitar']
}

# Replace the toaster and the star and the coral with the apple and the hat and the glasses in Box 1.
boxes[1].remove('toaster')
boxes[1].remove('coral')
boxes[1].remove('star')
boxes[1].append('apple')
boxes[1].append('hat')
boxes[1].append('glasses')

# Empty Box 8.
boxes[8] = []

# Swap the pen in Box 4 with the fork in Box 5.
boxes[4], boxes[5] = boxes[5], boxes[4]

# Move the glasses and the hat and the apple from Box 1 to Box 10.
items_to_move = ['glasses', 'hat', 'apple']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[10].append(item)

# Swap the tiger in Box 6 with the snow in Box 0.
boxes[0], boxes[6] = boxes[6], boxes[0]

# Move the snow from Box 6 to Box 3.
boxes[6].remove('snow')
boxes[3].append('snow')

# Move the chair and the elephant from Box 3 to Box 2.
boxes[3].remove('chair')
boxes[3].remove('elephant')
boxes[2].append('chair')
boxes[2].append('elephant')

# Replace the elephant with the shampoo in Box 2.
boxes[2].remove('elephant')
boxes[2].append('shampoo')

# Swap the guitar in Box 10 with the tiger in Box 0.
boxes[0], boxes[10] = boxes[10], boxes[0]

# Remove the apple from Box 10.
boxes[10].remove('apple')

# Remove the tiger and the glasses and the pillow from Box 10.
items_to_remove = ['tiger', 'glasses', 'pillow']
for item in items_to_remove:
    boxes[10].remove(item)

# Move the hat from Box 10 to Box 8.
boxes[10].remove('hat')
boxes[8].append('hat')

# Replace the dice and the toothpaste and the pen with the comet and the necklace and the coat in Box 5.
boxes[5].remove('dice')
boxes[5].remove('toothpaste')
boxes[5].remove('pen')
boxes[5].append('comet')
boxes[5].append('necklace')
boxes[5].append('coat')

# Put the flower and the pillow and the forest into Box 6.
items_to_move = ['flower', 'pillow', 'forest']
for item in items_to_move:
    boxes[6].append(item)

# Move the chair and the shampoo from Box 2 to Box 9.
boxes[2].remove('chair')
boxes[2].remove('shampoo')
boxes[9].append('chair')
boxes[9].append('shampoo')

# Remove the pillow and the forest and the flower from Box 6.
items_to_remove = ['pillow', 'forest', 'flower']
for item in items_to_remove:
    boxes[6].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")