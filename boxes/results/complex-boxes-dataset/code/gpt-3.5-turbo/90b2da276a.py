# Initial state of boxes
boxes = {
    0: ['blanket', 'pillow', 'controller', 'drum', 'tape'],
    1: ['polish', 'cup', 'ocean'],
    2: ['watch', 'pants'],
    3: ['forest', 'sculpture', 'umbrella', 'whistle', 'horn'],
    4: ['bag'],
    5: ['clock', 'thunder', 'leaf'],
    6: ['mountain', 'microscope', 'oven']
}

# Put the battery and the bell into Box 3.
boxes[3].append('battery')
boxes[3].append('bell')

# Remove the pants and the watch from Box 2.
boxes[2].remove('pants')
boxes[2].remove('watch')

# Empty Box 4.
boxes[4] = []

# Remove the polish from Box 1.
boxes[1].remove('polish')

# Remove the ocean and the cup from Box 1.
boxes[1].remove('ocean')
boxes[1].remove('cup')

# Replace the clock and the leaf and the thunder with the apple and the wallet and the sandals in Box 5.
boxes[5].remove('clock')
boxes[5].remove('thunder')
boxes[5].remove('leaf')
boxes[5].append('apple')
boxes[5].append('wallet')
boxes[5].append('sandals')

# Remove the pillow and the blanket and the tape from Box 0.
boxes[0].remove('pillow')
boxes[0].remove('blanket')
boxes[0].remove('tape')

# Remove the mountain from Box 6.
boxes[6].remove('mountain')

# Remove the sandals from Box 5.
boxes[5].remove('sandals')

# Put the shampoo and the brush and the cup into Box 6.
boxes[6].append('shampoo')
boxes[6].append('brush')
boxes[6].append('cup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")