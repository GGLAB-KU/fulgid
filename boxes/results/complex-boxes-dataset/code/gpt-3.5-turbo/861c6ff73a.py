# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: [],
    3: ['sandals', 'lamp'],
    4: ['comet', 'coral'],
    5: ['necklace', 'lock', 'card', 'comb'],
    6: ['butterfly', 'magnet'],
    7: ['telescope', 'grass', 'mask', 'sculpture', 'makeup'],
    8: ['planet', 'cloud', 'thunder'],
    9: ['earring'],
    10: ['plate', 'pants', 'seaweed', 'pillow', 'frame'],
    11: ['note']
}

# Put the mirror and the shoe and the pants into Box 8.
boxes[8].append('mirror')
boxes[8].append('shoe')
boxes[8].append('pants')

# Put the zipper and the mountain into Box 9.
boxes[9].append('zipper')
boxes[9].append('mountain')

# Swap the magnet in Box 6 with the coral in Box 4.
boxes[6].remove('magnet')
boxes[4].remove('coral')
boxes[6].append('coral')
boxes[4].append('magnet')

# Replace the butterfly and the coral with the whistle and the thunder in Box 6.
boxes[6].remove('butterfly')
boxes[4].remove('magnet')
boxes[6].append('whistle')
boxes[4].append('thunder')

# Move the note from Box 11 to Box 4.
boxes[11].remove('note')
boxes[4].append('note')

# Put the flute and the forest and the snow into Box 3.
boxes[3].append('flute')
boxes[3].append('forest')
boxes[3].append('snow')

# Move the thunder from Box 8 to Box 2.
boxes[8].remove('thunder')
boxes[2].append('thunder')

# Put the book and the storm and the thread into Box 1.
boxes[1].append('book')
boxes[1].append('storm')
boxes[1].append('thread')

# Put the makeup and the charger into Box 7.
boxes[7].append('makeup')
boxes[7].append('charger')

# Replace the thunder with the telescope in Box 6.
boxes[6].remove('thunder')
boxes[6].append('telescope')

# Remove the cloud and the mirror from Box 8.
boxes[8].remove('cloud')
boxes[8].remove('mirror')

# Swap the storm in Box 1 with the planet in Box 8.
boxes[1].remove('storm')
boxes[8].remove('planet')
boxes[1].append('planet')
boxes[8].append('storm')

# Move the thunder from Box 2 to Box 4.
boxes[2].remove('thunder')
boxes[4].append('thunder')

# Put the lion and the dress and the shelf into Box 4.
boxes[4].append('lion')
boxes[4].append('dress')
boxes[4].append('shelf')

# Replace the seaweed and the plate and the pillow with the blender and the mask and the cow in Box 10.
boxes[10].remove('seaweed')
boxes[10].remove('plate')
boxes[10].remove('pillow')
boxes[10].append('blender')
boxes[10].append('mask')
boxes[10].append('cow')

# Remove the telescope from Box 6.
boxes[6].remove('telescope')

# Put the car into Box 11.
boxes[11].append('car')

# Empty Box 8.
boxes[8] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")