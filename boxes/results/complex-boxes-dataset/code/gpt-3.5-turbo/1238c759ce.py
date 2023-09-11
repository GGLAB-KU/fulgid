# Initial state of boxes
boxes = {
    0: ['plate', 'gloves', 'telescope', 'dolphin'],
    1: [],
    2: ['crown'],
    3: ['blender'],
    4: ['frame', 'paint', 'battery'],
    5: ['cat', 'pot', 'basket'],
    6: ['lion'],
    7: ['shelf', 'star', 'wire', 'swimsuit'],
    8: ['bag', 'mountain'],
    9: ['needle', 'shampoo', 'thunder', 'coat'],
    10: ['glove', 'cow', 'horse'],
    11: ['brush', 'butterfly'],
    12: []
}

# Move the brush and the butterfly from Box 11 to Box 12.
boxes[11].remove('brush')
boxes[11].remove('butterfly')
boxes[12].append('brush')
boxes[12].append('butterfly')

# Move the frame and the battery from Box 4 to Box 2.
boxes[4].remove('frame')
boxes[4].remove('battery')
boxes[2].append('frame')
boxes[2].append('battery')

# Put the cow into Box 11.
boxes[10].remove('cow')
boxes[11].append('cow')

# Remove the mountain and the bag from Box 8.
boxes[8].remove('mountain')
boxes[8].remove('bag')

# Swap the gloves in Box 0 with the brush in Box 12.
boxes[0].remove('gloves')
boxes[12].remove('brush')
boxes[0].append('brush')
boxes[12].append('gloves')

# Swap the lion in Box 6 with the frame in Box 2.
boxes[6].remove('lion')
boxes[2].remove('frame')
boxes[6].append('frame')
boxes[2].append('lion')

# Remove the shampoo and the coat and the thunder from Box 9.
boxes[9].remove('shampoo')
boxes[9].remove('coat')
boxes[9].remove('thunder')

# Put the swimsuit into Box 9.
boxes[5].remove('swimsuit')
boxes[9].append('swimsuit')

# Move the basket from Box 5 to Box 7.
boxes[5].remove('basket')
boxes[7].append('basket')

# Put the lion into Box 12.
boxes[6].remove('lion')
boxes[12].append('lion')

# Remove the pot from Box 5.
boxes[5].remove('pot')

# Move the cow from Box 11 to Box 2.
boxes[11].remove('cow')
boxes[2].append('cow')

# Move the frame from Box 6 to Box 12.
boxes[6].remove('frame')
boxes[12].append('frame')

# Swap the cat in Box 5 with the star in Box 7.
boxes[5].remove('cat')
boxes[7].remove('star')
boxes[5].append('star')
boxes[7].append('cat')

# Move the paint from Box 4 to Box 9.
boxes[4].remove('paint')
boxes[9].append('paint')

# Swap the horse in Box 10 with the cat in Box 7.
boxes[10].remove('horse')
boxes[7].remove('cat')
boxes[10].append('cat')
boxes[7].append('horse')

# Replace the needle and the paint with the cup and the chair in Box 9.
boxes[9].remove('needle')
boxes[9].remove('paint')
boxes[9].append('cup')
boxes[9].append('chair')

# Remove the lion from Box 12.
boxes[12].remove('lion')

# Swap the star in Box 5 with the crown in Box 2.
boxes[5].remove('star')
boxes[2].remove('crown')
boxes[5].append('crown')
boxes[2].append('star')

# Replace the battery and the lion with the snow and the pillow in Box 2.
boxes[2].remove('battery')
boxes[2].remove('lion')
boxes[2].append('snow')
boxes[2].append('pillow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")