# Initial state of boxes
boxes = {
    0: [],
    1: ['planet', 'rocket', 'toy', 'mountain', 'harmonica'],
    2: ['rock'],
    3: ['bag', 'shoes', 'gloves', 'bus', 'boot']
}

# Put the tiger into Box 2.
boxes[2].append('tiger')

# Replace the tiger with the scarf in Box 2.
boxes[2].remove('tiger')
boxes[2].append('scarf')

# Move the toy and the rocket from Box 1 to Box 2.
items_to_move = ['toy', 'rocket']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Put the button and the bear into Box 0.
boxes[0].append('button')
boxes[0].append('bear')

# Put the shorts and the clock and the horse into Box 0.
items_to_put = ['shorts', 'clock', 'horse']
for item in items_to_put:
    boxes[0].append(item)

# Put the grass and the battery into Box 3.
boxes[3].append('grass')
boxes[3].append('battery')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")