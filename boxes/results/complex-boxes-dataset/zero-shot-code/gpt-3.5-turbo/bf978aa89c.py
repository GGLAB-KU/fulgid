box = {
    0: ['flower'],
    1: ['bracelet'],
    2: ['plate'],
    3: ['game'],
    4: ['rock', 'toothbrush', 'clock'],
    5: ['bird', 'toy'],
    6: ['doll', 'swimsuit', 'boot', 'controller', 'horn'],
    7: [],
    8: [],
    9: ['telescope', 'freezer'],
    10: ['table'],
    11: ['brush', 'spoon']
}

# Remove the spoon and the brush from Box 11
box[11].remove('spoon')
box[11].remove('brush')

# Swap the bracelet in Box 1 with the rock in Box 4
box[1], box[4] = box[4], box[1]

# Swap the rock in Box 1 with the table in Box 10
box[1], box[10] = box[10], box[1]

# Move the table from Box 1 to Box 10
box[10].append(box[1].pop())

# Remove the freezer from Box 9
box[9].remove('freezer')

# Remove the controller and the swimsuit from Box 6
box[6].remove('controller')
box[6].remove('swimsuit')

# Swap the toothbrush in Box 4 with the telescope in Box 9
box[4], box[9] = box[9], box[4]

# Swap the toothbrush in Box 9 with the bird in Box 5
box[9], box[5] = box[5], box[9]

# Move the telescope and the bracelet from Box 4 to Box 6
box[6].extend(box[4])
box[4] = []

# Remove the bird from Box 9
box[9].remove('bird')

# Replace the bracelet and the horn and the boot with the island and the submarine and the rock in Box 6
box[6] = ['island', 'submarine', 'rock']

# Put the button and the lamp and the game into Box 7
box[7].extend(['button', 'lamp', 'game'])

# Move the game from Box 3 to Box 7
box[7].append(box[3].pop())

# Remove the telescope from Box 6
box[6].remove('telescope')

# Replace the toy with the forest in Box 5
box[5] = ['forest']

# Remove the flower from Box 0
box[0].remove('flower')

# Remove the plate from Box 2
box[2].remove('plate')

# Swap the button in Box 7 with the doll in Box 6
box[7], box[6] = box[6], box[7]

# Print the contents of each box
for i in range(12):
    print(f"Box {i}: {box[i]}")