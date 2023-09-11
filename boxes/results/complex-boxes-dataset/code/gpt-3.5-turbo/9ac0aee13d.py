# Initial state of boxes
boxes = {
    0: ['coral', 'console', 'headphone'],
    1: ['cloud', 'submarine', 'rocket', 'lamp'],
    2: [],
    3: ['razor', 'motorcycle'],
    4: ['plate', 'makeup', 'apple'],
    5: ['shelf', 'vase', 'toothbrush', 'blanket', 'toy'],
    6: [],
    7: ['scissors', 'table'],
    8: ['sock', 'whistle'],
    9: ['frame', 'lipstick', 'violin', 'island', 'storm'],
    10: ['wire', 'mask', 'umbrella', 'dress', 'shirt']
}

# Replace the shirt and the wire with the crown and the horn in Box 10.
boxes[10].remove('shirt')
boxes[10].remove('wire')
boxes[10].append('crown')
boxes[10].append('horn')

# Remove the coral from Box 0.
boxes[0].remove('coral')

# Put the lamp and the note and the tape into Box 10.
boxes[10].append('lamp')
boxes[10].append('note')
boxes[10].append('tape')

# Swap the scissors in Box 7 with the lamp in Box 1.
boxes[7].remove('scissors')
boxes[1].remove('lamp')
boxes[7].append('lamp')
boxes[1].append('scissors')

# Remove the headphone from Box 0.
boxes[0].remove('headphone')

# Put the paint and the grinder and the battery into Box 5.
boxes[5].append('paint')
boxes[5].append('grinder')
boxes[5].append('battery')

# Remove the whistle from Box 8.
boxes[8].remove('whistle')

# Replace the table and the lamp with the tiger and the microwave in Box 7.
boxes[7].remove('table')
boxes[7].remove('lamp')
boxes[7].append('tiger')
boxes[7].append('microwave')

# Move the tiger from Box 7 to Box 2.
boxes[7].remove('tiger')
boxes[2].append('tiger')

# Put the coral and the phone and the earring into Box 0.
boxes[0].append('coral')
boxes[0].append('phone')
boxes[0].append('earring')

# Put the laptop and the thread into Box 3.
boxes[3].append('laptop')
boxes[3].append('thread')

# Remove the scissors and the submarine from Box 1.
boxes[1].remove('scissors')
boxes[1].remove('submarine')

# Remove the apple from Box 4.
boxes[4].remove('apple')

# Swap the microwave in Box 7 with the storm in Box 9.
boxes[7].remove('microwave')
boxes[9].remove('storm')
boxes[7].append('storm')
boxes[9].append('microwave')

# Put the lightning and the paint and the cup into Box 2.
boxes[2].append('lightning')
boxes[2].append('paint')
boxes[2].append('cup')

# Empty Box 5.
boxes[5] = []

# Swap the storm in Box 7 with the motorcycle in Box 3.
boxes[7].remove('storm')
boxes[3].remove('motorcycle')
boxes[7].append('motorcycle')
boxes[3].append('storm')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")