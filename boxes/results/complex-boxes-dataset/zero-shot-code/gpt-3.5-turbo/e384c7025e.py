box = {
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

def print_boxes():
    for i in range(11):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

# Remove the belt from Box 3
box[3].remove('belt')

# Swap the skirt in Box 2 with the console in Box 4
box[2], box[4] = box[4], box[2]

# Swap the ship in Box 2 with the fork in Box 0
box[0], box[2] = box[2], box[0]

# Put the gloves and the rock into Box 8
box[8] = ['gloves', 'rock']

# Move the skirt from Box 4 to Box 8
box[8].append(box[4].pop())

# Move the ship from Box 0 to Box 9
box[9].append(box[0].pop())

# Put the jacket and the dolphin into Box 9
box[9].extend(['jacket', 'dolphin'])

# Remove the rock and the skirt and the gloves from Box 8
box[8] = []

# Move the coin and the oven from Box 7 to Box 9
box[9].extend(box[7].pop(0))
box[9].extend(box[7].pop(0))

# Move the console from Box 2 to Box 9
box[9].append(box[2].pop())

# Remove the needle and the bag from Box 10
box[10].remove('needle')
box[10].remove('bag')

# Swap the river in Box 5 with the boot in Box 7
box[5], box[7] = box[7], box[5]

# Remove the elephant and the coin from Box 9
box[9].remove('elephant')
box[9].remove('coin')

# Swap the harmonica in Box 10 with the boot in Box 5
box[5], box[10] = box[10], box[5]

# Move the tiger from Box 1 to Box 10
box[10].append(box[1].pop())

# Swap the river in Box 7 with the laptop in Box 2
box[2], box[7] = box[7], box[2]

# Print the boxes
print_boxes()