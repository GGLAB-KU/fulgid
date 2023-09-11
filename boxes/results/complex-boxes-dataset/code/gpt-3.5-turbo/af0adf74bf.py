# Initial state of boxes
boxes = {
    0: ['telescope'],
    1: ['comb', 'starfish'],
    2: ['earring', 'bear', 'shoes'],
    3: ['pen'],
    4: ['grass', 'candle'],
    5: ['submarine', 'laptop', 'clock', 'drum'],
    6: ['cat'],
    7: ['spoon'],
    8: ['keyboard'],
    9: ['game', 'boot', 'lipstick'],
    10: ['scissors', 'jacket', 'blender', 'card', 'harmonica'],
    11: ['cloud', 'paint', 'chair'],
    12: ['grinder', 'lion', 'flute', 'seaweed', 'soap']
}

# Replace the keyboard with the table in Box 8.
boxes[8].remove('keyboard')
boxes[8].append('table')

# Replace the grass with the shirt in Box 4.
boxes[4].remove('grass')
boxes[4].append('shirt')

# Put the crown into Box 5.
boxes[5].append('crown')

# Move the cat from Box 6 to Box 7.
boxes[6].remove('cat')
boxes[7].append('cat')

# Move the cloud and the chair from Box 11 to Box 8.
boxes[11].remove('cloud')
boxes[11].remove('chair')
boxes[8].append('cloud')
boxes[8].append('chair')

# Put the glasses and the brush into Box 4.
boxes[4].append('glasses')
boxes[4].append('brush')

# Put the pen and the dice and the starfish into Box 2.
boxes[2].append('pen')
boxes[2].append('dice')
boxes[2].append('starfish')

# Remove the crown from Box 5.
boxes[5].remove('crown')

# Put the earring into Box 11.
boxes[11].append('earring')

# Swap the seaweed in Box 12 with the clock in Box 5.
boxes[12].remove('seaweed')
boxes[5].remove('clock')
boxes[12].append('clock')
boxes[5].append('seaweed')

# Put the shorts and the basket into Box 1.
boxes[1].append('shorts')
boxes[1].append('basket')

# Replace the pen with the seaweed in Box 3.
boxes[3].remove('pen')
boxes[3].append('seaweed')

# Replace the laptop and the seaweed with the violin and the button in Box 5.
boxes[5].remove('laptop')
boxes[5].remove('seaweed')
boxes[5].append('violin')
boxes[5].append('button')

# Move the seaweed from Box 3 to Box 4.
boxes[3].remove('seaweed')
boxes[4].append('seaweed')

# Remove the violin and the drum and the submarine from Box 5.
boxes[5].remove('violin')
boxes[5].remove('drum')
boxes[5].remove('submarine')

# Swap the candle in Box 4 with the lipstick in Box 9.
boxes[4].remove('candle')
boxes[9].remove('lipstick')
boxes[4].append('lipstick')
boxes[9].append('candle')

# Swap the telescope in Box 0 with the candle in Box 9.
boxes[0].remove('telescope')
boxes[9].remove('candle')
boxes[0].append('candle')
boxes[9].append('telescope')

# Put the bus into Box 6.
boxes[6].append('bus')

# Empty Box 11.
boxes[11] = []

# Put the mixer and the shoes and the comet into Box 6.
boxes[6].append('mixer')
boxes[6].append('shoes')
boxes[6].append('comet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")