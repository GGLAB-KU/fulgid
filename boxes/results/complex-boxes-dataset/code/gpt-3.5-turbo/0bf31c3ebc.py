# Initial state of boxes
boxes = {
    0: ['drum', 'skirt', 'toy', 'snow'],
    1: ['earring', 'vase', 'table'],
    2: ['telescope'],
    3: ['branch', 'horn', 'leaf', 'glasses'],
    4: [],
    5: ['flute', 'scarf', 'toaster'],
    6: ['headphone'],
    7: ['console', 'bracelet'],
    8: ['dog']
}

# Put the key and the flower into Box 4.
boxes[4].append('key')
boxes[4].append('flower')

# Remove the toaster from Box 5.
boxes[5].remove('toaster')

# Remove the headphone from Box 6.
boxes[6].remove('headphone')

# Empty Box 2.
boxes[2] = []

# Replace the dog with the butterfly in Box 8.
boxes[8].remove('dog')
boxes[8].append('butterfly')

# Swap the horn in Box 3 with the bracelet in Box 7.
boxes[3].remove('horn')
boxes[7].remove('bracelet')
boxes[3].append('bracelet')
boxes[7].append('horn')

# Remove the horn from Box 7.
boxes[7].remove('horn')

# Replace the flower and the key with the drum and the earring in Box 4.
boxes[4].remove('flower')
boxes[4].remove('key')
boxes[4].append('drum')
boxes[4].append('earring')

# Empty Box 8.
boxes[8] = []

# Put the key and the crown into Box 3.
boxes[3].append('key')
boxes[3].append('crown')

# Move the earring and the drum from Box 4 to Box 3.
boxes[4].remove('earring')
boxes[4].remove('drum')
boxes[3].append('earring')
boxes[3].append('drum')

# Move the drum and the skirt from Box 0 to Box 1.
boxes[0].remove('drum')
boxes[0].remove('skirt')
boxes[1].append('drum')
boxes[1].append('skirt')

# Move the crown and the key and the leaf from Box 3 to Box 6.
boxes[3].remove('crown')
boxes[3].remove('key')
boxes[3].remove('leaf')
boxes[6].append('crown')
boxes[6].append('key')
boxes[6].append('leaf')

# Replace the console with the whistle in Box 7.
boxes[7].remove('console')
boxes[7].append('whistle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")