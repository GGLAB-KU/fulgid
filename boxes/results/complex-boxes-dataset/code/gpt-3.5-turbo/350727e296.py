# Initial state of boxes
boxes = {
    0: ['freezer', 'telescope', 'dice'],
    1: ['clock', 'bowl', 'scissors', 'keyboard'],
    2: ['apple', 'guitar', 'coat', 'hat', 'sock'],
    3: ['fridge', 'frame', 'microwave', 'violin', 'scarf'],
    4: [],
    5: ['cat', 'game', 'vase', 'crown', 'gloves'],
    6: ['lion', 'seaweed'],
    7: [],
    8: ['pillow'],
    9: [],
    10: ['octopus', 'rocket', 'toothpaste', 'shorts']
}

# Remove the frame and the scarf from Box 3.
boxes[3].remove('frame')
boxes[3].remove('scarf')

# Put the sandals and the lightning and the game into Box 4.
items_to_move = ['sandals', 'lightning', 'game']
for item in items_to_move:
    boxes[4].append(item)

# Put the scarf and the sandals and the mixer into Box 4.
items_to_move = ['scarf', 'sandals', 'mixer']
for item in items_to_move:
    boxes[4].append(item)

# Swap the octopus in Box 10 with the fridge in Box 3.
boxes[10].remove('octopus')
boxes[3].remove('fridge')
boxes[10].append('fridge')
boxes[3].append('octopus')

# Put the brush and the umbrella into Box 2.
items_to_move = ['brush', 'umbrella']
for item in items_to_move:
    boxes[2].append(item)

# Move the telescope and the dice from Box 0 to Box 1.
items_to_move = ['telescope', 'dice']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Remove the fridge and the toothpaste and the shorts from Box 10.
items_to_remove = ['fridge', 'toothpaste', 'shorts']
for item in items_to_remove:
    boxes[10].remove(item)

# Move the apple and the hat and the guitar from Box 2 to Box 8.
items_to_move = ['apple', 'hat', 'guitar']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[8].append(item)

# Swap the sock in Box 2 with the scarf in Box 4.
boxes[2].remove('sock')
boxes[4].remove('scarf')
boxes[2].append('scarf')
boxes[4].append('sock')

# Remove the guitar and the apple and the hat from Box 8.
items_to_remove = ['guitar', 'apple', 'hat']
for item in items_to_remove:
    boxes[8].remove(item)

# Remove the microwave and the octopus from Box 3.
items_to_remove = ['microwave', 'octopus']
for item in items_to_remove:
    boxes[3].remove(item)

# Empty Box 6.
boxes[6] = []

# Swap the crown in Box 5 with the pillow in Box 8.
boxes[5].remove('crown')
boxes[8].remove('pillow')
boxes[5].append('pillow')
boxes[8].append('crown')

# Move the rocket from Box 10 to Box 3.
boxes[10].remove('rocket')
boxes[3].append('rocket')

# Move the vase from Box 5 to Box 7.
boxes[5].remove('vase')
boxes[7].append('vase')

# Replace the crown with the dice in Box 8.
boxes[8].remove('crown')
boxes[8].append('dice')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")