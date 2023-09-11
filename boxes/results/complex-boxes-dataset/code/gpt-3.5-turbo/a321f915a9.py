# Initial state of boxes
boxes = {
    0: [],
    1: ['leaf'],
    2: ['dog', 'meteor'],
    3: ['crown', 'sandals', 'drum'],
    4: [],
    5: ['needle', 'mountain', 'lightning', 'grass'],
    6: ['scarf', 'necklace', 'glove', 'watch', 'shoes'],
    7: ['mixer', 'boat', 'lipstick'],
    8: ['bicycle', 'fish', 'shirt']
}

# Move the lipstick and the mixer from Box 7 to Box 4.
boxes[7].remove('lipstick')
boxes[7].remove('mixer')
boxes[4].append('lipstick')
boxes[4].append('mixer')

# Put the starfish into Box 4.
boxes[4].append('starfish')

# Move the grass and the needle and the mountain from Box 5 to Box 8.
items_to_move = ['grass', 'needle', 'mountain']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[8].append(item)

# Move the boat from Box 7 to Box 8.
boxes[7].remove('boat')
boxes[8].append('boat')

# Swap the shirt in Box 8 with the starfish in Box 4.
boxes[8].remove('shirt')
boxes[4].remove('starfish')
boxes[8].append('starfish')
boxes[4].append('shirt')

# Move the lipstick and the mixer and the shirt from Box 4 to Box 5.
items_to_move = ['lipstick', 'mixer', 'shirt']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[5].append(item)

# Remove the needle and the bicycle from Box 8.
boxes[8].remove('needle')
boxes[8].remove('bicycle')

# Swap the shirt in Box 5 with the shoes in Box 6.
boxes[5].remove('shirt')
boxes[6].remove('shoes')
boxes[5].append('shoes')
boxes[6].append('shirt')

# Move the sandals and the drum and the crown from Box 3 to Box 1.
items_to_move = ['sandals', 'drum', 'crown']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Swap the boat in Box 8 with the dog in Box 2.
boxes[8].remove('boat')
boxes[2].remove('dog')
boxes[8].append('dog')
boxes[2].append('boat')

# Put the umbrella and the headphone into Box 6.
boxes[6].append('umbrella')
boxes[6].append('headphone')

# Replace the necklace and the scarf with the piano and the glasses in Box 6.
boxes[6].remove('necklace')
boxes[6].remove('scarf')
boxes[6].append('piano')
boxes[6].append('glasses')

# Empty Box 8.
boxes[8] = []

# Replace the shoes and the lipstick and the mixer with the lock and the blender and the glasses in Box 5.
boxes[5].remove('shoes')
boxes[5].remove('lipstick')
boxes[5].remove('mixer')
boxes[5].append('lock')
boxes[5].append('blender')
boxes[5].append('glasses')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")