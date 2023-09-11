# Initial state of boxes
boxes = {
    0: ['octopus', 'dog'],
    1: ['doll', 'violin', 'piano', 'pan', 'butterfly'],
    2: ['tie', 'freezer'],
    3: ['grinder', 'camera', 'scarf', 'pot', 'gloves'],
    4: [],
    5: ['blender', 'candle'],
    6: ['grass', 'bear', 'drum'],
    7: ['sock', 'lamp'],
    8: [],
    9: ['jacket'],
    10: ['shampoo', 'branch', 'desert', 'thread', 'table'],
    11: ['skirt'],
    12: ['spoon', 'pants', 'sandals']
}

# Remove the jacket from Box 9.
boxes[9].remove('jacket')

# Put the starfish and the boat into Box 2.
boxes[2].append('starfish')
boxes[2].append('boat')

# Replace the table and the desert with the boot and the cat in Box 10.
boxes[10].remove('table')
boxes[10].remove('desert')
boxes[10].append('boot')
boxes[10].append('cat')

# Swap the skirt in Box 11 with the blender in Box 5.
boxes[11].remove('skirt')
boxes[5].remove('blender')
boxes[11].append('blender')
boxes[5].append('skirt')

# Remove the bear and the grass and the drum from Box 6.
boxes[6].remove('bear')
boxes[6].remove('grass')
boxes[6].remove('drum')

# Empty Box 12.
boxes[12] = []

# Replace the boot and the cat and the shampoo with the cloud and the keyboard and the microscope in Box 10.
boxes[10].remove('boot')
boxes[10].remove('cat')
boxes[10].remove('shampoo')
boxes[10].append('cloud')
boxes[10].append('keyboard')
boxes[10].append('microscope')

# Remove the boat from Box 2.
boxes[2].remove('boat')

# Move the grinder from Box 3 to Box 4.
boxes[3].remove('grinder')
boxes[4].append('grinder')

# Move the gloves from Box 3 to Box 0.
boxes[3].remove('gloves')
boxes[0].append('gloves')

# Swap the sock in Box 7 with the blender in Box 11.
boxes[7].remove('sock')
boxes[11].remove('blender')
boxes[7].append('blender')
boxes[11].append('sock')

# Put the sculpture and the starfish and the grass into Box 1.
boxes[1].append('sculpture')
boxes[1].append('starfish')
boxes[1].append('grass')

# Remove the lamp from Box 7.
boxes[7].remove('lamp')

# Put the razor and the button and the bird into Box 3.
boxes[3].append('razor')
boxes[3].append('button')
boxes[3].append('bird')

# Replace the thread and the branch and the microscope with the bicycle and the whistle and the wallet in Box 10.
boxes[10].remove('thread')
boxes[10].remove('branch')
boxes[10].remove('microscope')
boxes[10].append('bicycle')
boxes[10].append('whistle')
boxes[10].append('wallet')

# Swap the octopus in Box 0 with the blender in Box 7.
boxes[0].remove('octopus')
boxes[7].remove('blender')
boxes[0].append('blender')
boxes[7].append('octopus')

# Swap the camera in Box 3 with the whistle in Box 10.
boxes[3].remove('camera')
boxes[10].remove('whistle')
boxes[3].append('whistle')
boxes[10].append('camera')

# Remove the grinder from Box 4.
boxes[4].remove('grinder')

# Put the lipstick into Box 9.
boxes[9].append('lipstick')

# Remove the piano and the sculpture and the starfish from Box 1.
boxes[1].remove('piano')
boxes[1].remove('sculpture')
boxes[1].remove('starfish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")