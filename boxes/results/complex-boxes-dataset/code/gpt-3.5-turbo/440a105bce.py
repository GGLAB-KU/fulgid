# Initial state of boxes
boxes = {
    0: ['soap'],
    1: ['camera', 'pants', 'tiger', 'cloud', 'brush'],
    2: ['piano', 'storm', 'cow'],
    3: [],
    4: ['oven', 'forest'],
    5: ['plane', 'boat', 'book', 'fork'],
    6: ['mixer', 'starfish', 'tie'],
    7: ['lipstick'],
    8: ['bag', 'controller'],
    9: [],
    10: ['wig', 'violin', 'thread'],
    11: [],
    12: []
}

# Swap the soap in Box 0 with the brush in Box 1.
boxes[0].remove('soap')
boxes[1].remove('brush')
boxes[0].append('brush')
boxes[1].append('soap')

# Move the mixer and the starfish from Box 6 to Box 11.
boxes[6].remove('mixer')
boxes[6].remove('starfish')
boxes[11].append('mixer')
boxes[11].append('starfish')

# Empty Box 5.
boxes[5] = []

# Move the tie from Box 6 to Box 12.
boxes[6].remove('tie')
boxes[12].append('tie')

# Put the harmonica into Box 5.
boxes[5].append('harmonica')

# Move the bag and the controller from Box 8 to Box 2.
boxes[8].remove('bag')
boxes[8].remove('controller')
boxes[2].append('bag')
boxes[2].append('controller')

# Replace the lipstick with the comb in Box 7.
boxes[7].remove('lipstick')
boxes[7].append('comb')

# Put the headphone and the cup into Box 7.
boxes[7].append('headphone')
boxes[7].append('cup')

# Remove the bag and the cow from Box 2.
boxes[2].remove('bag')
boxes[2].remove('cow')

# Swap the pants in Box 1 with the tie in Box 12.
boxes[1].remove('pants')
boxes[12].remove('tie')
boxes[1].append('tie')
boxes[12].append('pants')

# Move the forest from Box 4 to Box 2.
boxes[4].remove('forest')
boxes[2].append('forest')

# Empty Box 10.
boxes[10] = []

# Move the comb from Box 7 to Box 10.
boxes[7].remove('comb')
boxes[10].append('comb')

# Remove the harmonica from Box 5.
boxes[5].remove('harmonica')

# Put the glasses and the magnet into Box 7.
boxes[7].append('glasses')
boxes[7].append('magnet')

# Swap the mixer in Box 11 with the comb in Box 10.
boxes[11].remove('mixer')
boxes[10].remove('comb')
boxes[11].append('comb')
boxes[10].append('mixer')

# Move the brush from Box 0 to Box 11.
boxes[0].remove('brush')
boxes[11].append('brush')

# Move the brush and the starfish from Box 11 to Box 6.
boxes[11].remove('brush')
boxes[11].remove('starfish')
boxes[6].append('brush')
boxes[6].append('starfish')

# Move the brush and the starfish from Box 6 to Box 12.
boxes[6].remove('brush')
boxes[6].remove('starfish')
boxes[12].append('brush')
boxes[12].append('starfish')

# Swap the cloud in Box 1 with the piano in Box 2.
boxes[1].remove('cloud')
boxes[2].remove('piano')
boxes[1].append('piano')
boxes[2].append('cloud')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")