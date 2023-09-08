# Initial state of boxes
boxes = {
    0: ['thunder'],
    1: ['river'],
    2: ['bracelet', 'needle', 'towel', 'submarine'],
    3: [],
    4: ['spoon', 'perfume', 'island', 'truck'],
    5: ['boat'],
    6: ['train'],
    7: ['pen', 'oven', 'bag', 'bicycle'],
    8: [],
    9: ['doll', 'storm', 'dice', 'rock'],
    10: ['crown']
}

# Swap the thunder in Box 0 with the bicycle in Box 7.
boxes[0], boxes[7] = boxes[7], boxes[0]

# Swap the crown in Box 10 with the boat in Box 5.
boxes[10], boxes[5] = boxes[5], boxes[10]

# Replace the thunder with the guitar in Box 7.
boxes[7].remove('thunder')
boxes[7].append('guitar')

# Replace the boat with the dolphin in Box 10.
boxes[10].remove('boat')
boxes[10].append('dolphin')

# Move the river from Box 1 to Box 0.
boxes[0].append(boxes[1].pop())

# Replace the river with the rocket in Box 0.
boxes[0].remove('river')
boxes[0].append('rocket')

# Remove the bag and the oven from Box 7.
boxes[7].remove('bag')
boxes[7].remove('oven')

# Swap the needle in Box 2 with the train in Box 6.
boxes[2].remove('needle')
boxes[6].remove('train')
boxes[2].append('train')
boxes[6].append('needle')

# Remove the rocket and the bicycle from Box 0.
boxes[0].remove('rocket')
boxes[0].remove('bicycle')

# Put the makeup and the snow into Box 0.
boxes[0].extend(['makeup', 'snow'])

# Empty Box 0.
boxes[0] = []

# Put the shirt into Box 4.
boxes[4].append('shirt')

# Remove the guitar from Box 7.
boxes[7].remove('guitar')

# Replace the shirt and the truck with the grass and the wire in Box 4.
boxes[4].remove('shirt')
boxes[4].remove('truck')
boxes[4].extend(['grass', 'wire'])

# Move the bracelet from Box 2 to Box 9.
boxes[2].remove('bracelet')
boxes[9].append('bracelet')

# Remove the crown from Box 5.
boxes[5].remove('crown')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")