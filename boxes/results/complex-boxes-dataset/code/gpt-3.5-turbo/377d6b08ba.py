# Initial state of boxes
boxes = {
    0: ['comet'],
    1: ['shampoo', 'toaster'],
    2: ['train', 'glasses'],
    3: ['bowl', 'tiger'],
    4: ['fish', 'blender', 'mirror', 'pen'],
    5: ['flute'],
    6: ['beach'],
    7: [],
    8: ['console', 'toothpaste', 'watch'],
    9: [],
    10: ['tie'],
    11: ['wig', 'microwave', 'meteor', 'scissors', 'frame'],
    12: ['sandals', 'bracelet', 'drum', 'note', 'horn'],
    13: ['card', 'bear', 'hat', 'zipper', 'bicycle'],
    14: ['thunder']
}

# Move the zipper and the hat and the bicycle from Box 13 to Box 2.
items_to_move = ['zipper', 'hat', 'bicycle']
for item in items_to_move:
    boxes[13].remove(item)
    boxes[2].append(item)

# Move the card and the bear from Box 13 to Box 5.
items_to_move = ['card', 'bear']
for item in items_to_move:
    boxes[13].remove(item)
    boxes[5].append(item)

# Put the chair and the dice into Box 12.
items_to_put = ['chair', 'dice']
for item in items_to_put:
    boxes[12].append(item)

# Remove the comet from Box 0.
boxes[0].remove('comet')

# Replace the bowl and the tiger with the microwave and the sculpture in Box 3.
boxes[3].remove('bowl')
boxes[3].remove('tiger')
boxes[3].append('microwave')
boxes[3].append('sculpture')

# Replace the tie with the boat in Box 10.
boxes[10].remove('tie')
boxes[10].append('boat')

# Remove the boat from Box 10.
boxes[10].remove('boat')

# Remove the shampoo and the toaster from Box 1.
boxes[1].remove('shampoo')
boxes[1].remove('toaster')

# Put the controller into Box 9.
boxes[9].append('controller')

# Remove the toothpaste and the console from Box 8.
boxes[8].remove('toothpaste')
boxes[8].remove('console')

# Put the ocean and the bear and the pot into Box 8.
items_to_put = ['ocean', 'bear', 'pot']
for item in items_to_put:
    boxes[8].append(item)

# Put the vase and the mask and the storm into Box 3.
items_to_put = ['vase', 'mask', 'storm']
for item in items_to_put:
    boxes[3].append(item)

# Remove the hat from Box 2.
boxes[2].remove('hat')

# Remove the bear and the ocean and the pot from Box 8.
items_to_remove = ['bear', 'ocean', 'pot']
for item in items_to_remove:
    boxes[8].remove(item)

# Swap the thunder in Box 14 with the card in Box 5.
boxes[14].remove('thunder')
boxes[5].remove('card')
boxes[14].append('card')
boxes[5].append('thunder')

# Replace the beach with the motorcycle in Box 6.
boxes[6].remove('beach')
boxes[6].append('motorcycle')

# Swap the blender in Box 4 with the train in Box 2.
boxes[4].remove('blender')
boxes[2].remove('train')
boxes[4].append('train')
boxes[2].append('blender')

# Replace the card with the soap in Box 14.
boxes[14].remove('card')
boxes[14].append('soap')

# Replace the sculpture with the cup in Box 3.
boxes[3].remove('sculpture')
boxes[3].append('cup')

# Put the lipstick and the mixer into Box 13.
items_to_put = ['lipstick', 'mixer']
for item in items_to_put:
    boxes[13].append(item)

# Remove the mirror from Box 4.
boxes[4].remove('mirror')

# Remove the motorcycle from Box 6.
boxes[6].remove('motorcycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")