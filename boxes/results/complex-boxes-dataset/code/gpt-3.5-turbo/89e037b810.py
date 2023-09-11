# Initial state of boxes
boxes = {
    0: ['dice', 'grass', 'glasses'],
    1: ['leaf', 'basket'],
    2: ['bear', 'phone', 'laptop', 'plane', 'violin'],
    3: ['zipper', 'jungle', 'dress'],
    4: ['comb'],
    5: ['headphone', 'cow'],
    6: []
}

# Swap the grass in Box 0 with the plane in Box 2.
boxes[0].remove('grass')
boxes[2].remove('plane')
boxes[0].append('plane')
boxes[2].append('grass')

# Replace the grass with the mountain in Box 2.
boxes[2].remove('grass')
boxes[2].append('mountain')

# Swap the jungle in Box 3 with the glasses in Box 0.
boxes[3].remove('jungle')
boxes[0].remove('glasses')
boxes[3].append('glasses')
boxes[0].append('jungle')

# Remove the laptop from Box 2.
boxes[2].remove('laptop')

# Swap the plane in Box 0 with the phone in Box 2.
boxes[0].remove('plane')
boxes[2].remove('phone')
boxes[0].append('phone')
boxes[2].append('plane')

# Remove the glasses and the zipper from Box 3.
boxes[3].remove('glasses')
boxes[3].remove('zipper')

# Replace the violin with the thunder in Box 2.
boxes[2].remove('violin')
boxes[2].append('thunder')

# Remove the comb from Box 4.
boxes[4].remove('comb')

# Swap the dice in Box 0 with the headphone in Box 5.
boxes[0].remove('dice')
boxes[5].remove('headphone')
boxes[0].append('headphone')
boxes[5].append('dice')

# Remove the leaf from Box 1.
boxes[1].remove('leaf')

# Put the usb and the skirt and the violin into Box 1.
items_to_move = ['usb', 'skirt', 'violin']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")