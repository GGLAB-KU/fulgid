# Initial state of boxes
boxes = {
    0: ['shark', 'boat', 'watch'],
    1: ['hat', 'paint', 'swimsuit', 'brush'],
    2: ['freezer', 'fridge', 'comb', 'tree'],
    3: ['card', 'key', 'zipper', 'lock', 'oven'],
    4: ['cloud', 'scarf', 'meteor'],
    5: ['plate'],
    6: ['basket', 'ring', 'glasses'],
    7: ['elephant', 'pillow', 'sculpture', 'pen'],
    8: ['pants', 'puzzle']
}

# Empty Box 7
boxes[7] = []

# Swap the comb in Box 2 with the card in Box 3
boxes[2].remove('comb')
boxes[3].remove('card')
boxes[2].append('card')
boxes[3].append('comb')

# Empty Box 6
boxes[6] = []

# Put the oven and the dice into Box 5
boxes[5].extend(['oven', 'dice'])

# Replace the pants and the puzzle with the watch and the plane in Box 8
boxes[8].remove('pants')
boxes[8].remove('puzzle')
boxes[8].append('watch')
boxes[8].append('plane')

# Replace the dice and the plate with the lipstick and the book in Box 5
boxes[5].remove('dice')
boxes[5].remove('plate')
boxes[5].append('lipstick')
boxes[5].append('book')

# Remove the meteor from Box 4
boxes[4].remove('meteor')

# Put the shelf and the tree and the glasses into Box 4
boxes[4].extend(['shelf', 'tree', 'glasses'])

# Swap the paint in Box 1 with the cloud in Box 4
boxes[1].remove('paint')
boxes[4].remove('cloud')
boxes[1].append('cloud')
boxes[4].append('paint')

# Remove the scarf from Box 4
boxes[4].remove('scarf')

# Put the star into Box 3
boxes[3].append('star')

# Remove the shelf and the glasses from Box 4
boxes[4].remove('shelf')
boxes[4].remove('glasses')

# Put the submarine and the snow into Box 1
boxes[1].extend(['submarine', 'snow'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")