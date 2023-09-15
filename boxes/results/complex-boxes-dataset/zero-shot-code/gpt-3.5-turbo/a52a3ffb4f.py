box = {
    0: ['shampoo'],
    1: ['ocean', 'bird', 'thread', 'dolphin'],
    2: ['piano', 'phone'],
    3: ['freezer'],
    4: [],
    5: ['wig', 'dice', 'gloves'],
    6: ['shelf', 'tiger'],
    7: ['butterfly'],
    8: ['boat', 'rocket'],
    9: [],
    10: ['skirt', 'coin', 'note', 'grinder']
}

def print_boxes():
    for i in range(11):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

# Swap the shampoo in Box 0 with the freezer in Box 3
box[0], box[3] = box[3], box[0]

# Put the grinder and the piano into Box 3
box[3].extend(['grinder', 'piano'])

# Move the grinder and the piano and the shampoo from Box 3 to Box 4
box[4].extend(box[3])
box[3] = []

# Swap the shelf in Box 6 with the dice in Box 5
box[6], box[5] = box[5], box[6]

# Move the gloves and the wig from Box 5 to Box 7
box[7].extend(box[5])
box[5] = []

# Replace the freezer with the charger in Box 0
box[0] = ['charger']

# Replace the charger with the bird in Box 0
box[0] = ['bird']

# Replace the dolphin and the bird with the headphone and the table in Box 1
box[1] = ['headphone', 'table']

# Remove the bird from Box 0
box[0] = []

# Remove the note from Box 10
box[10].remove('note')

# Empty Box 8
box[8] = []

# Put the submarine and the candle and the toaster into Box 9
box[9].extend(['submarine', 'candle', 'toaster'])

# Move the gloves and the butterfly from Box 7 to Box 4
box[4].extend(['gloves', 'butterfly'])
box[7] = []

# Replace the shelf with the lamp in Box 5
box[5] = ['lamp']

# Put the pants and the doll into Box 8
box[8] = ['pants', 'doll']

# Move the coin from Box 10 to Box 3
box[3].append(box[10].pop(box[10].index('coin')))

# Swap the candle in Box 9 with the coin in Box 3
box[9][box[9].index('candle')], box[3][box[3].index('coin')] = box[3][box[3].index('coin')], box[9][box[9].index('candle')]

print_boxes()