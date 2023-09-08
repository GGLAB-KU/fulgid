# Initial state of boxes
boxes = {
    0: [],
    1: ['table', 'zipper', 'blender'],
    2: [],
    3: ['shampoo', 'skirt', 'usb'],
    4: ['shoes'],
    5: ['comet', 'fork'],
    6: ['boat', 'charger', 'pants', 'hat'],
    7: ['branch', 'cloud', 'pen', 'whistle'],
    8: ['jungle', 'watch', 'pot'],
    9: [],
    10: ['meteor', 'battery', 'grinder', 'rain', 'freezer'],
    11: [],
    12: ['console', 'piano', 'clock', 'shark', 'bell'],
    13: ['toy', 'game'],
    14: ['drum']
}

# Remove the pot and the watch and the jungle from Box 8.
boxes[8].remove('pot')
boxes[8].remove('watch')
boxes[8].remove('jungle')

# Replace the pen and the cloud and the branch with the puzzle and the note and the drum in Box 7.
boxes[7].remove('pen')
boxes[7].remove('cloud')
boxes[7].remove('branch')
boxes[7].append('puzzle')
boxes[7].append('note')
boxes[7].append('drum')

# Swap the shoes in Box 4 with the blender in Box 1.
boxes[4].remove('shoes')
boxes[1].remove('blender')
boxes[4].append('blender')
boxes[1].append('shoes')

# Put the charger into Box 7.
boxes[6].remove('charger')
boxes[7].append('charger')

# Move the pants and the hat from Box 6 to Box 11.
boxes[6].remove('pants')
boxes[6].remove('hat')
boxes[11].append('pants')
boxes[11].append('hat')

# Replace the drum with the clock in Box 14.
boxes[14].remove('drum')
boxes[14].append('clock')

# Swap the blender in Box 4 with the toy in Box 13.
boxes[4].remove('blender')
boxes[13].remove('toy')
boxes[4].append('toy')
boxes[13].append('blender')

# Swap the comet in Box 5 with the toy in Box 4.
boxes[5].remove('comet')
boxes[4].remove('toy')
boxes[5].append('toy')
boxes[4].append('comet')

# Swap the charger in Box 7 with the rain in Box 10.
boxes[7].remove('charger')
boxes[10].remove('rain')
boxes[7].append('rain')
boxes[10].append('charger')

# Move the fork from Box 5 to Box 10.
boxes[5].remove('fork')
boxes[10].append('fork')

# Remove the shampoo and the skirt and the usb from Box 3.
boxes[3].remove('shampoo')
boxes[3].remove('skirt')
boxes[3].remove('usb')

# Swap the hat in Box 11 with the boat in Box 6.
boxes[11].remove('hat')
boxes[6].remove('boat')
boxes[11].append('boat')
boxes[6].append('hat')

# Remove the clock from Box 14.
boxes[14].remove('clock')

# Replace the toy with the shoe in Box 5.
boxes[5].remove('toy')
boxes[5].append('shoe')

# Swap the shoe in Box 5 with the drum in Box 7.
boxes[5].remove('shoe')
boxes[7].remove('drum')
boxes[5].append('drum')
boxes[7].append('shoe')

# Put the camera and the swimsuit and the lamp into Box 1.
items_to_put = ['camera', 'swimsuit', 'lamp']
for item in items_to_put:
    boxes[1].append(item)

# Remove the charger and the hat from Box 6.
boxes[6].remove('charger')
boxes[6].remove('hat')

# Swap the battery in Box 10 with the comet in Box 4.
boxes[10].remove('battery')
boxes[4].remove('comet')
boxes[10].append('comet')
boxes[4].append('battery')

# Swap the meteor in Box 10 with the battery in Box 4.
boxes[10].remove('meteor')
boxes[4].remove('battery')
boxes[10].append('battery')
boxes[4].append('meteor')

# Replace the drum with the bird in Box 5.
boxes[5].remove('drum')
boxes[5].append('bird')

# Swap the game in Box 13 with the grinder in Box 10.
boxes[13].remove('game')
boxes[10].remove('grinder')
boxes[13].append('grinder')
boxes[10].append('game')

# Move the meteor from Box 4 to Box 10.
boxes[4].remove('meteor')
boxes[10].append('meteor')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")