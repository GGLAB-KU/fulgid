# Initial state of boxes
boxes = {
    0: [],
    1: ['blender'],
    2: ['moon', 'magnet', 'harmonica', 'paint', 'coat'],
    3: ['polish', 'sculpture', 'bear', 'hat', 'grinder'],
    4: ['bowl', 'flute', 'toothpaste', 'skirt', 'car'],
    5: ['spoon', 'rock', 'plane', 'shark', 'island'],
    6: ['horse', 'doll'],
    7: ['umbrella', 'telescope', 'whistle']
}

# Swap the skirt in Box 4 with the spoon in Box 5.
boxes[4].remove('skirt')
boxes[5].remove('spoon')
boxes[4].append('spoon')
boxes[5].append('skirt')

# Move the doll from Box 6 to Box 3.
boxes[6].remove('doll')
boxes[3].append('doll')

# Put the speaker into Box 5.
boxes[5].append('speaker')

# Swap the car in Box 4 with the horse in Box 6.
boxes[4].remove('car')
boxes[6].remove('horse')
boxes[4].append('horse')
boxes[6].append('car')

# Remove the hat from Box 3.
boxes[3].remove('hat')

# Remove the rock and the speaker from Box 5.
boxes[5].remove('rock')
boxes[5].remove('speaker')

# Swap the whistle in Box 7 with the plane in Box 5.
boxes[7].remove('whistle')
boxes[5].remove('plane')
boxes[7].append('plane')
boxes[5].append('whistle')

# Put the tie into Box 5.
boxes[5].append('tie')

# Put the leaf and the wallet into Box 1.
boxes[1].append('leaf')
boxes[1].append('wallet')

# Move the plane and the telescope from Box 7 to Box 5.
boxes[7].remove('plane')
boxes[7].remove('telescope')
boxes[5].append('plane')
boxes[5].append('telescope')

# Put the cat into Box 4.
boxes[4].append('cat')

# Move the flute from Box 4 to Box 0.
boxes[4].remove('flute')
boxes[0].append('flute')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")