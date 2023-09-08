# Initial state of boxes
boxes = {
    0: ['forest', 'makeup', 'comet', 'jungle', 'bowl'],
    1: [],
    2: ['blender'],
    3: [],
    4: ['umbrella'],
    5: ['storm', 'toy', 'tape', 'moon'],
    6: ['bicycle', 'cow', 'cup', 'lock', 'skirt'],
    7: ['button', 'shelf'],
    8: ['drum'],
    9: [],
    10: ['game', 'ocean', 'sandals', 'coral'],
    11: [],
    12: ['dice', 'lipstick']
}

# Move the bowl and the makeup from Box 0 to Box 1.
boxes[0].remove('bowl')
boxes[0].remove('makeup')
boxes[1].append('bowl')
boxes[1].append('makeup')

# Move the jungle and the comet from Box 0 to Box 3.
boxes[0].remove('jungle')
boxes[0].remove('comet')
boxes[3].append('jungle')
boxes[3].append('comet')

# Move the cup from Box 6 to Box 7.
boxes[6].remove('cup')
boxes[7].append('cup')

# Move the dice and the lipstick from Box 12 to Box 7.
boxes[12].remove('dice')
boxes[12].remove('lipstick')
boxes[7].append('dice')
boxes[7].append('lipstick')

# Put the hat and the needle into Box 9.
boxes[9].append('hat')
boxes[9].append('needle')

# Swap the storm in Box 5 with the bicycle in Box 6.
boxes[5].remove('storm')
boxes[6].remove('bicycle')
boxes[5].append('bicycle')
boxes[6].append('storm')

# Replace the makeup and the bowl with the pillow and the mirror in Box 1.
boxes[1].remove('makeup')
boxes[1].remove('bowl')
boxes[1].append('pillow')
boxes[1].append('mirror')

# Remove the blender from Box 2.
boxes[2].remove('blender')

# Swap the drum in Box 8 with the forest in Box 0.
boxes[8].remove('drum')
boxes[0].remove('forest')
boxes[8].append('forest')
boxes[0].append('drum')

# Put the lion and the soap and the car into Box 10.
boxes[10].append('lion')
boxes[10].append('soap')
boxes[10].append('car')

# Put the puzzle and the book and the mountain into Box 4.
boxes[4].append('puzzle')
boxes[4].append('book')
boxes[4].append('mountain')

# Remove the cup and the dice from Box 7.
boxes[7].remove('cup')
boxes[7].remove('dice')

# Move the bicycle from Box 5 to Box 9.
boxes[5].remove('bicycle')
boxes[9].append('bicycle')

# Put the camera and the makeup and the bicycle into Box 8.
boxes[8].append('camera')
boxes[8].append('makeup')
boxes[8].append('bicycle')

# Remove the umbrella and the mountain and the book from Box 4.
boxes[4].remove('umbrella')
boxes[4].remove('mountain')
boxes[4].remove('book')

# Put the telescope and the island into Box 7.
boxes[7].append('telescope')
boxes[7].append('island')

# Replace the island and the telescope with the card and the apple in Box 7.
boxes[7].remove('island')
boxes[7].remove('telescope')
boxes[7].append('card')
boxes[7].append('apple')

# Move the storm and the skirt and the lock from Box 6 to Box 0.
boxes[6].remove('storm')
boxes[6].remove('skirt')
boxes[6].remove('lock')
boxes[0].append('storm')
boxes[0].append('skirt')
boxes[0].append('lock')

# Remove the puzzle from Box 4.
boxes[4].remove('puzzle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")