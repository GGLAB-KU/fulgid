# Initial state of boxes
boxes = {
    0: ['train', 'lamp'],
    1: ['cow', 'pan'],
    2: ['bracelet'],
    3: ['moon', 'elephant'],
    4: ['spoon', 'wallet', 'fish']
}

# Swap the train in Box 0 with the fish in Box 4.
boxes[0].remove('train')
boxes[4].remove('fish')
boxes[0].append('fish')
boxes[4].append('train')

# Move the lamp and the fish from Box 0 to Box 2.
boxes[0].remove('lamp')
boxes[0].remove('fish')
boxes[2].append('lamp')
boxes[2].append('fish')

# Put the wig and the pants and the plate into Box 3.
items_to_move = ['wig', 'pants', 'plate']
for item in items_to_move:
    boxes[3].append(item)

# Put the rain and the cloud into Box 4.
items_to_move = ['rain', 'cloud']
for item in items_to_move:
    boxes[4].append(item)

# Move the bracelet and the lamp and the fish from Box 2 to Box 4.
items_to_move = ['bracelet', 'lamp', 'fish']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[4].append(item)

# Swap the pan in Box 1 with the moon in Box 3.
boxes[1].remove('pan')
boxes[3].remove('moon')
boxes[1].append('moon')
boxes[3].append('pan')

# Move the moon and the cow from Box 1 to Box 2.
boxes[1].remove('cow')
boxes[3].remove('moon')
boxes[2].append('moon')
boxes[2].append('cow')

# Replace the wallet and the train with the battery and the branch in Box 4.
boxes[4].remove('wallet')
boxes[4].remove('train')
boxes[4].append('battery')
boxes[4].append('branch')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")