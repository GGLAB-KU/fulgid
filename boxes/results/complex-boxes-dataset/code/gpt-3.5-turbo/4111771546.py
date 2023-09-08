# Initial state of boxes
boxes = {
    0: [],
    1: ['wig'],
    2: ['tape', 'frame'],
    3: ['plate', 'toothpaste'],
    4: ['river'],
    5: ['pillow', 'laptop']
}

# Replace the wig with the car in Box 1.
boxes[1].remove('wig')
boxes[1].append('car')

# Put the lion and the bus and the mountain into Box 1.
boxes[1].extend(['lion', 'bus', 'mountain'])

# Put the headphone and the bowl and the boat into Box 0.
boxes[0].extend(['headphone', 'bowl', 'boat'])

# Put the watch and the ring into Box 4.
boxes[4].extend(['watch', 'ring'])

# Put the pen and the desert into Box 3.
boxes[3].extend(['pen', 'desert'])

# Swap the car in Box 1 with the laptop in Box 5.
boxes[1].remove('car')
boxes[5].remove('laptop')
boxes[1].append('laptop')
boxes[5].append('car')

# Remove the headphone from Box 0.
boxes[0].remove('headphone')

# Move the lion and the bus from Box 1 to Box 3.
items_to_move = ['lion', 'bus']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Move the lion from Box 3 to Box 4.
boxes[3].remove('lion')
boxes[4].append('lion')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")