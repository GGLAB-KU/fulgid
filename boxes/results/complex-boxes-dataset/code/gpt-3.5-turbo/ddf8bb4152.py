# Initial state of boxes
boxes = {
    0: ['clock', 'island', 'bell', 'snow'],
    1: ['paint'],
    2: ['microscope', 'bracelet', 'shelf', 'table'],
    3: ['key', 'thunder', 'zipper', 'bowl', 'horse'],
    4: ['shorts', 'magnet', 'brush'],
    5: [],
    6: ['rocket', 'vase', 'battery'],
    7: []
}

# Put the paint into Box 3.
boxes[3].append('paint')

# Swap the battery in Box 6 with the clock in Box 0.
boxes[0].remove('clock')
boxes[6].remove('battery')
boxes[0].append('battery')
boxes[6].append('clock')

# Empty Box 0.
boxes[0] = []

# Empty Box 4.
boxes[4] = []

# Put the toothbrush and the umbrella into Box 1.
boxes[1].append('toothbrush')
boxes[1].append('umbrella')

# Move the thunder from Box 3 to Box 2.
boxes[2].append(boxes[3].pop(boxes[3].index('thunder')))

# Replace the umbrella and the toothbrush and the paint with the doll and the skirt and the mask in Box 1.
boxes[1].remove('umbrella')
boxes[1].remove('toothbrush')
boxes[1].remove('paint')
boxes[1].append('doll')
boxes[1].append('skirt')
boxes[1].append('mask')

# Put the helmet into Box 0.
boxes[0].append('helmet')

# Swap the helmet in Box 0 with the clock in Box 6.
boxes[0].remove('helmet')
boxes[6].remove('clock')
boxes[0].append('clock')
boxes[6].append('helmet')

# Move the helmet from Box 6 to Box 2.
boxes[2].append(boxes[6].pop(boxes[6].index('helmet')))

# Move the skirt and the doll from Box 1 to Box 7.
boxes[7].append(boxes[1].pop(boxes[1].index('skirt')))
boxes[7].append(boxes[1].pop(boxes[1].index('doll')))

# Empty Box 1.
boxes[1] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")