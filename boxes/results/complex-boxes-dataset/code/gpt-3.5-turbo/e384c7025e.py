# Initial state of boxes
boxes = {
    0: ['fork'],
    1: ['tiger', 'bird', 'zipper', 'mountain', 'bus'],
    2: ['skirt', 'ship', 'laptop'],
    3: ['belt'],
    4: ['console'],
    5: ['river'],
    6: [],
    7: ['coin', 'boot', 'oven'],
    8: [],
    9: ['elephant', 'submarine'],
    10: ['bag', 'needle', 'harmonica']
}

# Remove the belt from Box 3.
boxes[3].remove('belt')

# Swap the skirt in Box 2 with the console in Box 4.
boxes[2].remove('skirt')
boxes[4].remove('console')
boxes[2].append('console')
boxes[4].append('skirt')

# Swap the ship in Box 2 with the fork in Box 0.
boxes[2].remove('ship')
boxes[0].remove('fork')
boxes[2].append('fork')
boxes[0].append('ship')

# Put the gloves and the rock into Box 8.
boxes[8].append('gloves')
boxes[8].append('rock')

# Move the skirt from Box 4 to Box 8.
boxes[4].remove('skirt')
boxes[8].append('skirt')

# Move the ship from Box 0 to Box 9.
boxes[0].remove('ship')
boxes[9].append('ship')

# Put the jacket and the dolphin into Box 9.
boxes[9].append('jacket')
boxes[9].append('dolphin')

# Remove the rock and the skirt and the gloves from Box 8.
boxes[8].remove('rock')
boxes[8].remove('skirt')
boxes[8].remove('gloves')

# Move the coin and the oven from Box 7 to Box 9.
boxes[7].remove('coin')
boxes[7].remove('oven')
boxes[9].append('coin')
boxes[9].append('oven')

# Move the console from Box 2 to Box 9.
boxes[2].remove('console')
boxes[9].append('console')

# Remove the needle and the bag from Box 10.
boxes[10].remove('needle')
boxes[10].remove('bag')

# Swap the river in Box 5 with the boot in Box 7.
boxes[5].remove('river')
boxes[7].remove('boot')
boxes[5].append('boot')
boxes[7].append('river')

# Remove the elephant and the coin from Box 9.
boxes[9].remove('elephant')
boxes[9].remove('coin')

# Swap the harmonica in Box 10 with the boot in Box 5.
boxes[10].remove('harmonica')
boxes[5].remove('boot')
boxes[10].append('boot')
boxes[5].append('harmonica')

# Move the tiger from Box 1 to Box 10.
boxes[1].remove('tiger')
boxes[10].append('tiger')

# Swap the river in Box 7 with the laptop in Box 2.
boxes[7].remove('river')
boxes[2].remove('laptop')
boxes[7].append('laptop')
boxes[2].append('river')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")