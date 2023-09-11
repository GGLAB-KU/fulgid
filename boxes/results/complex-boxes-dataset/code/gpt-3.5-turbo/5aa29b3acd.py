# Initial state of boxes
boxes = {
    0: ['toothbrush'],
    1: [],
    2: ['wig', 'shampoo', 'desert', 'book'],
    3: ['mirror', 'magnet', 'microwave', 'battery'],
    4: ['hat', 'flute', 'thread'],
    5: ['key', 'cow', 'cup'],
    6: ['blanket', 'coral', 'thunder'],
    7: [],
    8: ['bicycle', 'whistle', 'card', 'sock', 'scarf'],
    9: ['horn', 'microscope', 'train'],
    10: ['lipstick', 'polish', 'towel', 'wire'],
    11: ['scissors', 'leaf'],
    12: []
}

# Replace the sock with the telescope in Box 8.
boxes[8].remove('sock')
boxes[8].append('telescope')

# Replace the cup and the key and the cow with the motorcycle and the boot and the thread in Box 5.
boxes[5].remove('cup')
boxes[5].remove('key')
boxes[5].remove('cow')
boxes[5].append('motorcycle')
boxes[5].append('boot')
boxes[5].append('thread')

# Put the plane and the perfume and the tie into Box 9.
boxes[9].append('plane')
boxes[9].append('perfume')
boxes[9].append('tie')

# Remove the thread from Box 4.
boxes[4].remove('thread')

# Replace the hat with the thread in Box 4.
boxes[4].remove('hat')
boxes[4].append('thread')

# Replace the leaf with the headphone in Box 11.
boxes[11].remove('leaf')
boxes[11].append('headphone')

# Remove the thread from Box 4.
boxes[4].remove('thread')

# Put the telescope into Box 0.
boxes[0].append('telescope')

# Put the skirt into Box 7.
boxes[7].append('skirt')

# Put the guitar and the tiger and the sock into Box 10.
boxes[10].append('guitar')
boxes[10].append('tiger')
boxes[10].append('sock')

# Swap the mirror in Box 3 with the skirt in Box 7.
boxes[3].remove('mirror')
boxes[7].remove('skirt')
boxes[3].append('skirt')
boxes[7].append('mirror')

# Put the book and the moon into Box 5.
boxes[5].append('book')
boxes[5].append('moon')

# Move the bicycle and the card and the scarf from Box 8 to Box 3.
items_to_move = ['bicycle', 'card', 'scarf']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[3].append(item)

# Put the bell and the pillow and the card into Box 6.
boxes[6].append('bell')
boxes[6].append('pillow')
boxes[6].append('card')

# Move the mirror from Box 7 to Box 0.
boxes[7].remove('mirror')
boxes[0].append('mirror')

# Put the key into Box 0.
boxes[0].append('key')

# Put the razor and the freezer into Box 8.
boxes[8].append('razor')
boxes[8].append('freezer')

# Move the freezer from Box 8 to Box 0.
boxes[8].remove('freezer')
boxes[0].append('freezer')

# Replace the train with the blanket in Box 9.
boxes[9].remove('train')
boxes[9].append('blanket')

# Put the octopus into Box 8.
boxes[8].append('octopus')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")