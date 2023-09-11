# Initial state of boxes
boxes = {
    0: ['needle', 'key', 'shoe'],
    1: ['lamp'],
    2: [],
    3: [],
    4: ['pot', 'microwave', 'rain', 'cup', 'polish'],
    5: [],
    6: ['blender', 'toothbrush', 'guitar', 'wire', 'necklace'],
    7: ['coral', 'horn', 'razor'],
    8: ['starfish']
}

# Replace the key and the needle and the shoe with the vase and the pen and the sun in Box 0.
boxes[0].remove('key')
boxes[0].remove('needle')
boxes[0].remove('shoe')
boxes[0].append('vase')
boxes[0].append('pen')
boxes[0].append('sun')

# Put the thread into Box 2.
boxes[2].append('thread')

# Replace the guitar with the planet in Box 6.
boxes[6].remove('guitar')
boxes[6].append('planet')

# Put the toothpaste and the dolphin and the hat into Box 1.
boxes[1].append('toothpaste')
boxes[1].append('dolphin')
boxes[1].append('hat')

# Move the razor and the coral and the horn from Box 7 to Box 6.
items_to_move = ['razor', 'coral', 'horn']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[6].append(item)

# Put the toothpaste and the phone into Box 0.
boxes[0].append('toothpaste')
boxes[0].append('phone')

# Remove the necklace from Box 6.
boxes[6].remove('necklace')

# Swap the vase in Box 0 with the cup in Box 4.
boxes[0].remove('vase')
boxes[4].remove('cup')
boxes[0].append('cup')
boxes[4].append('vase')

# Remove the dolphin and the lamp from Box 1.
boxes[1].remove('dolphin')
boxes[1].remove('lamp')

# Move the microwave and the polish from Box 4 to Box 0.
boxes[4].remove('microwave')
boxes[4].remove('polish')
boxes[0].append('microwave')
boxes[0].append('polish')

# Move the pot from Box 4 to Box 1.
boxes[4].remove('pot')
boxes[1].append('pot')

# Swap the cup in Box 0 with the starfish in Box 8.
boxes[0].remove('cup')
boxes[8].remove('starfish')
boxes[0].append('starfish')
boxes[8].append('cup')

# Move the rain and the vase from Box 4 to Box 3.
boxes[4].remove('rain')
boxes[4].remove('vase')
boxes[3].append('rain')
boxes[3].append('vase')

# Move the wire and the toothbrush and the blender from Box 6 to Box 4.
items_to_move = ['wire', 'toothbrush', 'blender']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")