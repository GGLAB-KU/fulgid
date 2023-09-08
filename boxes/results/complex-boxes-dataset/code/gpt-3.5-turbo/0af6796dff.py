# Initial state of boxes
boxes = {
    0: ['bus', 'tape', 'cow', 'phone', 'wallet'],
    1: ['microscope', 'lion'],
    2: ['island', 'comb', 'pillow', 'soap', 'plate'],
    3: ['shoes', 'bird', 'apple', 'rain', 'comet'],
    4: ['sock', 'storm', 'basket']
}

# Swap the bus in Box 0 with the lion in Box 1.
boxes[0].remove('bus')
boxes[1].remove('lion')
boxes[0].append('lion')
boxes[1].append('bus')

# Swap the phone in Box 0 with the bus in Box 1.
boxes[0].remove('phone')
boxes[1].remove('bus')
boxes[0].append('bus')
boxes[1].append('phone')

# Move the pillow and the plate and the soap from Box 2 to Box 0.
items_to_move = ['pillow', 'plate', 'soap']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Move the island and the comb from Box 2 to Box 0.
items_to_move = ['island', 'comb']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Put the toaster into Box 3.
boxes[3].append('toaster')

# Swap the storm in Box 4 with the shoes in Box 3.
boxes[4].remove('storm')
boxes[3].remove('shoes')
boxes[4].append('shoes')
boxes[3].append('storm')

# Put the freezer and the wig and the horse into Box 2.
items_to_put = ['freezer', 'wig', 'horse']
for item in items_to_put:
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")