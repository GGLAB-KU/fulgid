box = {
    0: ['lipstick'],
    1: ['key'],
    2: ['coral', 'pen', 'toothpaste'],
    3: ['piano', 'basket', 'toothbrush'],
    4: ['starfish'],
    5: ['dress', 'crown', 'boat', 'tiger', 'doll'],
    6: ['apple', 'rock'],
    7: [],
    8: ['button', 'charger'],
    9: [],
    10: []
}

# Replace the starfish with the motorcycle in Box 4
box[4] = ['motorcycle']

# Swap the lipstick in Box 0 with the button in Box 8
box[0], box[8] = box[8], box[0]

# Move the button from Box 0 to Box 8
box[8].append(box[0].pop())

# Move the piano from Box 3 to Box 2
box[2].append(box[3].pop(0))

# Replace the pen and the piano and the toothpaste with the dog and the coat and the earring in Box 2
box[2] = ['dog', 'coat', 'earring']

# Remove the toothbrush from Box 3
box[3].remove('toothbrush')

# Swap the motorcycle in Box 4 with the basket in Box 3
box[4], box[3] = box[3], box[4]

# Put the table into Box 10
box[10].append('table')

# Move the basket from Box 4 to Box 5
box[5].append(box[4].pop())

# Move the motorcycle from Box 3 to Box 0
box[0].append(box[3].pop())

# Remove the table from Box 10
box[10].remove('table')

# Move the button and the lipstick and the charger from Box 8 to Box 7
box[7].extend(box[8])
box[8] = []

# Move the basket and the doll and the crown from Box 5 to Box 0
box[0].extend(box[5][:3])
box[5] = box[5][3:]

# Move the key from Box 1 to Box 4
box[4].append(box[1].pop())

# Put the perfume into Box 4
box[4].append('perfume')

# Put the skirt and the basket and the candle into Box 9
box[9].extend(['skirt', 'basket', 'candle'])

# Print the contents of each box
for i in range(11):
    print(f"Box {i}: {box[i]}")