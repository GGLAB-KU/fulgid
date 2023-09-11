# Initial state of boxes
boxes = {
    0: ['console', 'chair', 'sock', 'dice', 'forest'],
    1: ['towel', 'battery'],
    2: ['fork', 'shampoo', 'scarf', 'scissors'],
    3: ['ship'],
    4: ['necklace', 'fish'],
    5: ['starfish', 'cloud', 'motorcycle', 'bell'],
    6: ['toothpaste', 'crown', 'bowl', 'freezer', 'blender'],
    7: ['pants', 'keyboard', 'needle', 'bus'],
    8: []
}

# Remove the starfish and the cloud from Box 5.
boxes[5].remove('starfish')
boxes[5].remove('cloud')

# Put the controller into Box 7.
boxes[7].append('controller')

# Put the flute and the cat and the whistle into Box 7.
boxes[7].append('flute')
boxes[7].append('cat')
boxes[7].append('whistle')

# Remove the scarf from Box 2.
boxes[2].remove('scarf')

# Put the whistle and the tape into Box 3.
boxes[3].append('whistle')
boxes[3].append('tape')

# Swap the tape in Box 3 with the fish in Box 4.
boxes[3].remove('tape')
boxes[4].remove('fish')
boxes[3].append('fish')
boxes[4].append('tape')

# Put the tie into Box 3.
boxes[3].append('tie')

# Replace the chair and the console with the car and the truck in Box 0.
boxes[0].remove('chair')
boxes[0].remove('console')
boxes[0].append('car')
boxes[0].append('truck')

# Remove the car from Box 0.
boxes[0].remove('car')

# Move the ship and the whistle from Box 3 to Box 5.
boxes[3].remove('ship')
boxes[3].remove('whistle')
boxes[5].append('ship')
boxes[5].append('whistle')

# Swap the blender in Box 6 with the keyboard in Box 7.
boxes[6].remove('blender')
boxes[7].remove('keyboard')
boxes[6].append('keyboard')
boxes[7].append('blender')

# Remove the bus and the whistle and the pants from Box 7.
boxes[7].remove('bus')
boxes[7].remove('whistle')
boxes[7].remove('pants')

# Replace the keyboard and the toothpaste with the rocket and the submarine in Box 6.
boxes[6].remove('keyboard')
boxes[6].remove('toothpaste')
boxes[6].append('rocket')
boxes[6].append('submarine')

# Move the needle and the flute and the blender from Box 7 to Box 6.
boxes[7].remove('needle')
boxes[7].remove('flute')
boxes[7].remove('blender')
boxes[6].append('needle')
boxes[6].append('flute')
boxes[6].append('blender')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")