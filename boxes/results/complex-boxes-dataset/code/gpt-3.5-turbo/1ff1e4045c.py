# Initial state of boxes
boxes = {
    0: [],
    1: ['toy', 'cat', 'laptop', 'charger'],
    2: ['key', 'oven', 'pen', 'pillow', 'razor'],
    3: ['grass', 'shoe', 'needle', 'jungle', 'mask'],
    4: ['beach', 'telescope', 'blanket', 'gloves'],
    5: ['usb'],
    6: [],
    7: ['star', 'lightning'],
    8: ['bracelet', 'car', 'rain', 'sock', 'umbrella'],
    9: ['comb'],
    10: [],
    11: [],
    12: [],
    13: ['drum', 'coin']
}

# Remove the bracelet and the rain from Box 8.
boxes[8].remove('bracelet')
boxes[8].remove('rain')

# Remove the coin from Box 13.
boxes[13].remove('coin')

# Swap the shoe in Box 3 with the star in Box 7.
boxes[3].remove('shoe')
boxes[7].remove('star')
boxes[3].append('star')
boxes[7].append('shoe')

# Remove the cat and the laptop and the charger from Box 1.
items_to_remove = ['cat', 'laptop', 'charger']
for item in items_to_remove:
    boxes[1].remove(item)

# Remove the drum from Box 13.
boxes[13].remove('drum')

# Remove the telescope from Box 4.
boxes[4].remove('telescope')

# Put the blender into Box 6.
boxes[6].append('blender')

# Replace the oven with the puzzle in Box 2.
boxes[2].remove('oven')
boxes[2].append('puzzle')

# Put the piano and the grinder and the speaker into Box 4.
items_to_move = ['piano', 'grinder', 'speaker']
for item in items_to_move:
    boxes[4].append(item)

# Replace the jungle and the star and the mask with the jacket and the tie and the harmonica in Box 3.
boxes[3].remove('jungle')
boxes[3].remove('star')
boxes[3].remove('mask')
boxes[3].append('jacket')
boxes[3].append('tie')
boxes[3].append('harmonica')

# Remove the usb from Box 5.
boxes[5].remove('usb')

# Move the blender from Box 6 to Box 1.
boxes[6].remove('blender')
boxes[1].append('blender')

# Replace the puzzle and the pillow and the pen with the hat and the console and the lion in Box 2.
boxes[2].remove('puzzle')
boxes[2].remove('pillow')
boxes[2].remove('pen')
boxes[2].append('hat')
boxes[2].append('console')
boxes[2].append('lion')

# Swap the umbrella in Box 8 with the lion in Box 2.
boxes[8].remove('umbrella')
boxes[2].remove('lion')
boxes[8].append('lion')
boxes[2].append('umbrella')

# Put the chair and the soap into Box 1.
boxes[1].append('chair')
boxes[1].append('soap')

# Replace the gloves and the piano and the speaker with the skirt and the shirt and the coat in Box 4.
boxes[4].remove('gloves')
boxes[4].remove('piano')
boxes[4].remove('speaker')
boxes[4].append('skirt')
boxes[4].append('shirt')
boxes[4].append('coat')

# Remove the sock from Box 8.
boxes[8].remove('sock')

# Put the forest and the motorcycle into Box 4.
boxes[4].append('forest')
boxes[4].append('motorcycle')

# Swap the comb in Box 9 with the chair in Box 1.
boxes[9].remove('comb')
boxes[1].remove('chair')
boxes[9].append('chair')
boxes[1].append('comb')

# Move the shoe and the lightning from Box 7 to Box 10.
boxes[7].remove('shoe')
boxes[10].append('shoe')
boxes[7].remove('lightning')
boxes[10].append('lightning')

# Remove the shirt from Box 4.
boxes[4].remove('shirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")