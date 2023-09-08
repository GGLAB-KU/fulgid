# Initial state of boxes
boxes = {
    0: ['bird'],
    1: ['flower', 'shoe', 'moon'],
    2: ['oven', 'flute', 'leaf', 'earring'],
    3: ['necklace', 'pot', 'sock'],
    4: ['book'],
    5: ['needle', 'blender', 'dress', 'spoon', 'helmet'],
    6: [],
    7: ['umbrella', 'charger', 'zipper', 'mixer', 'comet'],
    8: ['game', 'harmonica', 'glove', 'horn'],
    9: [],
    10: [],
    11: ['fork', 'lion', 'shirt']
}

# Move the blender and the helmet and the dress from Box 5 to Box 9.
items_to_move = ['blender', 'helmet', 'dress']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[9].append(item)

# Replace the earring and the leaf and the oven with the starfish and the shorts and the flower in Box 2.
boxes[2].remove('earring')
boxes[2].remove('leaf')
boxes[2].remove('oven')
boxes[2].append('starfish')
boxes[2].append('shorts')
boxes[2].append('flower')

# Put the horn and the star into Box 7.
boxes[7].append('horn')
boxes[7].append('star')

# Remove the umbrella and the horn from Box 7.
boxes[7].remove('umbrella')
boxes[7].remove('horn')

# Swap the charger in Box 7 with the book in Box 4.
boxes[7].remove('charger')
boxes[4].remove('book')
boxes[7].append('book')
boxes[4].append('charger')

# Remove the flower and the moon and the shoe from Box 1.
items_to_remove = ['flower', 'moon', 'shoe']
for item in items_to_remove:
    boxes[1].remove(item)

# Replace the needle with the pan in Box 5.
boxes[5].remove('needle')
boxes[5].append('pan')

# Swap the starfish in Box 2 with the charger in Box 4.
boxes[2].remove('starfish')
boxes[4].remove('charger')
boxes[2].append('charger')
boxes[4].append('starfish')

# Replace the game and the glove with the tiger and the bracelet in Box 8.
boxes[8].remove('game')
boxes[8].remove('glove')
boxes[8].append('tiger')
boxes[8].append('bracelet')

# Swap the spoon in Box 5 with the dress in Box 9.
boxes[5].remove('spoon')
boxes[9].remove('dress')
boxes[5].append('dress')
boxes[9].append('spoon')

# Put the thunder into Box 11.
boxes[11].append('thunder')

# Replace the starfish with the vase in Box 4.
boxes[4].remove('starfish')
boxes[4].append('vase')

# Move the bracelet from Box 8 to Box 11.
boxes[8].remove('bracelet')
boxes[11].append('bracelet')

# Move the horn from Box 8 to Box 2.
boxes[8].remove('horn')
boxes[2].append('horn')

# Put the glove and the freezer and the lock into Box 10.
boxes[10].append('glove')
boxes[10].append('freezer')
boxes[10].append('lock')

# Remove the harmonica from Box 8.
boxes[8].remove('harmonica')

# Swap the dress in Box 5 with the bird in Box 0.
boxes[5].remove('dress')
boxes[0].remove('bird')
boxes[5].append('bird')
boxes[0].append('dress')

# Replace the book with the dolphin in Box 7.
boxes[7].remove('book')
boxes[7].append('dolphin')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")