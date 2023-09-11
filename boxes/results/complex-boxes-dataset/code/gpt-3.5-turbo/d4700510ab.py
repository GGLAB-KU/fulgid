# Initial state of boxes
boxes = {
    0: ['bag', 'lock', 'bird', 'train', 'speaker'],
    1: ['brush'],
    2: ['fish', 'dice', 'beach'],
    3: ['dog', 'key'],
    4: ['toothbrush', 'plane', 'puzzle']
}

# Move the key and the dog from Box 3 to Box 0.
boxes[0].append(boxes[3].pop(0))
boxes[0].append(boxes[3].pop(0))

# Replace the bag and the train with the umbrella and the hat in Box 0.
boxes[0].remove('bag')
boxes[0].remove('train')
boxes[0].append('umbrella')
boxes[0].append('hat')

# Remove the plane from Box 4.
boxes[4].remove('plane')

# Remove the puzzle and the toothbrush from Box 4.
boxes[4].remove('puzzle')
boxes[4].remove('toothbrush')

# Remove the brush from Box 1.
boxes[1].remove('brush')

# Move the beach and the dice from Box 2 to Box 3.
boxes[3].append(boxes[2].pop(2))
boxes[3].append(boxes[2].pop(1))

# Swap the fish in Box 2 with the dice in Box 3.
boxes[2].append(boxes[3].pop(1))
boxes[3].append(boxes[2].pop(0))

# Move the key and the bird from Box 0 to Box 1.
boxes[1].append(boxes[0].pop(2))
boxes[1].append(boxes[0].pop(2))

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")