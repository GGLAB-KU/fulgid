# Initial state of boxes
boxes = {
    0: ['car', 'moon', 'plate', 'blanket', 'desert'],
    1: [],
    2: ['planet', 'comb', 'meteor'],
    3: ['game', 'console', 'glasses'],
    4: ['phone', 'soap', 'tape', 'ocean', 'card'],
    5: ['lock', 'blender', 'cat', 'bowl', 'butterfly'],
    6: ['doll'],
    7: ['toothpaste', 'frame', 'sun', 'dress'],
    8: [],
    9: [],
    10: ['makeup'],
    11: ['snow', 'needle', 'island', 'earring']
}

# Move the doll from Box 6 to Box 8.
boxes[6].remove('doll')
boxes[8].append('doll')

# Remove the planet and the meteor from Box 2.
boxes[2].remove('planet')
boxes[2].remove('meteor')

# Remove the makeup from Box 10.
boxes[10].remove('makeup')

# Move the doll from Box 8 to Box 9.
boxes[8].remove('doll')
boxes[9].append('doll')

# Remove the comb from Box 2.
boxes[2].remove('comb')

# Remove the island and the snow and the earring from Box 11.
boxes[11].remove('island')
boxes[11].remove('snow')
boxes[11].remove('earring')

# Move the needle from Box 11 to Box 7.
boxes[11].remove('needle')
boxes[7].append('needle')

# Remove the game and the console from Box 3.
boxes[3].remove('game')
boxes[3].remove('console')

# Move the doll from Box 9 to Box 1.
boxes[9].remove('doll')
boxes[1].append('doll')

# Swap the car in Box 0 with the bowl in Box 5.
boxes[0].remove('car')
boxes[5].remove('bowl')
boxes[0].append('bowl')
boxes[5].append('car')

# Remove the doll from Box 1.
boxes[1].remove('doll')

# Put the skirt and the coin and the soap into Box 3.
items_to_move = ['skirt', 'coin', 'soap']
for item in items_to_move:
    boxes[3].append(item)

# Put the belt and the moon into Box 6.
items_to_move = ['belt', 'moon']
for item in items_to_move:
    boxes[6].append(item)

# Remove the frame and the toothpaste from Box 7.
boxes[7].remove('frame')
boxes[7].remove('toothpaste')

# Put the guitar and the violin into Box 6.
items_to_move = ['guitar', 'violin']
for item in items_to_move:
    boxes[6].append(item)

# Swap the dress in Box 7 with the moon in Box 0.
boxes[7].remove('dress')
boxes[0].remove('moon')
boxes[7].append('moon')
boxes[0].append('dress')

# Move the moon and the sun from Box 7 to Box 3.
items_to_move = ['moon', 'sun']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[3].append(item)

# Move the sun and the skirt and the glasses from Box 3 to Box 9.
items_to_move = ['sun', 'skirt', 'glasses']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[9].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")