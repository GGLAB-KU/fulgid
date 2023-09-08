# Initial state of boxes
boxes = {
    0: ['jungle', 'gloves'],
    1: ['pen'],
    2: ['mixer'],
    3: ['fridge', 'telescope', 'river', 'lion', 'shirt'],
    4: ['mountain', 'doll', 'beach', 'shampoo'],
    5: ['chair', 'hat', 'vase'],
    6: ['clock'],
    7: ['perfume', 'grinder', 'laptop']
}

# Put the drum into Box 6.
boxes[6].append('drum')

# Put the shorts and the speaker and the bracelet into Box 7.
items_to_add = ['shorts', 'speaker', 'bracelet']
for item in items_to_add:
    boxes[7].append(item)

# Remove the mixer from Box 2.
boxes[2].remove('mixer')

# Put the boot and the rocket and the spoon into Box 5.
items_to_add = ['boot', 'rocket', 'spoon']
for item in items_to_add:
    boxes[5].append(item)

# Put the perfume into Box 5.
boxes[5].append('perfume')

# Remove the pen from Box 1.
boxes[1].remove('pen')

# Remove the hat from Box 5.
boxes[5].remove('hat')

# Swap the gloves in Box 0 with the mountain in Box 4.
boxes[0].remove('gloves')
boxes[4].remove('mountain')
boxes[0].append('mountain')
boxes[4].append('gloves')

# Replace the shirt and the telescope with the tiger and the blanket in Box 3.
boxes[3].remove('shirt')
boxes[3].remove('telescope')
boxes[3].append('tiger')
boxes[3].append('blanket')

# Put the fork into Box 0.
boxes[0].append('fork')

# Move the fork and the mountain and the jungle from Box 0 to Box 2.
items_to_move = ['fork', 'mountain', 'jungle']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Move the vase and the spoon from Box 5 to Box 4.
items_to_move = ['vase', 'spoon']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")